from django.shortcuts import render

# Create your views here.
import json


from dateutil.relativedelta import relativedelta

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView, settings
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser


from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password
from django.db import DatabaseError, DataError, IntegrityError

from drf_spectacular.utils import extend_schema

from .models import *
from erp.models import *
from .serializers import *

from django.core.mail import send_mail
from django.conf import settings


import razorpay

from django.conf import settings
from django.utils import timezone








# ============= ADMIN APP VIEWS =============


@method_decorator(csrf_exempt, name='dispatch')
class UserLoginAPIView(APIView):

    @extend_schema(request=LoginSerializer)
    def post(self, request):
        try:
            identifier = request.data.get("identifier")
            password = request.data.get("password")
            print(identifier, password)

            if not identifier or not password:
                return Response(
                    {
                        "status": "error",
                        "message": "Please provide email/phone number and password."
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Search by email or phone number
            user = Users.objects.filter(email=identifier).first()

            if not user:
                user = Users.objects.filter(phone_number=identifier).first()

            if not user:
                return Response(
                    {
                        "status": "error",
                        "message": "Invalid credentials."
                    },
                    status=status.HTTP_401_UNAUTHORIZED
                )

            # Password verification
            # if not check_password(password, user.password):
            #     return Response(
            #         {
            #             "status": "error",
            #             "message": "Invalid password."
            #         },
            #         status=status.HTTP_401_UNAUTHORIZED
            #     )

            if password != user.password:
                return Response(
                    {
                        "status": "error",
                        "message": "Invalid password."
                    },
                    status=status.HTTP_401_UNAUTHORIZED
                )

            return Response(
                {
                    "status": "success",
                    "message": "Login successful",

                    "user": {
                        "id": user.id,
                        "full_name": user.full_name,
                        "email": user.email,
                        "phone_number": user.phone_number,
                        "role": user.role,
                        "user_type_id": user.user_type_id
                    }
                },
                status=status.HTTP_200_OK
            )

        except Exception as e:
            return Response(
                {
                    "status": "error",
                    "message": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )




@method_decorator(csrf_exempt, name='dispatch')
class UserLogoutAPIView(APIView):

    @extend_schema(request=LogoutSerializer)
    def post(self, request):

        try:

            user_id = request.data.get("user_id")

            if not user_id:
                return Response(
                    {
                        "status": "error",
                        "message": "user_id is required."
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            user = Users.objects.filter(id=user_id).first()

            if not user:
                return Response(
                    {
                        "status": "error",
                        "message": "User not found."
                    },
                    status=status.HTTP_404_NOT_FOUND
                )

            return Response(
                {
                    "status": "success",
                    "message": "Logout successful."
                },
                status=status.HTTP_200_OK
            )

        except Exception as e:
            return Response(
                {
                    "status": "error",
                    "message": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@method_decorator(csrf_exempt, name='dispatch')
class UserListCreateAPIView(APIView):
    """
    API view for listing all users and creating new users.
    
    GET: Retrieve a list of all users
    POST: Create a new user
    """
    
    def get(self, request):
        try:
            users = Users.objects.all().order_by('-id')
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(request=UserSerializer)
    def post(self, request):
        try:
            email = request.data.get('email')
            phone_number = request.data.get('phone_number')

            # Validation checks
            if Users.objects.filter(email=email).exists():
                return Response({'error': 'This email already exists.'}, status=status.HTTP_400_BAD_REQUEST)
            
            if Users.objects.filter(phone_number=phone_number).exists():
                return Response({'error': 'This phone number already exists.'}, status=status.HTTP_400_BAD_REQUEST)

            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        'status': 'success',
                        'message': 'User created successfully',
                        'data': serializer.data
                    },
                    status=status.HTTP_201_CREATED
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@method_decorator(csrf_exempt, name='dispatch')
class UserRetrieveUpdateDeleteAPIView(APIView):
    """
    API view for retrieving, updating, and deleting a specific user.
    
    GET: Retrieve a user by ID
    PUT: Update a user
    DELETE: Delete a user
    """
    
    def get_object(self, pk):
        try:
            return Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            return None

    def get(self, request, pk):
        try:
            user = self.get_object(pk)
            if not user:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(request=UserSerializer)
    def put(self, request, pk):
        try:
            user = self.get_object(pk)
            if not user:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        'status': 'success',
                        'message': 'User updated successfully',
                        'data': serializer.data
                    },
                    status=status.HTTP_200_OK
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            user = self.get_object(pk)
            if not user:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
            
            user_name = user.full_name
            user.delete()
            return Response(
                {
                    'status': 'success',
                    'message': f'User "{user_name}" deleted successfully'
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





# ============= SCHEME API VIEWS =============

@method_decorator(csrf_exempt, name='dispatch')
class SchemeListCreateAPIView(APIView):
    """
    API view for listing all schemes and creating new schemes.
    
    GET: Retrieve a list of all schemes
    POST: Create a new scheme
    """
    
    def get(self, request):
        try:
            schemes = Scheme.objects.all().order_by('-created_at')
            serializer = SchemeSerializer(schemes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(request=SchemeSerializer)
    def post(self, request):
        try:
            scheme_name = request.data.get('scheme_name')

            # Validation check
            if Scheme.objects.filter(scheme_name__iexact=scheme_name).exists():
                return Response({'error': 'This scheme name already exists.'}, status=status.HTTP_400_BAD_REQUEST)

            serializer = SchemeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        'status': 'success',
                        'message': 'Scheme created successfully',
                        'data': serializer.data
                    },
                    status=status.HTTP_201_CREATED
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@method_decorator(csrf_exempt, name='dispatch')
class SchemeRetrieveUpdateDeleteAPIView(APIView):
    """
    API view for retrieving, updating, and deleting a specific scheme.
    
    GET: Retrieve a scheme by ID
    PUT: Update a scheme
    DELETE: Delete a scheme
    """
    
    def get_object(self, pk):
        try:
            return Scheme.objects.get(scheme_id=pk)
        except Scheme.DoesNotExist:
            return None

    def get(self, request, pk):
        try:
            scheme = self.get_object(pk)
            if not scheme:
                return Response({'error': 'Scheme not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = SchemeSerializer(scheme)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(request=SchemeSerializer)
    def put(self, request, pk):
        try:
            scheme = self.get_object(pk)
            if not scheme:
                return Response({'error': 'Scheme not found'}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = SchemeSerializer(scheme, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        'status': 'success',
                        'message': 'Scheme updated successfully',
                        'data': serializer.data
                    },
                    status=status.HTTP_200_OK
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            scheme = self.get_object(pk)
            if not scheme:
                return Response({'error': 'Scheme not found'}, status=status.HTTP_404_NOT_FOUND)
            
            scheme_name = scheme.scheme_name
            scheme.delete()
            return Response(
                {
                    'status': 'success',
                    'message': f'Scheme "{scheme_name}" deleted successfully'
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


def send_customer_credentials(customer, plain_password):
    try:
        subject = "Welcome to Manikanta Jewellery Schemes"

        message = f"""
                    Dear {customer.account_name},

                    Welcome to Manikanta Jewellery Schemes.

                    Your account has been created successfully.

                    Login Credentials:

                    Email: {customer.email}
                    Phone Number: {customer.mobile or customer.phone}

                    Please change your password after your first login.

                    Regards,
                    Manikanta Jewellery Team

                    """

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [customer.email],
            fail_silently=False
        )

        return True

    except Exception as e:
        print("Email Error:", str(e))
        return False  


@method_decorator(csrf_exempt, name="dispatch")
class CustomerListCreateAPIView(APIView):

    # parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get(self, request):
        customers = AccountDetails.objects.all().order_by("-created_at")
        serializer = CustomerSerializer(customers, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(request=CustomerSerializer)
    def post(self, request):

        serializer = CustomerSerializer(data=request.data)

        if serializer.is_valid():
            try:
                customer = serializer.save()
            except (DataError, DatabaseError, IntegrityError) as e:
                return Response(
                    {"status": "error", "message": "Database error during create.", "details": str(e)},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            if customer.password:
                send_customer_credentials(
                    customer,
                    customer.password,
                )

            return Response(
                {
                    "status": "success",
                    "message": "Customer created successfully.",
                    "data": CustomerSerializer(customer).data,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )
    

@method_decorator(csrf_exempt, name="dispatch")
class CustomerRetrieveUpdateDeleteAPIView(APIView):

    # parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_object(self, pk):
        try:
            return AccountDetails.objects.get(account_id=pk)
        except AccountDetails.DoesNotExist:
            return None

    def get(self, request, pk):

        customer = self.get_object(pk)

        if not customer:
            return Response(
                {"error": "Customer not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = CustomerSerializer(customer)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    @extend_schema(request=CustomerSerializer)
    def put(self, request, pk):

        customer = self.get_object(pk)

        if not customer:
            return Response(
                {"error": "Customer not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = CustomerSerializer(
            customer,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():

            try:
                customer = serializer.save()
            except (DataError, DatabaseError, IntegrityError) as e:
                return Response(
                    {"status": "error", "message": "Database error during update.", "details": str(e)},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            return Response(
                {
                    "status": "success",
                    "message": "Customer updated successfully.",
                    "data": CustomerSerializer(customer).data,
                },
                status=status.HTTP_200_OK,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, pk):

        customer = self.get_object(pk)

        if not customer:
            return Response(
                {"error": "Customer not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        name = customer.account_name

        customer.delete()

        return Response(
            {
                "status": "success",
                "message": f'Customer "{name}" deleted successfully.',
            },
            status=status.HTTP_200_OK,
        )


@method_decorator(csrf_exempt, name='dispatch')
class CustomerSchemeEnrollmentListCreateAPIView(APIView):

    def get(self, request):

        try:

            enrollments = (
                CustomerSchemeEnrollment.objects
                .select_related(
                    'customer',
                    'scheme'
                )
                .order_by('-created_at')
            )

            serializer = CustomerSchemeEnrollmentSerializer(
                enrollments,
                many=True
            )

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        except Exception as e:

            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @extend_schema(
        request=CustomerSchemeEnrollmentSerializer
    )

    def post(self, request):

        try:

            customer_id = request.data.get('customer')
            scheme_id = request.data.get('scheme')

            if not customer_id:
                return Response(
                    {'error': 'Customer is required'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            if not scheme_id:
                return Response(
                    {'error': 'Scheme is required'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            customer = AccountDetails.objects.get(
                pk=customer_id
            )

            scheme = Scheme.objects.get(
                pk=scheme_id
            )

            created_by_user = None
            if getattr(request, 'user', None) and request.user.is_authenticated:
                created_by_user = (
                    Users.objects.filter(email=getattr(request.user, 'email', None)).first() or
                    Users.objects.filter(user_name=getattr(request.user, 'username', None)).first()
                )

            enrollment = CustomerSchemeEnrollment.objects.create(
                customer=customer,
                scheme=scheme,
                enrollment_date=timezone.now().date(),

                maturity_date=(
                    timezone.now().date() +
                    relativedelta(
                        months=scheme.scheme_maturity_period
                    )
                ),

                installment_amount=scheme.scheme_installment_amount,

                total_installments=scheme.payable_installments,

                remarks=request.data.get(
                    'remarks'
                ),

                created_by=created_by_user
            )

            # Auto Generate Installments

            for i in range(
                1,
                scheme.payable_installments + 1
            ):

                SchemeInstallment.objects.create(
                    enrollment=enrollment,
                    installment_no=i,

                    due_date=(
                        enrollment.enrollment_date +
                        relativedelta(months=i - 1)
                    ),

                    amount=scheme.scheme_installment_amount
                )

            serializer = CustomerSchemeEnrollmentSerializer(
                enrollment
            )

            return Response(
                {
                    'status': 'success',
                    'message': 'Enrollment created successfully',
                    'data': serializer.data
                },
                status=status.HTTP_201_CREATED
            )

        except AccountDetails.DoesNotExist:

            return Response(
                {'error': 'Customer not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        except Scheme.DoesNotExist:

            return Response(
                {'error': 'Scheme not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        except Exception as e:

            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        

@method_decorator(csrf_exempt, name='dispatch')
class CustomerSchemeEnrollmentRetrieveUpdateDeleteAPIView(APIView):

    def get_object(self, pk):

        try:
            return CustomerSchemeEnrollment.objects.get(
                pk=pk
            )
        except CustomerSchemeEnrollment.DoesNotExist:
            return None

    def get(self, request, pk):

        enrollment = self.get_object(pk)

        if not enrollment:

            return Response(
                {'error': 'Enrollment not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CustomerSchemeEnrollmentSerializer(
            enrollment
        )

        return Response(
            serializer.data
        )
    
    @extend_schema(
        request=CustomerSchemeEnrollmentSerializer
    )
    def put(self, request, pk):

        try:

            enrollment = self.get_object(pk)

            if not enrollment:

                return Response(
                    {
                        'error': 'Enrollment not found'
                    },
                    status=status.HTTP_404_NOT_FOUND
                )

            update_data = {
                'remarks': request.data.get(
                    'remarks',
                    enrollment.remarks
                ),

                'status': request.data.get(
                    'status',
                    enrollment.status
                ),

                'maturity_date': request.data.get(
                    'maturity_date',
                    enrollment.maturity_date
                )
            }

            customer_id = request.data.get('customer')
            if customer_id:
                customer = AccountDetails.objects.filter(
                    account_id=customer_id
                ).first()
                if not customer:
                    return Response(
                        {'error': 'Customer not found'},
                        status=status.HTTP_404_NOT_FOUND
                    )
                update_data['customer'] = customer.account_id

            scheme_id = request.data.get('scheme')
            if scheme_id:
                scheme = Scheme.objects.filter(
                    scheme_id=scheme_id
                ).first()
                if not scheme:
                    return Response(
                        {'error': 'Scheme not found'},
                        status=status.HTTP_404_NOT_FOUND
                    )
                update_data['scheme'] = scheme.scheme_id

            serializer = CustomerSchemeEnrollmentSerializer(
                enrollment,
                data=update_data,
                partial=True
            )

            if serializer.is_valid():

                serializer.save()

                return Response(
                    {
                        'status': 'success',
                        'message':
                        'Enrollment updated successfully',
                        'data': serializer.data
                    },
                    status=status.HTTP_200_OK
                )

            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        except Exception as e:

            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, request, pk):

        enrollment = self.get_object(pk)

        if not enrollment:

            return Response(
                {'error': 'Enrollment not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        enrollment.delete()

        return Response(
            {
                'status': 'success',
                'message': 'Enrollment deleted successfully'
            }
        )


@method_decorator(csrf_exempt, name='dispatch')
class SchemeInstallmentListAPIView(APIView):

    def get(self, request):

        try:

            enrollment_id = request.GET.get(
                'enrollment_id'
            )

            installments = (
                SchemeInstallment.objects
                .select_related(
                    'enrollment',
                    'enrollment__customer',
                    'enrollment__scheme'
                )
            )

            if enrollment_id:

                installments = installments.filter(
                    enrollment_id=enrollment_id
                )

            serializer = SchemeInstallmentSerializer(
                installments,
                many=True
            )

            return Response(
                serializer.data
            )

        except Exception as e:

            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        

@method_decorator(csrf_exempt, name='dispatch')
class PayInstallmentAPIView(APIView):

    @extend_schema(
        request=PayInstallmentRequestSerializer
    )
    def post(self, request, pk):

        try:

            installment = SchemeInstallment.objects.get(
                pk=pk
            )

            if installment.status == 'paid':

                return Response(
                    {
                        'error': 'Installment already paid'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            installment.paid_amount = request.data.get(
                'paid_amount',
                installment.amount
            )

            installment.paid_date = timezone.now().date()

            installment.receipt_number = request.data.get(
                'receipt_number'
            )

            installment.payment_mode = request.data.get(
                'payment_mode'
            )

            installment.transaction_reference = request.data.get(
                'transaction_reference'
            )

            installment.status = 'paid'

            installment.save()

            serializer = PayInstallmentSerializer(
                installment
            )

            return Response(
                {
                    'status': 'success',
                    'message': 'Installment paid successfully',
                    'data': serializer.data
                },
                status=status.HTTP_200_OK
            )

        except SchemeInstallment.DoesNotExist:

            return Response(
                {
                    'error': 'Installment not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        except Exception as e:

            return Response(
                {
                    'error': str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        


# ============= CUSTOMER APP VIEWS =============


@method_decorator(csrf_exempt, name='dispatch')
class CustomerLoginAPIView(APIView):

    @extend_schema(request=CustomerLoginSerializer)
    def post(self, request):

        try:

            identifier = request.data.get("identifier")
            password = request.data.get("password")

            if not identifier or not password:
                return Response(
                    {
                        "status": "error",
                        "message": "Please provide email/mobile and password."
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            customer = AccountDetails.objects.filter(
                email=identifier
            ).first()

            if not customer:
                customer = AccountDetails.objects.filter(
                    mobile=identifier
                ).first()

            if not customer:
                return Response(
                    {
                        "status": "error",
                        "message": "Customer not found."
                    },
                    status=status.HTTP_404_NOT_FOUND
                )

            # If password is stored as plain text
            if password != customer.password:
                return Response(
                    {
                        "status": "error",
                        "message": "Invalid password."
                    },
                    status=status.HTTP_401_UNAUTHORIZED
                )

            # If passwords are hashed, replace the above block with:
            # if not check_password(password, customer.password):

            return Response(
                {
                    "status": "success",
                    "message": "Login successful",

                    "customer": {
                        "customer_id": customer.account_id,
                        "customer_name": customer.account_name,
                        "email": customer.email,
                        "phone_number": customer.mobile,
                        "city": customer.city,
                        "address": customer.address1,
                        "kyc_status": customer.kyc_status,
                        "customer_referral_code": customer.customer_referral_code
                    }
                },
                status=status.HTTP_200_OK
            )

        except Exception as e:

            return Response(
                {
                    "status": "error",
                    "message": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
@method_decorator(csrf_exempt, name='dispatch')
class CustomerLogoutAPIView(APIView):

    @extend_schema(request=CustomerLogoutSerializer)
    def post(self, request):

        try:

            customer_id = request.data.get("customer_id")

            if not customer_id:
                return Response(
                    {
                        "status": "error",
                        "message": "customer_id is required."
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            customer = AccountDetails.objects.filter(
                account_id=customer_id
            ).first()

            if not customer:
                return Response(
                    {
                        "status": "error",
                        "message": "Customer not found."
                    },
                    status=status.HTTP_404_NOT_FOUND
                )

            return Response(
                {
                    "status": "success",
                    "message": f'Customer "{customer.account_name}" logged out successfully.',
                    "customer_id": customer.account_id
                },
                status=status.HTTP_200_OK
            )

        except Exception as e:

            return Response(
                {
                    "status": "error",
                    "message": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        

@method_decorator(csrf_exempt, name='dispatch')
class CustomerSchemesAPIView(APIView):

    def get(self, request, customer_id):

        try:

            customer = AccountDetails.objects.get(
                account_id=customer_id
            )

            enrollments = (
                CustomerSchemeEnrollment.objects
                .select_related(
                    'scheme'
                )
                .filter(
                    customer=customer
                )
                .order_by(
                    '-created_at'
                )
            )

            serializer = CustomerSchemeSerializer(
                enrollments,
                many=True
            )

            return Response(
                {
                    'status': 'success',
                    'customer_id': customer.account_id,
                    'customer_name': customer.account_name,
                    'total_schemes': enrollments.count(),
                    'data': serializer.data
                },
                status=status.HTTP_200_OK
            )

        except AccountDetails.DoesNotExist:

            return Response(
                {
                    'error': 'Customer not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        except Exception as e:

            return Response(
                {
                    'error': str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

@method_decorator(csrf_exempt, name='dispatch')
class CustomerSchemeDetailAPIView(APIView):

    def get(self, request, enrollment_id):

        try:

            enrollment = (
                CustomerSchemeEnrollment.objects
                .select_related(
                    'customer',
                    'scheme'
                )
                .get(
                    pk=enrollment_id
                )
            )

            serializer = (
                CustomerSchemeDetailSerializer(
                    enrollment
                )
            )

            next_installment = (
                SchemeInstallment.objects
                .filter(
                    enrollment=enrollment,
                    status='pending'
                )
                .order_by(
                    'installment_no'
                )
                .first()
            )

            next_due = None

            if next_installment:

                next_due = {
                    'installment_id':
                    next_installment.installment_id,

                    'installment_no':
                    next_installment.installment_no,

                    'due_date':
                    next_installment.due_date,

                    'amount':
                    next_installment.amount,

                    'status':
                    next_installment.status
                }

            return Response(
                {
                    'status': 'success',
                    'data': serializer.data,
                    'next_due_installment': next_due
                },
                status=status.HTTP_200_OK
            )

        except CustomerSchemeEnrollment.DoesNotExist:

            return Response(
                {
                    'error':
                    'Scheme enrollment not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        except Exception as e:

            return Response(
                {
                    'error': str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
@method_decorator(csrf_exempt, name='dispatch')
class CustomerSchemeInstallmentsAPIView(APIView):

    def get(self, request, enrollment_id):

        try:

            enrollment = (
                CustomerSchemeEnrollment.objects.get(
                    pk=enrollment_id
                )
            )

            installments = (
                SchemeInstallment.objects.filter(
                    enrollment=enrollment
                ).order_by(
                    'installment_no'
                )
            )

            serializer = (
                CustomerSchemeInstallmentSerializer(
                    installments,
                    many=True
                )
            )

            return Response(
                {
                    'status': 'success',

                    'enrollment_id':
                    enrollment.enrollment_id,

                    'enrollment_number':
                    enrollment.enrollment_number,

                    'scheme_name':
                    enrollment.scheme.scheme_name,

                    'total_installments':
                    enrollment.total_installments,

                    'paid_installments':
                    enrollment.paid_installments,

                    'pending_installments':
                    enrollment.pending_installments,

                    'data':
                    serializer.data
                },
                status=status.HTTP_200_OK
            )

        except CustomerSchemeEnrollment.DoesNotExist:

            return Response(
                {
                    'error':
                    'Enrollment not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        except Exception as e:

            return Response(
                {
                    'error': str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )        










class SchemeInitiateRazorpayAPIView_old(APIView):

    def post(self, request):

        try:
            installment_id = request.data.get("installment_id")

            if not installment_id:
                return Response(
                    {
                        "error": "installment_id is required"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            installment = SchemeInstallment.objects.get(
                pk=installment_id
            )

            client = razorpay.Client(
                auth=(
                    settings.RAZORPAY_KEY_ID,
                    settings.RAZORPAY_KEY_SECRET
                )
            )

            amount = int(
                float(installment.amount) * 100
            )

            order = client.order.create({
                "amount": amount,
                "currency": "INR",
                "payment_capture": 1
            })

            txn = SchemeTransaction.objects.create(
                installment=installment,
                customer=installment.enrollment.customer,
                enrollment=installment.enrollment,
                scheme = installment.enrollment.scheme,
                amount=installment.amount,
                razorpay_order_id=order["id"],
                status="pending"
            )

            return Response(
                {
                    "key": settings.RAZORPAY_KEY_ID,
                    "order_id": order["id"],
                    "amount": amount,
                    "transaction_id": txn.transaction_id
                },
                status=status.HTTP_200_OK
            )

        except SchemeInstallment.DoesNotExist:
            return Response(
                {
                    "error": "Installment not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )

        except Exception as e:
            return Response(
                {
                    "error": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )







class SchemeConfirmRazorpayAPIView_old(APIView):

    def post(self, request):

        order_id = request.data.get(
            "razorpay_order_id"
        )

        payment_id = request.data.get(
            "razorpay_payment_id"
        )

        signature = request.data.get(
            "razorpay_signature"
        )

        if not order_id:
            return Response(
                {
                    "status": "failed",
                    "error": "razorpay_order_id is required"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if not payment_id:
            return Response(
                {
                    "status": "failed",
                    "error": "razorpay_payment_id is required"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if not signature:
            return Response(
                {
                    "status": "failed",
                    "error": "razorpay_signature is required"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        client = razorpay.Client(
            auth=(
                settings.RAZORPAY_KEY_ID,
                settings.RAZORPAY_KEY_SECRET
            )
        )

        try:

            # Verify Signature
            client.utility.verify_payment_signature({
                "razorpay_order_id": order_id,
                "razorpay_payment_id": payment_id,
                "razorpay_signature": signature
            })

            txn = SchemeTransaction.objects.get(
                razorpay_order_id=order_id
            )

            # Prevent duplicate processing
            if txn.status == "success":
                return Response(
                    {
                        "status": "success",
                        "message": "Payment already verified"
                    },
                    status=status.HTTP_200_OK
                )

            # Fetch payment details from Razorpay
            payment_details = client.payment.fetch(
                payment_id
            )

            payment_method = payment_details.get(
                "method",
                "unknown"
            )

            # Update Transaction
            txn.razorpay_payment_id = payment_id
            txn.razorpay_signature = signature
            txn.payment_method = payment_method
            txn.status = "success"
            txn.save()

            # Update Installment
            installment = txn.installment

            installment.paid_amount = txn.amount
            installment.paid_date = timezone.now().date()
            installment.payment_mode = payment_method
            installment.transaction_reference = payment_id
            installment.status = "paid"
            installment.save()

            # Generate Receipt Number
            receipt_number = (
                f"RCPT"
                f"{timezone.now().strftime('%Y%m%d%H%M%S')}"
            )

            # Create Receipt
            receipt = SchemeReceipt.objects.create(
                installment=installment,
                receipt_number=receipt_number,
                amount=txn.amount,
                payment_mode=payment_method,
                transaction_reference=payment_id
            )

            return Response(
                {
                    "status": "success",
                    "message": "Payment verified successfully",
                    "receipt_no": receipt.receipt_number,
                    "payment_method": payment_method,
                    "installment_id": installment.installment_id,
                    "transaction_id": txn.transaction_id
                },
                status=status.HTTP_200_OK
            )

        except SchemeTransaction.DoesNotExist:

            return Response(
                {
                    "status": "failed",
                    "error": "Transaction not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )

        except Exception as e:

            # Mark transaction failed if exists
            try:
                txn = SchemeTransaction.objects.get(
                    razorpay_order_id=order_id
                )

                txn.status = "failed"
                txn.save()

            except Exception:
                pass

            return Response(
                {
                    "status": "failed",
                    "error": str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )

    






from decimal import Decimal, InvalidOperation

from django.db import transaction
from django.db.models import Sum
from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import razorpay

from django.conf import settings

from drf_spectacular.utils import extend_schema


class SchemeInitiateRazorpayAPIView(APIView):

    """
    Initiate Razorpay payment for an existing scheme installment.

    Supports:

    1. Full installment payment
    2. Partial installment payment

    This API is NOT used for new scheme enrollment.

    New scheme enrollment is handled by:
        SchemeEnrollmentInitiateRazorpayAPIView
    """

    @extend_schema(
        request=None
    )
    def post(self, request):

        installment_id = request.data.get("installment_id")
        payment_amount = request.data.get("payment_amount")

        # ============================================================
        # VALIDATION
        # ============================================================

        if not installment_id:
            return Response(
                {
                    "success": False,
                    "message": "installment_id is required."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if payment_amount is None:
            return Response(
                {
                    "success": False,
                    "message": "payment_amount is required."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # ============================================================
        # GET INSTALLMENT
        # ============================================================

        try:

            installment = (
                SchemeInstallment.objects
                .select_related(
                    "enrollment",
                    "enrollment__customer",
                    "enrollment__scheme",
                )
                .get(
                    installment_id=installment_id
                )
            )

        except SchemeInstallment.DoesNotExist:

            return Response(
                {
                    "success": False,
                    "message": "Installment not found."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        enrollment = installment.enrollment
        customer = enrollment.customer
        scheme = enrollment.scheme

        # ============================================================
        # CHECK ENROLLMENT
        # ============================================================

        if enrollment.status != "active":

            return Response(
                {
                    "success": False,
                    "message": (
                        "Payment cannot be made because "
                        "the scheme enrollment is not active."
                    )
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # ============================================================
        # CHECK INSTALLMENT STATUS
        # ============================================================

        if installment.status == "paid":

            return Response(
                {
                    "success": False,
                    "message": "This installment is already fully paid."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if installment.status == "cancelled":

            return Response(
                {
                    "success": False,
                    "message": "This installment has been cancelled."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # ============================================================
        # CALCULATE REMAINING AMOUNT
        # ============================================================

        installment_amount = Decimal(
            str(installment.amount)
        )

        already_paid = Decimal(
            str(installment.paid_amount or 0)
        )

        remaining_amount = (
            installment_amount - already_paid
        )

        if remaining_amount <= Decimal("0.00"):

            return Response(
                {
                    "success": False,
                    "message": "This installment is already fully paid."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # ============================================================
        # VALIDATE PAYMENT AMOUNT
        # ============================================================

        try:

            payment_amount = Decimal(
                str(payment_amount)
            )

        except (InvalidOperation, ValueError):

            return Response(
                {
                    "success": False,
                    "message": "Invalid payment_amount."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        payment_amount = payment_amount.quantize(
            Decimal("0.01")
        )

        if payment_amount <= Decimal("0.00"):

            return Response(
                {
                    "success": False,
                    "message": "payment_amount must be greater than zero."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # ============================================================
        # PAYMENT CANNOT EXCEED REMAINING AMOUNT
        # ============================================================

        if payment_amount > remaining_amount:

            return Response(
                {
                    "success": False,
                    "message": (
                        f"Payment amount cannot exceed the remaining "
                        f"installment amount of ₹{remaining_amount}."
                    ),
                    "installment_amount": str(installment_amount),
                    "already_paid": str(already_paid),
                    "remaining_amount": str(remaining_amount),
                    "requested_amount": str(payment_amount),
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # ============================================================
        # CHECK EXISTING PENDING TRANSACTION
        # ============================================================

        pending_transaction = (
            SchemeTransaction.objects
            .filter(
                enrollment=enrollment,
                installment=installment,
                status="pending"
            )
            .order_by("-transaction_id")
            .first()
        )

        if pending_transaction:

            return Response(
                {
                    "success": True,
                    "message": "Pending payment already exists.",
                    "razorpay_key": settings.RAZORPAY_KEY_ID,
                    "razorpay_order_id": (
                        pending_transaction.razorpay_order_id
                    ),
                    "transaction_id": (
                        pending_transaction.transaction_id
                    ),
                    "customer_id": customer.pk,
                    "scheme_id": scheme.pk,
                    "enrollment_id": enrollment.pk,
                    "installment_id": installment.installment_id,
                    "installment_no": installment.installment_no,
                    "installment_amount": str(
                        installment_amount
                    ),
                    "already_paid": str(
                        already_paid
                    ),
                    "remaining_amount": str(
                        remaining_amount
                    ),
                    "payment_amount": str(
                        pending_transaction.amount
                    ),
                },
                status=status.HTTP_200_OK
            )

        # ============================================================
        # CREATE RAZORPAY ORDER
        # ============================================================

        razorpay_amount = int(
            payment_amount * Decimal("100")
        )

        try:

            client = razorpay.Client(
                auth=(
                    settings.RAZORPAY_KEY_ID,
                    settings.RAZORPAY_KEY_SECRET
                )
            )

            razorpay_order = client.order.create(
                {
                    "amount": razorpay_amount,
                    "currency": "INR",
                    "payment_capture": 1,
                }
            )

        except Exception as e:

            return Response(
                {
                    "success": False,
                    "message": "Unable to create Razorpay order.",
                    "error": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        # ============================================================
        # CREATE TRANSACTION
        # ============================================================

        txn = SchemeTransaction.objects.create(

            customer=customer,

            scheme=scheme,

            enrollment=enrollment,

            installment=installment,

            amount=payment_amount,

            razorpay_order_id=razorpay_order["id"],

            status="pending",

            remarks=(
                f"Installment #{installment.installment_no} "
                f"payment."
            )
        )

        # ============================================================
        # RESPONSE
        # ============================================================

        return Response(
            {
                "success": True,
                "message": "Razorpay payment order created successfully.",

                "razorpay_key": settings.RAZORPAY_KEY_ID,

                "razorpay_order_id": (
                    razorpay_order["id"]
                ),

                "transaction_id": txn.transaction_id,

                "customer_id": customer.pk,

                "scheme_id": scheme.pk,

                "enrollment_id": enrollment.pk,

                "installment_id": (
                    installment.installment_id
                ),

                "installment_no": (
                    installment.installment_no
                ),

                "installment_amount": str(
                    installment_amount
                ),

                "already_paid": str(
                    already_paid
                ),

                "remaining_amount": str(
                    remaining_amount
                ),

                "payment_amount": str(
                    payment_amount
                ),
            },
            status=status.HTTP_201_CREATED
        )



class SchemeConfirmRazorpayAPIView(APIView):

    """
    Confirm Razorpay payment for an existing scheme installment.

    Supports:

    - Full installment payment
    - Partial installment payment
    - Multiple partial payments for the same installment

    This API is NOT used for new scheme enrollment.
    """

    @extend_schema(
        request=None
    )
    @transaction.atomic
    def post(self, request):

        razorpay_order_id = request.data.get(
            "razorpay_order_id"
        )

        razorpay_payment_id = request.data.get(
            "razorpay_payment_id"
        )

        razorpay_signature = request.data.get(
            "razorpay_signature"
        )

        # ============================================================
        # VALIDATION
        # ============================================================

        if not razorpay_order_id:

            return Response(
                {
                    "success": False,
                    "message": "razorpay_order_id is required."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if not razorpay_payment_id:

            return Response(
                {
                    "success": False,
                    "message": "razorpay_payment_id is required."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if not razorpay_signature:

            return Response(
                {
                    "success": False,
                    "message": "razorpay_signature is required."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # ============================================================
        # VERIFY RAZORPAY SIGNATURE
        # ============================================================

        try:

            client = razorpay.Client(
                auth=(
                    settings.RAZORPAY_KEY_ID,
                    settings.RAZORPAY_KEY_SECRET
                )
            )

            client.utility.verify_payment_signature(
                {
                    "razorpay_order_id": razorpay_order_id,
                    "razorpay_payment_id": razorpay_payment_id,
                    "razorpay_signature": razorpay_signature,
                }
            )

        except razorpay.errors.SignatureVerificationError:

            return Response(
                {
                    "success": False,
                    "message": "Invalid Razorpay payment signature."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        except Exception as e:

            return Response(
                {
                    "success": False,
                    "message": "Payment verification failed.",
                    "error": str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # ============================================================
        # GET TRANSACTION WITH LOCK
        # ============================================================

        try:

            txn = (
                SchemeTransaction.objects
                .select_for_update()
                .select_related(
                    "customer",
                    "scheme",
                    "enrollment",
                    "installment",
                )
                .get(
                    razorpay_order_id=razorpay_order_id
                )
            )

        except SchemeTransaction.DoesNotExist:

            return Response(
                {
                    "success": False,
                    "message": "Payment transaction not found."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        # ============================================================
        # IDEMPOTENCY
        # ============================================================

        if txn.status == "success":

            return Response(
                {
                    "success": True,
                    "message": "Payment already verified successfully.",
                    "transaction_id": txn.transaction_id,
                    "razorpay_payment_id": (
                        txn.razorpay_payment_id
                    ),
                    "status": "success",
                },
                status=status.HTTP_200_OK
            )

        # ============================================================
        # VALIDATE TRANSACTION TYPE
        # ============================================================

        if txn.enrollment is None or txn.installment is None:

            return Response(
                {
                    "success": False,
                    "message": (
                        "Invalid transaction. "
                        "This API is only for existing "
                        "scheme installment payments."
                    )
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        installment = (
            SchemeInstallment.objects
            .select_for_update()
            .select_related(
                "enrollment",
                "enrollment__customer",
                "enrollment__scheme",
            )
            .get(
                installment_id=txn.installment.installment_id
            )
        )

        enrollment = installment.enrollment

        # ============================================================
        # VERIFY CUSTOMER / SCHEME
        # ============================================================

        if txn.customer_id != enrollment.customer_id:

            return Response(
                {
                    "success": False,
                    "message": "Transaction customer mismatch."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if txn.scheme_id != enrollment.scheme_id:

            return Response(
                {
                    "success": False,
                    "message": "Transaction scheme mismatch."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # ============================================================
        # VERIFY INSTALLMENT
        # ============================================================

        if installment.status == "cancelled":

            return Response(
                {
                    "success": False,
                    "message": "This installment has been cancelled."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # ============================================================
        # GET RAZORPAY PAYMENT DETAILS
        # ============================================================

        try:

            payment_details = client.payment.fetch(
                razorpay_payment_id
            )

            payment_method = payment_details.get(
                "method"
            )

            razorpay_paid_amount = Decimal(
                str(
                    payment_details.get(
                        "amount",
                        0
                    )
                )
            ) / Decimal("100")

        except Exception as e:

            return Response(
                {
                    "success": False,
                    "message": "Unable to fetch Razorpay payment details.",
                    "error": str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # ============================================================
        # VERIFY AMOUNT
        # ============================================================

        transaction_amount = Decimal(
            str(txn.amount)
        ).quantize(
            Decimal("0.01")
        )

        razorpay_paid_amount = razorpay_paid_amount.quantize(
            Decimal("0.01")
        )

        if razorpay_paid_amount != transaction_amount:

            return Response(
                {
                    "success": False,
                    "message": "Razorpay payment amount does not match transaction amount.",
                    "transaction_amount": str(
                        transaction_amount
                    ),
                    "razorpay_paid_amount": str(
                        razorpay_paid_amount
                    ),
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # ============================================================
        # CURRENT INSTALLMENT BALANCE
        # ============================================================

        installment_amount = Decimal(
            str(installment.amount)
        )

        current_paid_amount = Decimal(
            str(installment.paid_amount or 0)
        )

        remaining_before_payment = (
            installment_amount -
            current_paid_amount
        )

        # ============================================================
        # PREVENT OVER PAYMENT
        # ============================================================

        if transaction_amount > remaining_before_payment:

            return Response(
                {
                    "success": False,
                    "message": (
                        "Payment amount exceeds the remaining "
                        "installment amount."
                    ),
                    "installment_amount": str(
                        installment_amount
                    ),
                    "already_paid": str(
                        current_paid_amount
                    ),
                    "remaining_amount": str(
                        remaining_before_payment
                    ),
                    "payment_amount": str(
                        transaction_amount
                    ),
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # ============================================================
        # ADD PAYMENT TO INSTALLMENT
        # ============================================================

        new_paid_amount = (
            current_paid_amount +
            transaction_amount
        )

        new_paid_amount = new_paid_amount.quantize(
            Decimal("0.01")
        )

        # ============================================================
        # DETERMINE STATUS
        # ============================================================

        if new_paid_amount >= installment_amount:

            new_paid_amount = installment_amount

            installment.status = "paid"

        else:

            installment.status = "partial"

        installment.paid_amount = new_paid_amount

        installment.payment_mode = payment_method

        installment.transaction_reference = (
            razorpay_payment_id
        )

        installment.paid_date = (
            timezone.now().date()
        )

        installment.save(
            update_fields=[
                "paid_amount",
                "status",
                "payment_mode",
                "transaction_reference",
                "paid_date",
            ]
        )

        # ============================================================
        # UPDATE TRANSACTION
        # ============================================================

        txn.razorpay_payment_id = (
            razorpay_payment_id
        )

        txn.razorpay_signature = (
            razorpay_signature
        )

        txn.payment_method = (
            payment_method
        )

        txn.status = "success"

        txn.save(
            update_fields=[
                "razorpay_payment_id",
                "razorpay_signature",
                "payment_method",
                "status",
            ]
        )

        # ============================================================
        # CREATE RECEIPT
        # ============================================================

        receipt_number = (
            f"RCPT-{timezone.now().strftime('%Y%m%d%H%M%S')}"
            f"-{txn.transaction_id}"
        )

        receipt = SchemeReceipt.objects.create(

            installment=installment,

            receipt_number=receipt_number,

            receipt_date=timezone.now().date(),

            amount=transaction_amount,

            payment_mode=payment_method,

            transaction_reference=razorpay_payment_id,

            remarks=(
                f"Razorpay payment for "
                f"installment #{installment.installment_no}"
            )
        )

        # ============================================================
        # UPDATE ENROLLMENT SUMMARY
        # ============================================================

        total_paid_amount = (
            enrollment.installments.aggregate(
                total=Sum("paid_amount")
            )["total"]
            or Decimal("0.00")
        )

        paid_installments = (
            enrollment.installments.filter(
                status="paid"
            ).count()
        )

        total_installments = (
            enrollment.total_installments
        )

        pending_installments = (
            total_installments -
            paid_installments
        )

        enrollment.paid_installments = (
            paid_installments
        )

        enrollment.pending_installments = (
            pending_installments
        )

        enrollment.total_paid_amount = (
            total_paid_amount
        )

        # ============================================================
        # COMPLETED / ACTIVE
        # ============================================================

        if paid_installments >= total_installments:

            enrollment.status = "completed"

        else:

            enrollment.status = "active"

        enrollment.save(
            update_fields=[
                "paid_installments",
                "pending_installments",
                "total_paid_amount",
                "status",
            ]
        )

        # ============================================================
        # REMAINING INSTALLMENT AMOUNT
        # ============================================================

        remaining_after_payment = (
            installment_amount -
            new_paid_amount
        )

        # ============================================================
        # RESPONSE
        # ============================================================

        return Response(
            {
                "success": True,

                "message": (
                    "Installment payment completed successfully."
                    if installment.status == "paid"
                    else
                    "Partial installment payment completed successfully."
                ),

                "transaction": {
                    "transaction_id": (
                        txn.transaction_id
                    ),

                    "razorpay_order_id": (
                        txn.razorpay_order_id
                    ),

                    "razorpay_payment_id": (
                        txn.razorpay_payment_id
                    ),

                    "payment_method": (
                        txn.payment_method
                    ),

                    "amount": str(
                        transaction_amount
                    ),

                    "status": txn.status,
                },

                "enrollment": {
                    "enrollment_id": (
                        enrollment.enrollment_id
                    ),

                    "paid_installments": (
                        enrollment.paid_installments
                    ),

                    "pending_installments": (
                        enrollment.pending_installments
                    ),

                    "total_paid_amount": str(
                        enrollment.total_paid_amount
                    ),

                    "status": enrollment.status,
                },

                "installment": {
                    "installment_id": (
                        installment.installment_id
                    ),

                    "installment_no": (
                        installment.installment_no
                    ),

                    "installment_amount": str(
                        installment_amount
                    ),

                    "previously_paid": str(
                        current_paid_amount
                    ),

                    "payment_amount": str(
                        transaction_amount
                    ),

                    "total_paid": str(
                        new_paid_amount
                    ),

                    "remaining_amount": str(
                        remaining_after_payment
                    ),

                    "status": installment.status,
                },

                "receipt": {
                    "receipt_id": (
                        receipt.receipt_id
                    ),

                    "receipt_number": (
                        receipt.receipt_number
                    ),

                    "amount": str(
                        receipt.amount
                    ),
                },
            },
            status=status.HTTP_200_OK
        )





class SchemeEnrollmentInitiateRazorpayAPIView(APIView):

    def post(self, request):

        try:

            customer_id = request.data.get("customer_id")
            scheme_id = request.data.get("scheme_id")

            # -----------------------------------------
            # Validate customer
            # -----------------------------------------

            if not customer_id:
                return Response(
                    {
                        "status": "failed",
                        "error": "customer_id is required"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            # -----------------------------------------
            # Validate scheme
            # -----------------------------------------

            if not scheme_id:
                return Response(
                    {
                        "status": "failed",
                        "error": "scheme_id is required"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            # -----------------------------------------
            # Get customer
            # -----------------------------------------

            customer = AccountDetails.objects.filter(
                account_id=customer_id
            ).first()

            if not customer:

                return Response(
                    {
                        "status": "failed",
                        "error": "Customer not found"
                    },
                    status=status.HTTP_404_NOT_FOUND
                )

            # -----------------------------------------
            # Get scheme
            # -----------------------------------------

            scheme = Scheme.objects.filter(
                scheme_id=scheme_id
            ).first()

            if not scheme:

                return Response(
                    {
                        "status": "failed",
                        "error": "Scheme not found"
                    },
                    status=status.HTTP_404_NOT_FOUND
                )

            # -----------------------------------------
            # Validate installment amount
            # -----------------------------------------

            if (
                scheme.scheme_installment_amount is None
                or scheme.scheme_installment_amount <= 0
            ):

                return Response(
                    {
                        "status": "failed",
                        "error":
                            "This scheme does not have a valid installment amount."
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            # -----------------------------------------
            # Validate payable installments
            # -----------------------------------------

            if scheme.payable_installments <= 0:

                return Response(
                    {
                        "status": "failed",
                        "error":
                            "This scheme does not have valid payable installments."
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            # -----------------------------------------
            # Check existing active enrollment
            # -----------------------------------------

            existing_enrollment = (
                CustomerSchemeEnrollment.objects
                .filter(
                    customer=customer,
                    scheme=scheme,
                    status='active'
                )
                .first()
            )

            if existing_enrollment:

                return Response(
                    {
                        "status": "failed",
                        "error":
                            "Customer is already enrolled in this scheme.",
                        "enrollment_id":
                            existing_enrollment.enrollment_id,
                        "enrollment_number":
                            existing_enrollment.enrollment_number
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            # -----------------------------------------
            # Check pending enrollment transaction
            # -----------------------------------------

            existing_transaction = (
                SchemeTransaction.objects
                .filter(
                    customer=customer,
                    scheme=scheme,
                    enrollment__isnull=True,
                    installment__isnull=True,
                    status='pending'
                )
                .order_by('-created_at')
                .first()
            )

            if existing_transaction:

                return Response(
                    {
                        "status": "success",
                        "message":
                            "A pending payment already exists for this scheme.",

                        "key":
                            settings.RAZORPAY_KEY_ID,

                        "order_id":
                            existing_transaction.razorpay_order_id,

                        "transaction_id":
                            existing_transaction.transaction_id,

                        "amount":
                            int(
                                existing_transaction.amount * 100
                            ),

                        "currency": "INR",

                        "customer_id":
                            customer.account_id,

                        "scheme_id":
                            scheme.scheme_id,

                        "scheme_name":
                            scheme.scheme_name,

                        "first_installment_amount":
                            scheme.scheme_installment_amount
                    },
                    status=status.HTTP_200_OK
                )

            # -----------------------------------------
            # Razorpay client
            # -----------------------------------------

            client = razorpay.Client(
                auth=(
                    settings.RAZORPAY_KEY_ID,
                    settings.RAZORPAY_KEY_SECRET
                )
            )

            # -----------------------------------------
            # First installment amount
            # -----------------------------------------

            first_installment_amount = (
                scheme.scheme_installment_amount
            )

            razorpay_amount = int(
                first_installment_amount * 100
            )

            # -----------------------------------------
            # Create Razorpay order
            # -----------------------------------------

            order = client.order.create(
                {
                    "amount": razorpay_amount,
                    "currency": "INR",
                    "payment_capture": 1
                }
            )

            # -----------------------------------------
            # Create SchemeTransaction
            #
            # Enrollment = NULL
            # Installment = NULL
            # -----------------------------------------

            transaction = SchemeTransaction.objects.create(

                customer=customer,

                scheme=scheme,

                enrollment=None,

                installment=None,

                amount=first_installment_amount,

                razorpay_order_id=order["id"],

                status="pending",

                remarks="First installment payment for new scheme enrollment."
            )

            # -----------------------------------------
            # Response
            # -----------------------------------------

            return Response(
                {
                    "status": "success",

                    "message":
                        "Payment order created successfully.",

                    "key":
                        settings.RAZORPAY_KEY_ID,

                    "order_id":
                        order["id"],

                    "transaction_id":
                        transaction.transaction_id,

                    "amount":
                        razorpay_amount,

                    "currency":
                        "INR",

                    "customer_id":
                        customer.account_id,

                    "customer_name":
                        customer.account_name,

                    "scheme_id":
                        scheme.scheme_id,

                    "scheme_name":
                        scheme.scheme_name,

                    "first_installment_amount":
                        first_installment_amount,

                    "total_installments":
                        scheme.payable_installments
                },
                status=status.HTTP_200_OK
            )

        except Exception as e:

            return Response(
                {
                    "status": "failed",
                    "error": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


from django.db import transaction

class SchemeEnrollmentConfirmRazorpayAPIView(APIView):

    @transaction.atomic
    def post(self, request):

        order_id = request.data.get(
            "razorpay_order_id"
        )

        payment_id = request.data.get(
            "razorpay_payment_id"
        )

        signature = request.data.get(
            "razorpay_signature"
        )

        # -----------------------------------------
        # Validate Razorpay data
        # -----------------------------------------

        if not order_id:

            return Response(
                {
                    "status": "failed",
                    "error":
                        "razorpay_order_id is required"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if not payment_id:

            return Response(
                {
                    "status": "failed",
                    "error":
                        "razorpay_payment_id is required"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if not signature:

            return Response(
                {
                    "status": "failed",
                    "error":
                        "razorpay_signature is required"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        try:

            # -----------------------------------------
            # Razorpay client
            # -----------------------------------------

            client = razorpay.Client(
                auth=(
                    settings.RAZORPAY_KEY_ID,
                    settings.RAZORPAY_KEY_SECRET
                )
            )

            # -----------------------------------------
            # Verify Razorpay signature
            # -----------------------------------------

            client.utility.verify_payment_signature(
                {
                    "razorpay_order_id":
                        order_id,

                    "razorpay_payment_id":
                        payment_id,

                    "razorpay_signature":
                        signature
                }
            )

            # -----------------------------------------
            # Get transaction
            # -----------------------------------------

            txn = (
                SchemeTransaction.objects
                .select_for_update()
                .select_related(
                    "customer",
                    "scheme",
                    "enrollment",
                    "installment"
                )
                .get(
                    razorpay_order_id=order_id
                )
            )

            # -----------------------------------------
            # Already successful
            # -----------------------------------------

            if txn.status == "success":

                return Response(
                    {
                        "status": "success",

                        "message":
                            "Payment already verified.",

                        "transaction_id":
                            txn.transaction_id,

                        "enrollment_id":
                            txn.enrollment.enrollment_id
                            if txn.enrollment
                            else None,

                        "enrollment_number":
                            txn.enrollment.enrollment_number
                            if txn.enrollment
                            else None
                    },
                    status=status.HTTP_200_OK
                )

            # -----------------------------------------
            # Make sure this is enrollment transaction
            # -----------------------------------------

            if txn.enrollment is not None:

                return Response(
                    {
                        "status": "failed",
                        "error":
                            "This transaction is already linked to an enrollment."
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            # -----------------------------------------
            # Get payment details from Razorpay
            # -----------------------------------------

            payment_details = client.payment.fetch(
                payment_id
            )

            payment_method = payment_details.get(
                "method",
                "unknown"
            )

            # -----------------------------------------
            # Validate payment amount
            # -----------------------------------------

            razorpay_paid_amount = (
                payment_details.get("amount")
            )

            expected_amount = int(
                txn.amount * 100
            )

            if razorpay_paid_amount != expected_amount:

                txn.status = "failed"
                txn.remarks = (
                    "Payment amount mismatch. "
                    f"Expected {expected_amount} but received "
                    f"{razorpay_paid_amount}."
                )
                txn.save(
                    update_fields=[
                        "status",
                        "remarks",
                        "updated_at"
                    ]
                )

                return Response(
                    {
                        "status": "failed",
                        "error":
                            "Payment amount does not match the first installment amount."
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            # -----------------------------------------
            # Get customer and scheme
            # -----------------------------------------

            customer = txn.customer
            scheme = txn.scheme

            # -----------------------------------------
            # Double-check active enrollment
            # -----------------------------------------

            existing_enrollment = (
                CustomerSchemeEnrollment.objects
                .select_for_update()
                .filter(
                    customer=customer,
                    scheme=scheme,
                    status='active'
                )
                .first()
            )

            if existing_enrollment:

                txn.razorpay_payment_id = payment_id
                txn.razorpay_signature = signature
                txn.payment_method = payment_method
                txn.status = "success"
                txn.enrollment = existing_enrollment

                # Get first installment
                first_installment = (
                    SchemeInstallment.objects
                    .filter(
                        enrollment=existing_enrollment,
                        installment_no=1
                    )
                    .first()
                )

                txn.installment = first_installment

                txn.save()

                return Response(
                    {
                        "status": "success",

                        "message":
                            "Customer is already enrolled in this scheme.",

                        "transaction_id":
                            txn.transaction_id,

                        "enrollment_id":
                            existing_enrollment.enrollment_id,

                        "enrollment_number":
                            existing_enrollment.enrollment_number
                    },
                    status=status.HTTP_200_OK
                )

            # -----------------------------------------
            # Create Enrollment
            # -----------------------------------------

            enrollment = (
                CustomerSchemeEnrollment.objects.create(

                    customer=customer,

                    scheme=scheme,

                    enrollment_date=
                        timezone.now().date(),

                    maturity_date=(
                        timezone.now().date()
                        +
                        relativedelta(
                            months=
                                scheme.scheme_maturity_period
                        )
                    ),

                    installment_amount=
                        scheme.scheme_installment_amount,

                    total_installments=
                        scheme.payable_installments,

                    remarks=
                        "Enrollment created after successful first installment payment."
                )
            )

            # -----------------------------------------
            # Create installments
            # -----------------------------------------

            first_installment = None

            for i in range(
                1,
                scheme.payable_installments + 1
            ):

                installment = (
                    SchemeInstallment.objects.create(

                        enrollment=enrollment,

                        installment_no=i,

                        due_date=(
                            enrollment.enrollment_date
                            +
                            relativedelta(
                                months=i - 1
                            )
                        ),

                        amount=
                            scheme.scheme_installment_amount,

                        status="pending"
                    )
                )

                if i == 1:
                    first_installment = installment

            # -----------------------------------------
            # Safety check
            # -----------------------------------------

            if not first_installment:

                raise Exception(
                    "First installment could not be created."
                )

            # -----------------------------------------
            # Mark first installment as PAID
            # -----------------------------------------

            first_installment.paid_amount = txn.amount

            first_installment.paid_date = (
                timezone.now().date()
            )

            first_installment.payment_mode = (
                payment_method
            )

            first_installment.transaction_reference = (
                payment_id
            )

            first_installment.status = "paid"

            first_installment.save()

            # -----------------------------------------
            # Update transaction
            # -----------------------------------------

            txn.razorpay_payment_id = payment_id

            txn.razorpay_signature = signature

            txn.payment_method = payment_method

            txn.status = "success"

            txn.enrollment = enrollment

            txn.installment = first_installment

            txn.save()

            # -----------------------------------------
            # Generate receipt
            # -----------------------------------------

            receipt_number = (
                f"RCPT"
                f"{timezone.now().strftime('%Y%m%d%H%M%S')}"
                f"{txn.transaction_id}"
            )

            receipt = SchemeReceipt.objects.create(

                installment=first_installment,

                receipt_number=receipt_number,

                receipt_date=timezone.now().date(),

                amount=txn.amount,

                payment_mode=payment_method,

                transaction_reference=payment_id,

                remarks=
                    "First installment payment for scheme enrollment."
            )

            # -----------------------------------------
            # Final response
            # -----------------------------------------

            return Response(
                {
                    "status": "success",

                    "message":
                        "Payment verified and scheme enrollment completed successfully.",

                    "transaction_id":
                        txn.transaction_id,

                    "enrollment_id":
                        enrollment.enrollment_id,

                    "enrollment_number":
                        enrollment.enrollment_number,

                    "customer_id":
                        customer.account_id,

                    "customer_name":
                        customer.account_name,

                    "scheme_id":
                        scheme.scheme_id,

                    "scheme_name":
                        scheme.scheme_name,

                    "first_installment": {
                        "installment_id":
                            first_installment.installment_id,

                        "installment_no":
                            first_installment.installment_no,

                        "amount":
                            first_installment.amount,

                        "paid_amount":
                            first_installment.paid_amount,

                        "status":
                            first_installment.status,

                        "paid_date":
                            first_installment.paid_date
                    },

                    "receipt_no":
                        receipt.receipt_number,

                    "payment_method":
                        payment_method
                },
                status=status.HTTP_201_CREATED
            )

        except SchemeTransaction.DoesNotExist:

            return Response(
                {
                    "status": "failed",
                    "error":
                        "Scheme transaction not found."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        except Exception as e:

            return Response(
                {
                    "status": "failed",
                    "error": str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )