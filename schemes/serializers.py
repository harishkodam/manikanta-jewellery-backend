from django.utils import timezone
from rest_framework import serializers
from .models import *
from erp.models import Users, AccountDetails


class LoginSerializer(serializers.Serializer):
    """
    Serializer for user login.
    Accepts email or phone_number and password.
    """
    identifier = serializers.CharField(help_text="Email or Phone Number")
    password = serializers.CharField(write_only=True, help_text="User password")


class LogoutSerializer(serializers.Serializer):
    """
    Serializer for user logout.
    Requires user ID.
    """
    user_id = serializers.IntegerField(help_text="User ID to logout")


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.
    Handles user creation, update, and retrieval.
    Password is write-only for security.
    """

    class Meta:
        model = Users
        fields = '__all__'
        read_only_fields = ['id']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        """
        Create a new user instance.
        Password is hashed automatically by the model's save method.
        """
        user = Users.objects.create(**validated_data)
        return user

    def update(self, instance, validated_data):
        """
        Update user instance.
        Only password is re-hashed if provided.
        """
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountDetails
        fields = "__all__"
        read_only_fields = ("account_id",)
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def validate(self, attrs):
        instance = getattr(self, "instance", None)

        email = attrs.get("email")
        mobile = attrs.get("mobile") or attrs.get("phone")
        aadhaar = attrs.get("aadhar_card")
        pan = attrs.get("pan_card")

        queryset = AccountDetails.objects.all()

        if instance:
            queryset = queryset.exclude(account_id=instance.account_id)

        if email and queryset.filter(email=email).exists():
            raise serializers.ValidationError(
                {"email": "This email already exists."}
            )

        if mobile and queryset.filter(mobile=mobile).exists():
            raise serializers.ValidationError(
                {"mobile": "This mobile number already exists."}
            )

        if aadhaar and queryset.filter(aadhar_card=aadhaar).exists():
            raise serializers.ValidationError(
                {"aadhar_card": "This Aadhaar number already exists."}
            )

        if pan and queryset.filter(pan_card=pan).exists():
            raise serializers.ValidationError(
                {"pan_card": "This PAN number already exists."}
            )

        return attrs

    def to_internal_value(self, data):
        # Coerce empty-string values for numeric/integer/decimal fields to None
        data = data.copy()
        for key in ("op_bal", "metal_balance", "verified_by", "dr_cr"):
            if key in data and (data.get(key) == "" or data.get(key) == "."):
                data[key] = None

        # Ensure mobile falls back to phone if provided
        if data.get("phone") and not data.get("mobile"):
            data["mobile"] = data.get("phone")

        return super().to_internal_value(data)

    def validate_dr_cr(self, value):
        """Validate `dr_cr` field to avoid invalid values reaching the DB.

        Accepts None or empty values (converted to None) or one of 'DR'/'CR' (case-insensitive).
        Any other value raises a `ValidationError` so the API returns HTTP 400 instead of a DB 500.
        """
        if value is None:
            return None

        # Normalize and allow empty strings to become None
        v = str(value).strip()
        if v == "":
            return None

        v_upper = v.upper()
        if v_upper not in ("DR", "CR"):
            raise serializers.ValidationError("dr_cr must be one of 'DR', 'CR', or null.")

        return v_upper

    def create(self, validated_data):
        validated_data.setdefault("created_at", timezone.now())

        if validated_data.get("phone") and not validated_data.get("mobile"):
            validated_data["mobile"] = validated_data["phone"]

        return AccountDetails.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if validated_data.get("phone") and not validated_data.get("mobile"):
            validated_data["mobile"] = validated_data["phone"]

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


class CustomerLoginSerializer(serializers.Serializer):
    """
    Serializer for customer login.
    Accepts email or phone number and password.
    """

    identifier = serializers.CharField(
        help_text="Email or Phone Number"
    )

    password = serializers.CharField(
        write_only=True,
        help_text="Customer Password"
    )



class CustomerLogoutSerializer(serializers.Serializer):
    """
    Serializer for customer logout.
    """

    customer_id = serializers.IntegerField(
        help_text="Customer ID to logout"
    )





class SchemeSerializer(serializers.ModelSerializer):

    created_by_name = serializers.CharField(
        source='created_by.full_name',
        read_only=True,
        allow_null=True
    )

    updated_by_name = serializers.CharField(
        source='updated_by.full_name',
        read_only=True,
        allow_null=True
    )

    scheme_benefit_display = serializers.CharField(
        source='get_scheme_benefit_display',
        read_only=True
    )

    class Meta:
        model = Scheme
        fields = '__all__'

        read_only_fields = [
            'scheme_id',
            'payable_installments',
            'created_at',
            'created_by',
            'updated_at',
            'updated_by'
        ]

    def validate(self, attrs):

        scheme_benefit = attrs.get(
            'scheme_benefit',
            getattr(self.instance, 'scheme_benefit', None)
        )

        x_value = attrs.get(
            'x_value',
            getattr(self.instance, 'x_value', None)
        )

        y_value = attrs.get(
            'y_value',
            getattr(self.instance, 'y_value', None)
        )

        maturity_period = attrs.get(
            'scheme_maturity_period',
            getattr(self.instance, 'scheme_maturity_period', None)
        )

        if scheme_benefit == 'x_plus_y':

            if not x_value:
                raise serializers.ValidationError({
                    'x_value': 'X value is required for X+Y scheme.'
                })

            if not y_value:
                raise serializers.ValidationError({
                    'y_value': 'Y value is required for X+Y scheme.'
                })

        else:
            attrs['x_value'] = None
            attrs['y_value'] = None

        if maturity_period and maturity_period <= 0:
            raise serializers.ValidationError({
                'scheme_maturity_period':
                'Maturity period must be greater than zero.'
            })

        return attrs
    


class CustomerSchemeEnrollmentSerializer(serializers.ModelSerializer):

    customer_name = serializers.CharField(
        source='customer.account_name',
        read_only=True
    )

    scheme_name = serializers.CharField(
        source='scheme.scheme_name',
        read_only=True
    )

    class Meta:
        model = CustomerSchemeEnrollment

        fields = '__all__'

        read_only_fields = (
            'enrollment_id',
            'enrollment_number',
            'enrollment_date',
            'maturity_date',
            'installment_amount',
            'total_installments',
            'paid_installments',
            'pending_installments',
            'total_paid_amount',
            'created_at',
            'updated_at'
        )


class SchemeInstallmentSerializer(serializers.ModelSerializer):

    enrollment_number = serializers.CharField(
        source='enrollment.enrollment_number',
        read_only=True
    )

    customer_name = serializers.CharField(
        source='enrollment.customer.account_name',
        read_only=True
    )

    scheme_name = serializers.CharField(
        source='enrollment.scheme.scheme_name',
        read_only=True
    )

    class Meta:
        model = SchemeInstallment
        fields = '__all__'


class PayInstallmentRequestSerializer(serializers.Serializer):

    paid_amount = serializers.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    payment_mode = serializers.CharField(
        max_length=20
    )

    receipt_number = serializers.CharField(
        max_length=50
    )

    transaction_reference = serializers.CharField(
        max_length=100,
        required=False,
        allow_blank=True
    )

class PayInstallmentSerializer(serializers.ModelSerializer):

    enrollment_number = serializers.CharField(
        source='enrollment.enrollment_number',
        read_only=True
    )

    customer_name = serializers.CharField(
        source='enrollment.customer.account_name',
        read_only=True
    )

    class Meta:
        model = SchemeInstallment
        fields = (
            'installment_id',
            'installment_no',
            'enrollment_number',
            'customer_name',
            'amount',
            'paid_amount',
            'paid_date',
            'receipt_number',
            'payment_mode',
            'transaction_reference',
            'status'
        )



class CustomerSchemeSerializer(serializers.ModelSerializer):

    scheme_name = serializers.CharField(
        source='scheme.scheme_name',
        read_only=True
    )

    scheme_benefit = serializers.CharField(
        source='scheme.scheme_benefit',
        read_only=True
    )

    class Meta:
        model = CustomerSchemeEnrollment

        fields = '__all__'


class CustomerSchemeDetailSerializer(serializers.ModelSerializer):

    customer_name = serializers.CharField(
        source='customer.account_name',
        read_only=True
    )

    scheme_name = serializers.CharField(
        source='scheme.scheme_name',
        read_only=True
    )

    scheme_benefit = serializers.CharField(
        source='scheme.scheme_benefit',
        read_only=True
    )

    progress = serializers.SerializerMethodField()

    class Meta:
        model = CustomerSchemeEnrollment
        fields = '__all__'

    def get_progress(self, obj):
        return f"{obj.paid_installments}/{obj.total_installments}"
    

    
class CustomerSchemeInstallmentSerializer(serializers.ModelSerializer):

    can_pay = serializers.SerializerMethodField()

    class Meta:
        model = SchemeInstallment
        fields = '__all__'

    def get_can_pay(self, obj):

        return obj.status == 'pending'