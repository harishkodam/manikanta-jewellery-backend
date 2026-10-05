from django.shortcuts import get_object_or_404
from django.db import transaction
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiExample

from .models import *
from .serializers import *
from .filters import *


from django.utils import timezone

import razorpay
from django.conf import settings





@method_decorator(csrf_exempt, name="dispatch")
class OpeningTagsEntryListAPIView(APIView):
    """
    Get all opening tag entries with optional filters.
    """

    def get(self, request):

        queryset = OpeningTagsEntry.objects.all()

        # Apply filters
        filterset = OpeningTagsEntryFilter(
            request.GET,
            queryset=queryset
        )

        if not filterset.is_valid():
            return Response(
                {
                    "status": False,
                    "errors": filterset.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = OpeningTagsEntrySerializer(
            filterset.qs,
            many=True
        )

        return Response(
            {
                "status": True,
                "count": filterset.qs.count(),
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )


@method_decorator(csrf_exempt, name="dispatch")
class OpeningTagsEntryRetrieveAPIView(APIView):
    """
    Get single opening tag entry by opentag_id.
    """

    def get(self, request, pk):

        product = get_object_or_404(
            OpeningTagsEntry,
            opentag_id=pk
        )

        serializer = OpeningTagsEntrySerializer(product)

        return Response(
            {
                "status": True,
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )


@method_decorator(csrf_exempt, name="dispatch")
class CustomerAddressListCreateAPIView(APIView):
    """
    List and create customer addresses.
    """

    def get(self, request):
        customer_id = request.GET.get("customer_id")
        addresses = CustomerAddress.objects.all()
        if customer_id:
            addresses = addresses.filter(customer_id=customer_id)

        serializer = CustomerAddressSerializer(addresses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(request=CustomerAddressSerializer)
    def post(self, request):
        serializer = CustomerAddressSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.validated_data.get("is_default"):
                CustomerAddress.objects.filter(
                    customer=serializer.validated_data["customer"]
                ).update(is_default=False)
            address = serializer.save()
            return Response(
                {
                    "status": "success",
                    "message": "Address created successfully.",
                    "data": CustomerAddressSerializer(address).data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name="dispatch")
class CustomerAddressRetrieveUpdateDeleteAPIView(APIView):
    def get_object(self, pk):
        try:
            return CustomerAddress.objects.get(pk=pk)
        except CustomerAddress.DoesNotExist:
            return None

    def get(self, request, pk):
        address = self.get_object(pk)
        if not address:
            return Response({"error": "Address not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CustomerAddressSerializer(address)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(request=CustomerAddressSerializer)
    def put(self, request, pk):
        address = self.get_object(pk)
        if not address:
            return Response({"error": "Address not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CustomerAddressSerializer(address, data=request.data, partial=True)
        if serializer.is_valid():
            if serializer.validated_data.get("is_default"):
                CustomerAddress.objects.filter(customer=address.customer).update(is_default=False)
            address = serializer.save()
            return Response(
                {
                    "status": "success",
                    "message": "Address updated successfully.",
                    "data": CustomerAddressSerializer(address).data,
                },
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        address = self.get_object(pk)
        if not address:
            return Response({"error": "Address not found."}, status=status.HTTP_404_NOT_FOUND)

        address.delete()
        return Response(
            {
                "status": "success",
                "message": "Address deleted successfully.",
            },
            status=status.HTTP_200_OK,
        )


@method_decorator(csrf_exempt, name="dispatch")
class WishlistListCreateAPIView(APIView):
    """
    List and create wishlist items.
    """

    def get(self, request):
        customer_id = request.GET.get("customer_id")
        wishlist = Wishlist.objects.all()
        if customer_id:
            wishlist = wishlist.filter(customer_id=customer_id)

        serializer = WishlistSerializer(wishlist, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(request=WishlistSerializer)
    def post(self, request):
        serializer = WishlistSerializer(data=request.data)
        if serializer.is_valid():
            wishlist_item = serializer.save()
            return Response(
                {
                    "status": "success",
                    "message": "Wishlist item added successfully.",
                    "data": WishlistSerializer(wishlist_item).data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name="dispatch")
class WishlistRetrieveDeleteAPIView(APIView):
    def get_object(self, pk):
        try:
            return Wishlist.objects.get(pk=pk)
        except Wishlist.DoesNotExist:
            return None

    def get(self, request, pk):
        item = self.get_object(pk)
        if not item:
            return Response({"error": "Wishlist item not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = WishlistSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        item = self.get_object(pk)
        if not item:
            return Response({"error": "Wishlist item not found."}, status=status.HTTP_404_NOT_FOUND)

        item.delete()
        return Response(
            {
                "status": "success",
                "message": "Wishlist item removed successfully.",
            },
            status=status.HTTP_200_OK,
        )

def recalculate_cart(cart):
    items = cart.items.all()
    subtotal = sum(((item.unit_price or 0) * item.quantity) for item in items)
    item_discount = sum((item.discount or 0) for item in items)
    tax_amount = sum((item.gst_amount or 0) for item in items)
    grand_total = subtotal - item_discount - (cart.discount or 0) + tax_amount + (cart.shipping_charge or 0)

    cart.subtotal = subtotal
    cart.tax_amount = tax_amount
    cart.grand_total = grand_total
    cart.save(update_fields=["subtotal", "tax_amount", "grand_total"])
    
@method_decorator(csrf_exempt, name="dispatch")
class CartAPIView(APIView):
    def get(self, request):
        cart_id = request.GET.get("cart_id")
        customer_id = request.GET.get("customer_id")

        if cart_id:
            cart = get_object_or_404(Cart, cart_id=cart_id)
            serializer = CartSerializer(cart)
            return Response(serializer.data, status=status.HTTP_200_OK)

        if customer_id:
            cart = Cart.objects.filter(customer_id=customer_id).first()
            if not cart:
                return Response({"error": "Cart not found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = CartSerializer(cart)
            return Response(serializer.data, status=status.HTTP_200_OK)

        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@method_decorator(csrf_exempt, name="dispatch")
class CartAddItemAPIView(APIView):
    def _resolve_cart(self, item_data):
        cart_id = item_data.get("cart")
        if cart_id:
            return Cart.objects.filter(cart_id=cart_id).first()

        customer = item_data.get("customer")
        if not customer:
            return None

        return Cart.objects.get_or_create(customer_id=customer, defaults={
            "subtotal": 0,
            "discount": 0,
            "tax_amount": 0,
            "shipping_charge": 0,
            "grand_total": 0,
        })[0]

    @extend_schema(request=CartItemSerializer)
    def post(self, request):
        request_data = request.data
        many = isinstance(request_data, list)
        items_data = [dict(item) for item in request_data] if many else [dict(request_data)]

        cart_ids = []
        for item_data in items_data:
            cart = self._resolve_cart(item_data)
            if not cart:
                return Response(
                    {"error": "cart or customer is required."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            item_data["cart"] = cart.cart_id
            cart_ids.append(cart.cart_id)

        serializer_data = items_data if many else items_data[0]
        serializer = CartItemSerializer(data=serializer_data, many=many)
        if serializer.is_valid():
            items = serializer.save()
            cart_ids = set(cart_ids)
            for cart_id in cart_ids:
                cart = Cart.objects.get(cart_id=cart_id)
                recalculate_cart(cart)

            return Response(
                {
                    "status": "success",
                    "message": "Cart item(s) added successfully.",
                    "data": CartItemSerializer(items, many=many).data,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name="dispatch")
class CartUpdateItemAPIView(APIView):
    @extend_schema(request=CartItemSerializer)
    def put(self, request):
        cart_item_id = request.data.get("cart_item_id")
        if not cart_item_id:
            return Response({"error": "cart_item_id is required."}, status=status.HTTP_400_BAD_REQUEST)

        item = get_object_or_404(CartItem, cart_item_id=cart_item_id)
        serializer = CartItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            item = serializer.save()
            recalculate_cart(item.cart)
            return Response(
                {
                    "status": "success",
                    "message": "Cart item updated successfully.",
                    "data": CartItemSerializer(item).data,
                },
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name="dispatch")
class CartRemoveItemAPIView(APIView):
    def delete(self, request, cart_item_id):
        item = get_object_or_404(CartItem, cart_item_id=cart_item_id)
        cart = item.cart
        item.delete()
        recalculate_cart(cart)
        return Response(
            {
                "status": "success",
                "message": "Cart item removed successfully.",
            },
            status=status.HTTP_200_OK,
        )


@method_decorator(csrf_exempt, name="dispatch")
class CartClearAPIView(APIView):
    def delete(self, request):
        cart_id = request.GET.get("cart_id")
        customer_id = request.GET.get("customer_id")

        if cart_id:
            cart = get_object_or_404(Cart, cart_id=cart_id)
        elif customer_id:
            cart = Cart.objects.filter(customer_id=customer_id).first()
            if not cart:
                return Response({"error": "Cart not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "cart_id or customer_id is required."}, status=status.HTTP_400_BAD_REQUEST)

        cart.items.all().delete()
        recalculate_cart(cart)
        return Response(
            {
                "status": "success",
                "message": "Cart cleared successfully.",
            },
            status=status.HTTP_200_OK,
        )


@method_decorator(csrf_exempt, name="dispatch")
class CheckoutAPIView_old(APIView):
    def get(self, request):
        cart_id = request.GET.get("cart_id")
        customer_id = request.GET.get("customer_id")

        if cart_id:
            cart = get_object_or_404(Cart, cart_id=cart_id)
        elif customer_id:
            cart = Cart.objects.filter(customer_id=customer_id).first()
            if not cart:
                return Response({"error": "Cart not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "cart_id or customer_id is required."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = CartSerializer(cart)
        return Response(
            {
                "status": "success",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    @extend_schema(request=CheckoutSerializer)
    def post(self, request):
        serializer = CheckoutSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        cart_id = serializer.validated_data.get("cart_id")
        customer = serializer.validated_data.get("customer")
        shipping_address = serializer.validated_data["shipping_address"]
        billing_address = serializer.validated_data["billing_address"]
        payment_method = serializer.validated_data["payment_method"]
        remarks = serializer.validated_data.get("remarks", "")

        if cart_id:
            cart = get_object_or_404(Cart, cart_id=cart_id)
        else:
            cart = Cart.objects.filter(customer=customer).first()
            if not cart:
                return Response({"error": "Cart not found."}, status=status.HTTP_404_NOT_FOUND)

        if customer and cart.customer_id != customer.pk:
            return Response({"error": "Cart does not belong to this customer."}, status=status.HTTP_400_BAD_REQUEST)

        customer = cart.customer
        if shipping_address.customer_id != customer.pk or billing_address.customer_id != customer.pk:
            return Response({"error": "Address does not belong to this customer."}, status=status.HTTP_400_BAD_REQUEST)

        if not cart.items.exists():
            return Response({"error": "Cart is empty."}, status=status.HTTP_400_BAD_REQUEST)

        recalculate_cart(cart)
        with transaction.atomic():
            order = Orders.objects.create(
                order_number=OrderSerializer.generate_order_number(),
                customer=customer,
                shipping_address=shipping_address,
                billing_address=billing_address,
                subtotal=cart.subtotal,
                discount=cart.discount,
                shipping_charge=cart.shipping_charge or 0,
                tax_amount=cart.tax_amount or 0,
                grand_total=cart.grand_total,
                payment_method=payment_method,
                payment_status="Pending",
                order_status="Pending",
                remarks=remarks,
            )

            for item in cart.items.select_related("product"):
                OrderItems.objects.create(
                    order=order,
                    product=item.product,
                    barcode=item.product.pcode_barcode,
                    huid_number=item.product.huid_no,
                    hsn_number="",
                    product_name=item.product.product_name or "",
                    category=item.product.category,
                    metal_type=item.product.metal_type,
                    purity=item.product.purity,
                    gross_weight=item.product.gross_weight or 0,
                    net_weight=item.product.weight_bw or 0,
                    stone_weight=item.product.stones_weight or 0,
                    making_charge=item.product.making_charges or 0,
                    wastage=item.product.wastageweight or 0,
                    unit_price=item.unit_price,
                    quantity=item.quantity,
                    discount=item.discount,
                    gst_percentage=item.gst_percentage,
                    gst_amount=item.gst_amount,
                    total_price=item.total_price,
                )

            sync_order_item_product_status(order, "Sold")
            cart.items.all().delete()
            recalculate_cart(cart)

        return Response(
            {
                "status": "success",
                "message": "Checkout completed successfully.",
                "order": OrderSerializer(order).data,
            },
            status=status.HTTP_201_CREATED,
        )




@method_decorator(csrf_exempt, name="dispatch")
class CheckoutAPIView(APIView):

    """
    Checkout + Razorpay Order Creation

    This API:

    1. Validates cart
    2. Validates shipping/billing address
    3. Creates Orders record
    4. Creates OrderItems
    5. Creates Razorpay order
    6. Creates PaymentTransaction

    IMPORTANT:
    - Cart is NOT cleared here.
    - Product is NOT marked Sold here.
    - Order becomes Confirmed only after payment verification.
    """

    def get(self, request):

        cart_id = request.GET.get("cart_id")
        customer_id = request.GET.get("customer_id")

        if cart_id:

            cart = get_object_or_404(
                Cart,
                cart_id=cart_id
            )

        elif customer_id:

            cart = Cart.objects.filter(
                customer_id=customer_id
            ).first()

            if not cart:

                return Response(
                    {
                        "status": False,
                        "error": "Cart not found."
                    },
                    status=status.HTTP_404_NOT_FOUND
                )

        else:

            return Response(
                {
                    "status": False,
                    "error": "cart_id or customer_id is required."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = CartSerializer(cart)

        return Response(
            {
                "status": True,
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )

    @extend_schema(
        request=CheckoutSerializer
    )
    def post(self, request):

        # --------------------------------------------------
        # 1. Validate checkout request
        # --------------------------------------------------

        serializer = CheckoutSerializer(
            data=request.data
        )

        if not serializer.is_valid():

            return Response(
                {
                    "status": False,
                    "errors": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        cart_id = serializer.validated_data.get(
            "cart_id"
        )

        customer = serializer.validated_data.get(
            "customer"
        )

        shipping_address = serializer.validated_data[
            "shipping_address"
        ]

        billing_address = serializer.validated_data[
            "billing_address"
        ]

        payment_method = serializer.validated_data[
            "payment_method"
        ]

        remarks = serializer.validated_data.get(
            "remarks",
            ""
        )

        # --------------------------------------------------
        # 2. Get cart
        # --------------------------------------------------

        if cart_id:

            cart = get_object_or_404(
                Cart,
                cart_id=cart_id
            )

        else:

            cart = Cart.objects.filter(
                customer=customer
            ).first()

            if not cart:

                return Response(
                    {
                        "status": False,
                        "error": "Cart not found."
                    },
                    status=status.HTTP_404_NOT_FOUND
                )

        # --------------------------------------------------
        # 3. Validate customer
        # --------------------------------------------------

        if customer and cart.customer_id != customer.pk:

            return Response(
                {
                    "status": False,
                    "error": "Cart does not belong to this customer."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        customer = cart.customer

        # --------------------------------------------------
        # 4. Validate addresses
        # --------------------------------------------------

        if (
            shipping_address.customer_id != customer.pk
            or
            billing_address.customer_id != customer.pk
        ):

            return Response(
                {
                    "status": False,
                    "error": "Address does not belong to this customer."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # --------------------------------------------------
        # 5. Check cart
        # --------------------------------------------------

        if not cart.items.exists():

            return Response(
                {
                    "status": False,
                    "error": "Cart is empty."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # --------------------------------------------------
        # 6. Recalculate cart
        # --------------------------------------------------

        recalculate_cart(cart)

        # --------------------------------------------------
        # 7. Only ONLINE payment uses Razorpay
        # --------------------------------------------------

        if payment_method == "Online":

            # ----------------------------------------------
            # Create Order + OrderItems
            # ----------------------------------------------

            with transaction.atomic():

                order = Orders.objects.create(

                    order_number=
                    OrderSerializer.generate_order_number(),

                    customer=customer,

                    shipping_address=shipping_address,

                    billing_address=billing_address,

                    subtotal=cart.subtotal,

                    discount=cart.discount,

                    shipping_charge=
                    cart.shipping_charge or 0,

                    tax_amount=
                    cart.tax_amount or 0,

                    grand_total=cart.grand_total,

                    payment_method="Online",

                    payment_status="Pending",

                    order_status="Pending",

                    remarks=remarks,
                )

                # ------------------------------------------
                # Create Order Items
                # ------------------------------------------

                for item in cart.items.select_related(
                    "product"
                ):

                    OrderItems.objects.create(

                        order=order,

                        product=item.product,

                        barcode=item.product.pcode_barcode,

                        huid_number=item.product.huid_no,

                        hsn_number="",

                        product_name=
                        item.product.product_name or "",

                        category=item.product.category,

                        metal_type=item.product.metal_type,

                        purity=item.product.purity,

                        gross_weight=
                        item.product.gross_weight or 0,

                        net_weight=
                        item.product.weight_bw or 0,

                        stone_weight=
                        item.product.stones_weight or 0,

                        making_charge=
                        item.product.making_charges or 0,

                        wastage=
                        item.product.wastageweight or 0,

                        unit_price=item.unit_price,

                        quantity=item.quantity,

                        discount=item.discount,

                        gst_percentage=
                        item.gst_percentage,

                        gst_amount=
                        item.gst_amount,

                        total_price=
                        item.total_price,
                    )

                # ------------------------------------------
                # Razorpay Client
                # ------------------------------------------

                client = razorpay.Client(
                    auth=(
                        settings.RAZORPAY_KEY_ID,
                        settings.RAZORPAY_KEY_SECRET
                    )
                )

                # ------------------------------------------
                # Amount must be in paise
                # ------------------------------------------

                razorpay_amount = int(
                    round(
                        float(order.grand_total) * 100
                    )
                )

                # ------------------------------------------
                # Create Razorpay Order
                # ------------------------------------------

                razorpay_order = client.order.create(
                    {
                        "amount": razorpay_amount,

                        "currency": "INR",

                        "receipt": order.order_number,

                        "notes": {
                            "order_id":
                            str(order.order_id),

                            "order_number":
                            order.order_number,

                            "customer_id":
                            str(customer.account_id),
                        }
                    }
                )

                # ------------------------------------------
                # Create PaymentTransaction
                # ------------------------------------------

                payment_transaction = (
                    PaymentTransaction.objects.create(

                        order=order,

                        customer=customer,

                        amount=order.grand_total,

                        currency="INR",

                        razorpay_order_id=
                        razorpay_order["id"],

                        status="pending",

                        gateway_response=
                        razorpay_order,
                    )
                )

            # --------------------------------------------------
            # IMPORTANT:
            #
            # Do NOT:
            #
            # cart.items.all().delete()
            #
            # Do NOT:
            #
            # sync_order_item_product_status(order, "Sold")
            #
            # Payment hasn't happened yet.
            # --------------------------------------------------

            return Response(
                {
                    "status": True,

                    "message":
                    "Order created. Proceed to Razorpay payment.",

                    "order": {
                        "order_id":
                        order.order_id,

                        "order_number":
                        order.order_number,

                        "amount":
                        str(order.grand_total),

                        "currency":
                        "INR",
                    },

                    "razorpay": {

                        "key":
                        settings.RAZORPAY_KEY_ID,

                        "razorpay_order_id":
                        razorpay_order["id"],

                        "amount":
                        razorpay_amount,

                        "currency":
                        "INR",
                    },

                    "payment_transaction_id":
                    payment_transaction.payment_transaction_id,
                },

                status=status.HTTP_201_CREATED
            )

        # --------------------------------------------------
        # 8. COD
        # --------------------------------------------------

        elif payment_method == "COD":

            with transaction.atomic():

                order = Orders.objects.create(

                    order_number=
                    OrderSerializer.generate_order_number(),

                    customer=customer,

                    shipping_address=shipping_address,

                    billing_address=billing_address,

                    subtotal=cart.subtotal,

                    discount=cart.discount,

                    shipping_charge=
                    cart.shipping_charge or 0,

                    tax_amount=
                    cart.tax_amount or 0,

                    grand_total=cart.grand_total,

                    payment_method="COD",

                    payment_status="Pending",

                    order_status="Confirmed",

                    remarks=remarks,
                )

                for item in cart.items.select_related(
                    "product"
                ):

                    OrderItems.objects.create(

                        order=order,

                        product=item.product,

                        barcode=item.product.pcode_barcode,

                        huid_number=item.product.huid_no,

                        hsn_number="",

                        product_name=
                        item.product.product_name or "",

                        category=item.product.category,

                        metal_type=item.product.metal_type,

                        purity=item.product.purity,

                        gross_weight=
                        item.product.gross_weight or 0,

                        net_weight=
                        item.product.weight_bw or 0,

                        stone_weight=
                        item.product.stones_weight or 0,

                        making_charge=
                        item.product.making_charges or 0,

                        wastage=
                        item.product.wastageweight or 0,

                        unit_price=item.unit_price,

                        quantity=item.quantity,

                        discount=item.discount,

                        gst_percentage=
                        item.gst_percentage,

                        gst_amount=
                        item.gst_amount,

                        total_price=
                        item.total_price,
                    )

                # Product is reserved/sold for COD
                sync_order_item_product_status(
                    order,
                    "Sold"
                )

                # Clear cart
                cart.items.all().delete()

                recalculate_cart(cart)

            return Response(
                {
                    "status": True,

                    "message":
                    "COD order created successfully.",

                    "order":
                    OrderSerializer(order).data,
                },

                status=status.HTTP_201_CREATED
            )

        # --------------------------------------------------
        # 9. Wallet
        # --------------------------------------------------

        elif payment_method == "Wallet":

            return Response(
                {
                    "status": False,

                    "error":
                    "Wallet payment is not implemented yet."
                },

                status=status.HTTP_400_BAD_REQUEST
            )

        # --------------------------------------------------
        # 10. Invalid payment method
        # --------------------------------------------------

        return Response(
            {
                "status": False,

                "error":
                "Invalid payment method."
            },

            status=status.HTTP_400_BAD_REQUEST
        )


@method_decorator(csrf_exempt, name="dispatch")
class VerifyPaymentAPIView_old(APIView):

    """
    Verify Razorpay payment.

    After successful verification:

    PaymentTransaction -> success
    Orders -> Paid
    Orders -> Confirmed
    Products -> Sold
    Cart -> Cleared
    """

    @extend_schema(
        request=VerifyPaymentSerializer
    )
    def post(self, request):

        serializer = VerifyPaymentSerializer(
            data=request.data
        )

        if not serializer.is_valid():

            return Response(
                {
                    "status": False,
                    "errors": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        razorpay_order_id = serializer.validated_data[
            "razorpay_order_id"
        ]

        razorpay_payment_id = serializer.validated_data[
            "razorpay_payment_id"
        ]

        razorpay_signature = serializer.validated_data[
            "razorpay_signature"
        ]

        # --------------------------------------------------
        # Find PaymentTransaction
        # --------------------------------------------------

        payment_transaction = (
            PaymentTransaction.objects
            .select_related("order", "customer")
            .filter(
                razorpay_order_id=razorpay_order_id
            )
            .first()
        )

        if not payment_transaction:

            return Response(
                {
                    "status": False,
                    "error":
                    "Payment transaction not found."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        # --------------------------------------------------
        # Prevent duplicate verification
        # --------------------------------------------------

        if payment_transaction.status == "success":

            return Response(
                {
                    "status": True,

                    "message":
                    "Payment already verified.",

                    "order_id":
                    payment_transaction.order.order_id
                },
                status=status.HTTP_200_OK
            )

        # --------------------------------------------------
        # Razorpay client
        # --------------------------------------------------

        client = razorpay.Client(
            auth=(
                settings.RAZORPAY_KEY_ID,
                settings.RAZORPAY_KEY_SECRET
            )
        )

        # --------------------------------------------------
        # Verify Signature
        # --------------------------------------------------

        try:

            client.utility.verify_payment_signature(
                {
                    "razorpay_order_id":
                    razorpay_order_id,

                    "razorpay_payment_id":
                    razorpay_payment_id,

                    "razorpay_signature":
                    razorpay_signature,
                }
            )

        except Exception as e:

            payment_transaction.status = "failed"

            payment_transaction.razorpay_payment_id = (
                razorpay_payment_id
            )

            payment_transaction.razorpay_signature = (
                razorpay_signature
            )

            payment_transaction.gateway_response = {
                "error": str(e)
            }

            payment_transaction.save()

            payment_transaction.order.payment_status = "Failed"

            payment_transaction.order.save(
                update_fields=[
                    "payment_status",
                    "updated_at"
                ]
            )

            return Response(
                {
                    "status": False,

                    "message":
                    "Payment verification failed.",

                    "error": str(e)
                },

                status=status.HTTP_400_BAD_REQUEST
            )

        # --------------------------------------------------
        # Payment verified successfully
        # --------------------------------------------------

        with transaction.atomic():

            order = payment_transaction.order

            # ----------------------------------------------
            # Update PaymentTransaction
            # ----------------------------------------------

            payment_transaction.status = "success"

            payment_transaction.razorpay_payment_id = (
                razorpay_payment_id
            )

            payment_transaction.razorpay_signature = (
                razorpay_signature
            )

            # payment_transaction.paid_at = (
            #     timezone.now()
            #     if hasattr(
            #         payment_transaction,
            #         "paid_at"
            #     )
            #     else None
            # )

            payment_transaction.save()

            # ----------------------------------------------
            # Update Order
            # ----------------------------------------------

            order.payment_status = "Paid"

            order.order_status = "Confirmed"

            order.save(
                update_fields=[
                    "payment_status",
                    "order_status",
                    "updated_at"
                ]
            )

            # ----------------------------------------------
            # Mark products Sold
            # ----------------------------------------------

            sync_order_item_product_status(
                order,
                "Sold"
            )

            # ----------------------------------------------
            # Clear customer's cart
            # ----------------------------------------------

            cart = Cart.objects.filter(
                customer=order.customer
            ).first()

            if cart:

                cart.items.all().delete()

                recalculate_cart(cart)

        return Response(
            {
                "status": True,

                "message":
                "Payment verified successfully.",

                "payment_status":
                "Paid",

                "order_status":
                "Confirmed",

                "order":
                OrderSerializer(order).data,

                "payment": {

                    "razorpay_order_id":
                    razorpay_order_id,

                    "razorpay_payment_id":
                    razorpay_payment_id,

                    "status":
                    "success",
                }
            },

            status=status.HTTP_200_OK
        )







@method_decorator(csrf_exempt, name="dispatch")
class VerifyPaymentAPIView(APIView):

    """
    Verify Razorpay payment.

    After successful verification:

    PaymentTransaction -> success
    PaymentTransaction -> payment_mode
    Orders -> Paid
    Orders -> Confirmed
    Products -> Sold
    Cart -> Cleared
    """

    @extend_schema(
        request=VerifyPaymentSerializer
    )
    def post(self, request):

        # ==================================================
        # 1. Validate request
        # ==================================================

        serializer = VerifyPaymentSerializer(
            data=request.data
        )

        if not serializer.is_valid():

            return Response(
                {
                    "status": False,
                    "errors": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        razorpay_order_id = serializer.validated_data[
            "razorpay_order_id"
        ]

        razorpay_payment_id = serializer.validated_data[
            "razorpay_payment_id"
        ]

        razorpay_signature = serializer.validated_data[
            "razorpay_signature"
        ]

        # ==================================================
        # 2. Find PaymentTransaction
        # ==================================================

        payment_transaction = (
            PaymentTransaction.objects
            .select_related("order", "customer")
            .filter(
                razorpay_order_id=razorpay_order_id
            )
            .first()
        )

        if not payment_transaction:

            return Response(
                {
                    "status": False,
                    "error":
                    "Payment transaction not found."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        # ==================================================
        # 3. Prevent duplicate verification
        # ==================================================

        if payment_transaction.status == "success":

            return Response(
                {
                    "status": True,

                    "message":
                    "Payment already verified.",

                    "order_id":
                    payment_transaction.order.order_id,

                    "payment_mode":
                    payment_transaction.payment_mode,

                    "payment": {

                        "razorpay_order_id":
                        payment_transaction.razorpay_order_id,

                        "razorpay_payment_id":
                        payment_transaction.razorpay_payment_id,

                        "status":
                        payment_transaction.status,
                    }
                },
                status=status.HTTP_200_OK
            )

        # ==================================================
        # 4. Razorpay Client
        # ==================================================

        client = razorpay.Client(
            auth=(
                settings.RAZORPAY_KEY_ID,
                settings.RAZORPAY_KEY_SECRET
            )
        )

        # ==================================================
        # 5. Verify Razorpay Signature
        # ==================================================

        try:

            client.utility.verify_payment_signature(
                {
                    "razorpay_order_id":
                    razorpay_order_id,

                    "razorpay_payment_id":
                    razorpay_payment_id,

                    "razorpay_signature":
                    razorpay_signature,
                }
            )

        except Exception as e:

            payment_transaction.status = "failed"

            payment_transaction.razorpay_payment_id = (
                razorpay_payment_id
            )

            payment_transaction.razorpay_signature = (
                razorpay_signature
            )

            payment_transaction.gateway_response = {
                "error": str(e)
            }

            payment_transaction.save(
                update_fields=[
                    "status",
                    "razorpay_payment_id",
                    "razorpay_signature",
                    "gateway_response",
                    "updated_at"
                ]
            )

            order = payment_transaction.order

            order.payment_status = "Failed"

            order.save(
                update_fields=[
                    "payment_status",
                    "updated_at"
                ]
            )

            return Response(
                {
                    "status": False,

                    "message":
                    "Payment verification failed.",

                    "error": str(e)
                },

                status=status.HTTP_400_BAD_REQUEST
            )

        # ==================================================
        # 6. Fetch Payment Details From Razorpay
        # ==================================================

        try:

            payment_details = client.payment.fetch(
                razorpay_payment_id
            )

        except Exception as e:

            return Response(
                {
                    "status": False,

                    "message":
                    "Payment verified but unable to fetch payment details.",

                    "error": str(e)
                },

                status=status.HTTP_400_BAD_REQUEST
            )

        # ==================================================
        # 7. Get Actual Razorpay Payment Mode
        # ==================================================

        razorpay_method = payment_details.get(
            "method"
        )

        # Example Razorpay values:
        #
        # upi
        # card
        # netbanking
        # wallet
        # emi

        PAYMENT_MODE_MAPPING = {

            "upi": "UPI",

            "card": "CARD",

            "netbanking": "NETBANKING",

            "wallet": "WALLET",

            "emi": "EMI",
        }

        payment_mode = PAYMENT_MODE_MAPPING.get(
            razorpay_method,
            "OTHER"
        )

        # ==================================================
        # 8. Payment must be captured
        # ==================================================

        razorpay_payment_status = payment_details.get(
            "status"
        )

        # Razorpay normally returns:
        #
        # captured
        # authorized
        # failed
        # refunded

        if razorpay_payment_status != "captured":

            payment_transaction.status = "failed"

            payment_transaction.razorpay_payment_id = (
                razorpay_payment_id
            )

            payment_transaction.razorpay_signature = (
                razorpay_signature
            )

            payment_transaction.payment_mode = (
                payment_mode
            )

            payment_transaction.gateway_response = (
                payment_details
            )

            payment_transaction.save()

            order = payment_transaction.order

            order.payment_status = "Failed"

            order.save(
                update_fields=[
                    "payment_status",
                    "updated_at"
                ]
            )

            return Response(
                {
                    "status": False,

                    "message":
                    "Payment is not captured.",

                    "payment_status":
                    razorpay_payment_status,

                    "payment_mode":
                    payment_mode,
                },

                status=status.HTTP_400_BAD_REQUEST
            )

        # ==================================================
        # 9. Payment Successfully Verified
        # ==================================================

        with transaction.atomic():

            order = payment_transaction.order

            # ----------------------------------------------
            # Update PaymentTransaction
            # ----------------------------------------------

            payment_transaction.status = "success"

            payment_transaction.payment_mode = (
                payment_mode
            )

            payment_transaction.razorpay_payment_id = (
                razorpay_payment_id
            )

            payment_transaction.razorpay_signature = (
                razorpay_signature
            )

            payment_transaction.gateway_response = (
                payment_details
            )

            payment_transaction.save()

            # ----------------------------------------------
            # Update Order
            # ----------------------------------------------

            order.payment_status = "Paid"

            order.order_status = "Confirmed"

            order.save(
                update_fields=[
                    "payment_status",
                    "order_status",
                    "updated_at"
                ]
            )

            # ----------------------------------------------
            # Mark Products Sold
            # ----------------------------------------------

            sync_order_item_product_status(
                order,
                "Sold"
            )

            # ----------------------------------------------
            # Clear Customer Cart
            # ----------------------------------------------

            cart = Cart.objects.filter(
                customer=order.customer
            ).first()

            if cart:

                cart.items.all().delete()

                recalculate_cart(cart)

        # ==================================================
        # 10. Return Response
        # ==================================================

        return Response(
            {
                "status": True,

                "message":
                "Payment verified successfully.",

                "payment_status":
                "Paid",

                "order_status":
                "Confirmed",

                "order":
                OrderSerializer(order).data,

                "payment": {

                    "razorpay_order_id":
                    razorpay_order_id,

                    "razorpay_payment_id":
                    razorpay_payment_id,

                    "payment_mode":
                    payment_mode,

                    "razorpay_method":
                    razorpay_method,

                    "razorpay_status":
                    razorpay_payment_status,

                    "status":
                    "success",
                }
            },

            status=status.HTTP_200_OK
        )




@method_decorator(csrf_exempt, name="dispatch")
class OrderCancelAPIView(APIView):
    def post(self, request, pk):
        order = get_object_or_404(Orders, pk=pk)
        order.order_status = "Cancelled"
        order.cancelled_at = timezone.now()
        order.save(update_fields=["order_status", "cancelled_at", "updated_at"])
        sync_order_item_product_status(order, "Available")
        return Response(
            {
                "status": "success",
                "message": "Order cancelled successfully.",
                "order": OrderSerializer(order).data,
            },
            status=status.HTTP_200_OK,
        )


@method_decorator(csrf_exempt, name="dispatch")
class OrderReturnAPIView(APIView):
    def post(self, request, pk):
        order = get_object_or_404(Orders, pk=pk)
        order.order_status = "Returned"
        order.save(update_fields=["order_status", "updated_at"])
        sync_order_item_product_status(order, "Available")
        return Response(
            {
                "status": "success",
                "message": "Order returned successfully.",
                "order": OrderSerializer(order).data,
            },
            status=status.HTTP_200_OK,
        )


@method_decorator(csrf_exempt, name="dispatch")
class OrderInvoiceAPIView(APIView):
    def get(self, request, pk):
        order = get_object_or_404(Orders, pk=pk)
        order_data = OrderSerializer(order).data
        return Response(
            {
                "status": "success",
                "invoice": order_data,
            },
            status=status.HTTP_200_OK,
        )


@method_decorator(csrf_exempt, name="dispatch")
class OrderTrackingAPIView(APIView):
    def get(self, request, pk):
        order = get_object_or_404(Orders, pk=pk)
        tracking = OrderTracking.objects.filter(order=order).order_by("created_at")
        serializer = OrderTrackingSerializer(tracking, many=True)
        return Response(
            {
                "status": "success",
                "tracking": serializer.data,
            },
            status=status.HTTP_200_OK,
        )


@method_decorator(csrf_exempt, name="dispatch")
class CartRetrieveUpdateDeleteAPIView(APIView):
    def get_object(self, pk):
        try:
            return Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            return None

    def get(self, request, pk):
        cart = self.get_object(pk)
        if not cart:
            return Response({"error": "Cart not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(request=CartSerializer)
    def put(self, request, pk):
        cart = self.get_object(pk)
        if not cart:
            return Response({"error": "Cart not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CartSerializer(cart, data=request.data, partial=True)
        if serializer.is_valid():
            cart = serializer.save()
            recalculate_cart(cart)
            return Response(
                {
                    "status": "success",
                    "message": "Cart updated successfully.",
                    "data": CartSerializer(cart).data,
                },
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        cart = self.get_object(pk)
        if not cart:
            return Response({"error": "Cart not found."}, status=status.HTTP_404_NOT_FOUND)

        cart.delete()
        return Response(
            {
                "status": "success",
                "message": "Cart deleted successfully.",
            },
            status=status.HTTP_200_OK,
        )


@method_decorator(csrf_exempt, name="dispatch")
class CartItemListCreateAPIView(APIView):
    def get(self, request):
        cart_id = request.GET.get("cart_id")
        customer_id = request.GET.get("customer_id")
        items = CartItem.objects.all()

        if cart_id:
            items = items.filter(cart_id=cart_id)
        elif customer_id:
            items = items.filter(cart__customer_id=customer_id)

        serializer = CartItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(request=CartItemSerializer)
    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            item = serializer.save()
            recalculate_cart(item.cart)
            return Response(
                {
                    "status": "success",
                    "message": "Cart item added successfully.",
                    "data": CartItemSerializer(item).data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name="dispatch")
class CartItemRetrieveUpdateDeleteAPIView(APIView):
    def get_object(self, pk):
        try:
            return CartItem.objects.get(pk=pk)
        except CartItem.DoesNotExist:
            return None

    def get(self, request, pk):
        item = self.get_object(pk)
        if not item:
            return Response({"error": "Cart item not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CartItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(request=CartItemSerializer)
    def put(self, request, pk):
        item = self.get_object(pk)
        if not item:
            return Response({"error": "Cart item not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CartItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            item = serializer.save()
            recalculate_cart(item.cart)
            return Response(
                {
                    "status": "success",
                    "message": "Cart item updated successfully.",
                    "data": CartItemSerializer(item).data,
                },
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        item = self.get_object(pk)
        if not item:
            return Response({"error": "Cart item not found."}, status=status.HTTP_404_NOT_FOUND)

        cart = item.cart
        item.delete()
        recalculate_cart(cart)
        return Response(
            {
                "status": "success",
                "message": "Cart item deleted successfully.",
            },
            status=status.HTTP_200_OK,
        )


@method_decorator(csrf_exempt, name="dispatch")
class OrderListCreateAPIView(APIView):
    def get(self, request):
        customer_id = request.GET.get("customer_id")
        order_status = request.GET.get("order_status")

        orders = Orders.objects.all()
        if customer_id:
            orders = orders.filter(customer_id=customer_id)
        if order_status:
            orders = orders.filter(order_status=order_status)

        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(request=OrderSerializer)
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            return Response(
                {
                    "status": "success",
                    "message": "Order created successfully.",
                    "data": OrderSerializer(order).data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name="dispatch")
class OrderRetrieveUpdateDeleteAPIView(APIView):
    def get_object(self, pk):
        try:
            return Orders.objects.get(pk=pk)
        except Orders.DoesNotExist:
            return None

    def get(self, request, pk):
        order = self.get_object(pk)
        if not order:
            return Response({"error": "Order not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(request=OrderSerializer)
    def put(self, request, pk):
        order = self.get_object(pk)
        if not order:
            return Response({"error": "Order not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            order = serializer.save()
            if order.order_status in {"Cancelled", "Returned"}:
                sync_order_item_product_status(order, "Available")
            else:
                sync_order_item_product_status(order, "Sold")
            return Response(
                {
                    "status": "success",
                    "message": "Order updated successfully.",
                    "data": OrderSerializer(order).data,
                },
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        order = self.get_object(pk)
        if not order:
            return Response({"error": "Order not found."}, status=status.HTTP_404_NOT_FOUND)

        order.delete()
        return Response(
            {
                "status": "success",
                "message": "Order deleted successfully.",
            },
            status=status.HTTP_200_OK,
        )

class CurrentRatesAPIView(APIView):

    def get(self, request):

        rates = CurrentRates.objects.all().order_by("-rate_date", "-rate_time")

        serializer = CurrentRatesSerializer(
            rates,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )









from decimal import Decimal

from django.db.models import Sum, Count
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import PaymentTransaction












from decimal import Decimal

from django.db.models import Sum

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django_filters.rest_framework import DjangoFilterBackend

from .models import PaymentTransaction
from .filters import PaymentTransactionFilter


class PaymentTransactionListAPIView(APIView):

    def get(self, request):

        # =====================================================
        # BASE QUERYSET
        # =====================================================

        queryset = PaymentTransaction.objects.select_related(
            "order",
            "customer"
        ).all()

        # =====================================================
        # APPLY FILTER
        # =====================================================

        transaction_filter = PaymentTransactionFilter(
            request.GET,
            queryset=queryset
        )

        transactions = transaction_filter.qs

        # =====================================================
        # SUMMARY
        # =====================================================

        total_transactions = transactions.count()

        total_amount = transactions.aggregate(
            total=Sum("amount")
        )["total"] or Decimal("0.00")

        # =====================================================
        # STATUS SUMMARY
        # =====================================================

        successful_transactions = transactions.filter(
            status="success"
        ).count()

        pending_transactions = transactions.filter(
            status="pending"
        ).count()

        failed_transactions = transactions.filter(
            status="failed"
        ).count()

        refunded_transactions = transactions.filter(
            status="refunded"
        ).count()

        # =====================================================
        # PAYMENT METHOD SUMMARY
        # =====================================================

        online_transactions = transactions.filter(
            order__payment_method="Online"
        ).count()

        cod_transactions = transactions.filter(
            order__payment_method="COD"
        ).count()

        wallet_transactions = transactions.filter(
            order__payment_method="Wallet"
        ).count()

        # =====================================================
        # PAYMENT MODE SUMMARY
        # =====================================================

        upi_transactions = transactions.filter(
            payment_mode__iexact="UPI"
        ).count()

        card_transactions = transactions.filter(
            payment_mode__iexact="Card"
        ).count()

        netbanking_transactions = transactions.filter(
            payment_mode__iexact="NetBanking"
        ).count()

        # =====================================================
        # TRANSACTION DATA
        # =====================================================

        transaction_data = []

        for transaction in transactions.order_by("-created_at"):

            transaction_data.append({

                "payment_transaction_id":
                    transaction.payment_transaction_id,

                "order_id":
                    transaction.order.order_id,

                "order_number":
                    transaction.order.order_number,

                "customer_id":
                    transaction.customer_id,

                "amount":
                    str(transaction.amount),

                "currency":
                    transaction.currency,

                # Payment Method
                # From Orders
                "payment_method":
                    transaction.order.payment_method,

                # Payment Mode
                # From PaymentTransaction
                "payment_mode":
                    transaction.payment_mode,

                # Order payment status
                "payment_status":
                    transaction.order.payment_status,

                # Gateway transaction status
                "transaction_status":
                    transaction.status,

                "razorpay_order_id":
                    transaction.razorpay_order_id,

                "razorpay_payment_id":
                    transaction.razorpay_payment_id,

                "gateway_response":
                    transaction.gateway_response,

                "created_at":
                    transaction.created_at,

                "updated_at":
                    transaction.updated_at,
            })

        # =====================================================
        # RESPONSE
        # =====================================================

        return Response(
            {
                "success": True,

                "message":
                    "Payment transactions fetched successfully.",

                "summary": {

                    "total_transactions":
                        total_transactions,

                    "total_amount":
                        str(total_amount),

                    "transaction_status": {

                        "success":
                            successful_transactions,

                        "pending":
                            pending_transactions,

                        "failed":
                            failed_transactions,

                        "refunded":
                            refunded_transactions,
                    },

                    "payment_method": {

                        "online":
                            online_transactions,

                        "cod":
                            cod_transactions,

                        "wallet":
                            wallet_transactions,
                    },

                    "payment_mode": {

                        "upi":
                            upi_transactions,

                        "card":
                            card_transactions,

                        "netbanking":
                            netbanking_transactions,
                    },
                },

                "data":
                    transaction_data,
            },
            status=status.HTTP_200_OK
        )













class PaymentTransactionListAPIView_old(APIView):
    """
    GET API for Payment Transactions

    Supported filters:

    ?status=success
    ?payment_method=Online
    ?payment_mode=UPI
    ?order_id=10
    ?customer_id=5
    ?razorpay_order_id=order_xxx
    ?razorpay_payment_id=pay_xxx
    ?date_from=2026-08-01
    ?date_to=2026-08-20
    ?amount_min=1000
    ?amount_max=50000

    Multiple filters can be combined.
    """

    def get(self, request):

        # =====================================================
        # BASE QUERYSET
        # =====================================================

        transactions = PaymentTransaction.objects.select_related(
            "order",
            "customer"
        ).all()

        # =====================================================
        # STATUS FILTER
        # =====================================================

        transaction_status = request.query_params.get("status")

        if transaction_status:
            transactions = transactions.filter(
                status__iexact=transaction_status
            )

        # =====================================================
        # PAYMENT METHOD FILTER
        # From Orders table
        #
        # Online / COD / Wallet
        # =====================================================

        payment_method = request.query_params.get(
            "payment_method"
        )

        if payment_method:
            transactions = transactions.filter(
                order__payment_method__iexact=payment_method
            )

        # =====================================================
        # PAYMENT MODE FILTER
        # From PaymentTransaction table
        #
        # UPI / Card / NetBanking / etc.
        # =====================================================

        payment_mode = request.query_params.get(
            "payment_mode"
        )

        if payment_mode:
            transactions = transactions.filter(
                payment_mode__iexact=payment_mode
            )

        # =====================================================
        # ORDER ID FILTER
        # =====================================================

        order_id = request.query_params.get("order_id")

        if order_id:
            transactions = transactions.filter(
                order_id=order_id
            )

        # =====================================================
        # CUSTOMER ID FILTER
        # =====================================================

        customer_id = request.query_params.get("customer_id")

        if customer_id:
            transactions = transactions.filter(
                customer_id=customer_id
            )

        # =====================================================
        # RAZORPAY ORDER ID FILTER
        # =====================================================

        razorpay_order_id = request.query_params.get(
            "razorpay_order_id"
        )

        if razorpay_order_id:
            transactions = transactions.filter(
                razorpay_order_id=razorpay_order_id
            )

        # =====================================================
        # RAZORPAY PAYMENT ID FILTER
        # =====================================================

        razorpay_payment_id = request.query_params.get(
            "razorpay_payment_id"
        )

        if razorpay_payment_id:
            transactions = transactions.filter(
                razorpay_payment_id=razorpay_payment_id
            )

        # =====================================================
        # DATE FROM FILTER
        # =====================================================

        date_from = request.query_params.get("date_from")

        if date_from:
            transactions = transactions.filter(
                created_at__date__gte=date_from
            )

        # =====================================================
        # DATE TO FILTER
        # =====================================================

        date_to = request.query_params.get("date_to")

        if date_to:
            transactions = transactions.filter(
                created_at__date__lte=date_to
            )

        # =====================================================
        # MINIMUM AMOUNT FILTER
        # =====================================================

        amount_min = request.query_params.get("amount_min")

        if amount_min:
            transactions = transactions.filter(
                amount__gte=amount_min
            )

        # =====================================================
        # MAXIMUM AMOUNT FILTER
        # =====================================================

        amount_max = request.query_params.get("amount_max")

        if amount_max:
            transactions = transactions.filter(
                amount__lte=amount_max
            )

        # =====================================================
        # SUMMARY
        # =====================================================

        total_transactions = transactions.count()

        total_amount = transactions.aggregate(
            total=Sum("amount")
        )["total"] or Decimal("0.00")

        # =====================================================
        # STATUS SUMMARY
        # =====================================================

        successful_transactions = transactions.filter(
            status="success"
        ).count()

        pending_transactions = transactions.filter(
            status="pending"
        ).count()

        failed_transactions = transactions.filter(
            status="failed"
        ).count()

        refunded_transactions = transactions.filter(
            status="refunded"
        ).count()

        # =====================================================
        # PAYMENT METHOD SUMMARY
        # =====================================================

        online_transactions = transactions.filter(
            order__payment_method="Online"
        ).count()

        cod_transactions = transactions.filter(
            order__payment_method="COD"
        ).count()

        wallet_method_transactions = transactions.filter(
            order__payment_method="Wallet"
        ).count()

        # =====================================================
        # PAYMENT MODE SUMMARY
        # =====================================================

        upi_transactions = transactions.filter(
            payment_mode__iexact="UPI"
        ).count()

        card_transactions = transactions.filter(
            payment_mode__iexact="Card"
        ).count()

        netbanking_transactions = transactions.filter(
            payment_mode__iexact="NetBanking"
        ).count()

        # =====================================================
        # TRANSACTION DATA
        # =====================================================

        transaction_data = []

        for transaction in transactions.order_by("-created_at"):

            transaction_data.append({

                "payment_transaction_id":
                    transaction.payment_transaction_id,

                # -------------------------------------------------
                # Order
                # -------------------------------------------------

                "order_id":
                    transaction.order.order_id,

                "order_number":
                    transaction.order.order_number,

                # -------------------------------------------------
                # Customer
                # -------------------------------------------------

                "customer_id":
                    transaction.customer_id,

                # -------------------------------------------------
                # Amount
                # -------------------------------------------------

                "amount":
                    str(transaction.amount),

                "currency":
                    transaction.currency,

                # -------------------------------------------------
                # Payment
                # -------------------------------------------------

                "payment_method":
                    transaction.order.payment_method,

                "payment_mode":
                    transaction.payment_mode,

                "payment_status":
                    transaction.order.payment_status,

                "transaction_status":
                    transaction.status,

                # -------------------------------------------------
                # Razorpay
                # -------------------------------------------------

                "razorpay_order_id":
                    transaction.razorpay_order_id,

                "razorpay_payment_id":
                    transaction.razorpay_payment_id,

                # -------------------------------------------------
                # Gateway Response
                # -------------------------------------------------

                "gateway_response":
                    transaction.gateway_response,

                # -------------------------------------------------
                # Dates
                # -------------------------------------------------

                "created_at":
                    transaction.created_at,

                "updated_at":
                    transaction.updated_at,
            })

        # =====================================================
        # RESPONSE
        # =====================================================

        return Response(
            {
                "success": True,

                "message":
                    "Payment transactions fetched successfully.",

                # =================================================
                # SUMMARY
                # =================================================

                "summary": {

                    "total_transactions":
                        total_transactions,

                    "total_amount":
                        str(total_amount),

                    # ---------------------------------------------
                    # Transaction Status
                    # ---------------------------------------------

                    "successful_transactions":
                        successful_transactions,

                    "pending_transactions":
                        pending_transactions,

                    "failed_transactions":
                        failed_transactions,

                    "refunded_transactions":
                        refunded_transactions,

                    # ---------------------------------------------
                    # Payment Method
                    # ---------------------------------------------

                    "payment_method": {

                        "online":
                            online_transactions,

                        "cod":
                            cod_transactions,

                        "wallet":
                            wallet_method_transactions,
                    },

                    # ---------------------------------------------
                    # Payment Mode
                    # ---------------------------------------------

                    "payment_mode": {

                        "upi":
                            upi_transactions,

                        "card":
                            card_transactions,

                        "netbanking":
                            netbanking_transactions,
                    },
                },

                # =================================================
                # APPLIED FILTERS
                # =================================================

                "filters": {

                    "status":
                        transaction_status,

                    "payment_method":
                        payment_method,

                    "payment_mode":
                        payment_mode,

                    "order_id":
                        order_id,

                    "customer_id":
                        customer_id,

                    "razorpay_order_id":
                        razorpay_order_id,

                    "razorpay_payment_id":
                        razorpay_payment_id,

                    "date_from":
                        date_from,

                    "date_to":
                        date_to,

                    "amount_min":
                        amount_min,

                    "amount_max":
                        amount_max,
                },

                # =================================================
                # TRANSACTIONS
                # =================================================

                "data":
                    transaction_data,
            },
            status=status.HTTP_200_OK
        )







from datetime import timedelta
from decimal import Decimal

from dateutil.relativedelta import relativedelta

from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Rates


class RatesChartAPIView(APIView):
    """
    Gold / Silver Rate Chart API

    Supported periods:
        1W  - Last 7 days
        1M  - Last 1 month
        6M  - Last 6 months
        1Y  - Last 1 year
        ALL - All available records

    Supported carats:
        9K
        16K
        18K
        22K
        24K
        SILVER
    """

    # ==========================================================
    # CARAT -> MODEL FIELD
    # ==========================================================

    CARAT_FIELD_MAP = {
        "9K": "rate_9crt",
        "16K": "rate_16crt",
        "18K": "rate_18crt",
        "22K": "rate_22crt",
        "24K": "rate_24crt",
        "SILVER": "silver_rate",
    }

    # ==========================================================
    # CARAT DISPLAY NAMES
    # ==========================================================

    CARAT_DISPLAY_MAP = {
        "9K": "9 Carat",
        "16K": "16 Carat",
        "18K": "18 Carat",
        "22K": "22 Carat (916)",
        "24K": "24 Carat (999)",
        "SILVER": "Silver",
    }

    # ==========================================================
    # GET
    # ==========================================================

    def get(self, request):

        # ------------------------------------------------------
        # GET PARAMETERS
        # ------------------------------------------------------

        period = request.query_params.get(
            "period",
            "1W"
        ).upper().strip()

        carat = request.query_params.get(
            "carat",
            "22K"
        ).upper().strip()

        # ------------------------------------------------------
        # VALIDATION
        # ------------------------------------------------------

        valid_periods = [
            "1W",
            "1M",
            "6M",
            "1Y",
            "ALL",
        ]

        valid_carats = list(
            self.CARAT_FIELD_MAP.keys()
        )

        # ------------------------------------------------------
        # INVALID PERIOD
        # ------------------------------------------------------

        if period not in valid_periods:

            return Response(
                {
                    "success": False,
                    "message": "Invalid period.",
                    "allowed_periods": valid_periods,
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # ------------------------------------------------------
        # INVALID CARAT
        # ------------------------------------------------------

        if carat not in valid_carats:

            return Response(
                {
                    "success": False,
                    "message": "Invalid carat.",
                    "allowed_carats": valid_carats,
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # ------------------------------------------------------
        # SELECT DATABASE FIELD
        # ------------------------------------------------------

        rate_field = self.CARAT_FIELD_MAP[carat]

        carat_name = self.CARAT_DISPLAY_MAP[carat]

        # ------------------------------------------------------
        # CURRENT DATE
        # ------------------------------------------------------

        today = timezone.localdate()

        # ------------------------------------------------------
        # CALCULATE START DATE
        # ------------------------------------------------------

        if period == "1W":

            start_date = today - timedelta(days=7)

        elif period == "1M":

            start_date = today - relativedelta(months=1)

        elif period == "6M":

            start_date = today - relativedelta(months=6)

        elif period == "1Y":

            start_date = today - relativedelta(years=1)

        else:

            start_date = None

        # ------------------------------------------------------
        # QUERYSET
        # ------------------------------------------------------

        queryset = Rates.objects.all()

        if start_date:

            queryset = queryset.filter(
                rate_date__gte=start_date,
                rate_date__lte=today
            )

        # ------------------------------------------------------
        # ORDER BY DATE + TIME
        # ------------------------------------------------------

        queryset = queryset.order_by(
            "rate_date",
            "rate_time",
            "rates_id"
        )

        # ------------------------------------------------------
        # BUILD CHART DATA
        # ------------------------------------------------------

        chart_data = []

        previous_rate = None

        for rate in queryset:

            current_rate = getattr(
                rate,
                rate_field
            )

            # ----------------------------------------------
            # Skip records where selected rate is NULL
            # ----------------------------------------------

            if current_rate is None:
                continue

            current_rate = Decimal(
                str(current_rate)
            )

            # ----------------------------------------------
            # Calculate change
            # ----------------------------------------------

            if previous_rate is None:

                change = Decimal("0.00")

                change_type = "no_change"

                change_percentage = Decimal("0.00")

            else:

                change = (
                    current_rate - previous_rate
                ).quantize(
                    Decimal("0.01")
                )

                if change > 0:

                    change_type = "increase"

                elif change < 0:

                    change_type = "decrease"

                else:

                    change_type = "no_change"

                # ------------------------------------------
                # Percentage change
                # ------------------------------------------

                if previous_rate != 0:

                    change_percentage = (
                        change / previous_rate * 100
                    ).quantize(
                        Decimal("0.01")
                    )

                else:

                    change_percentage = Decimal("0.00")

            # ----------------------------------------------
            # Add chart record
            # ----------------------------------------------

            chart_data.append(
                {
                    "rates_id": rate.rates_id,

                    "date": rate.rate_date.strftime(
                        "%Y-%m-%d"
                    ),

                    "time": rate.rate_time.strftime(
                        "%H:%M:%S"
                    ),

                    "rate": current_rate,

                    "previous_rate": previous_rate,

                    "change": change,

                    "change_percentage": change_percentage,

                    "change_type": change_type,
                }
            )

            # ----------------------------------------------
            # Update previous rate
            # ----------------------------------------------

            previous_rate = current_rate

        # ------------------------------------------------------
        # CURRENT / LATEST RATE
        # ------------------------------------------------------

        latest_rate = None

        if chart_data:

            latest_rate = chart_data[-1]["rate"]

        # ------------------------------------------------------
        # RESPONSE
        # ------------------------------------------------------

        return Response(
            {
                "success": True,

                "message": "Rates fetched successfully.",

                "period": period,

                "carat": carat,

                "carat_name": carat_name,

                "rate_field": rate_field,

                "start_date": start_date,

                "end_date": today,

                "latest_rate": latest_rate,

                "total_records": len(chart_data),

                "data": chart_data,
            },
            status=status.HTTP_200_OK
        )