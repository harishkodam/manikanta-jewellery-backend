from django.utils import timezone
from rest_framework import serializers
from decimal import Decimal, ROUND_HALF_UP
from .models import (
    AccountDetails,
    Cart,
    CartItem,
    CustomerAddress,
    OrderItems,
    Orders,
    OpeningTagsEntry,
    OrderTracking,
    Shipment,
    Wishlist,
    CurrentRates,
    PaymentTransaction,
    Rates,
)


ZERO = Decimal("0.00")


def money(value):
    if value is None or value == "":
        return ZERO
    return Decimal(value).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def product_price(product):
    for field in ("selling_price", "mrp_price", "total_price"):
        value = getattr(product, field, None)
        if value is not None:
            return money(value)
    return ZERO


def update_cart_item_totals(item):
    subtotal = money(item.unit_price) * item.quantity
    discount = money(item.discount)
    taxable_amount = max(subtotal - discount, ZERO)
    item.gst_amount = (taxable_amount * money(item.gst_percentage) / Decimal("100")).quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP,
    )
    item.total_price = taxable_amount + item.gst_amount
    return item


def sync_order_item_product_status(order, status_value):
    for order_item in order.items.select_related("product"):
        product = order_item.product
        if product is not None:
            product.status = status_value
            product.save(update_fields=["status"])


class OpeningTagsEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningTagsEntry
        fields = "__all__"





class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAddress
        fields = "__all__"


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = "__all__"


class CartItemSerializer(serializers.ModelSerializer):
    product_details = OpeningTagsEntrySerializer(source="product", read_only=True)
    customer = serializers.PrimaryKeyRelatedField(
        queryset=AccountDetails.objects.all(),
        write_only=True,
        required=False,
    )

    class Meta:
        model = CartItem
        fields = "__all__"
        validators = []
        extra_kwargs = {
            "unit_price": {"required": False},
            "total_price": {"required": False},
            "gst_amount": {"required": False},
        }

    def validate_quantity(self, value):
        if value < 1:
            raise serializers.ValidationError("Quantity must be at least 1.")
        return value

    def validate(self, attrs):
        product = attrs.get("product") or getattr(self.instance, "product", None)
        quantity = attrs.get("quantity", getattr(self.instance, "quantity", 1))
        unit_price = attrs.get("unit_price", getattr(self.instance, "unit_price", None))

        if product and unit_price is None:
            attrs["unit_price"] = product_price(product)

        unit_price = money(attrs.get("unit_price", unit_price))
        discount = money(attrs.get("discount", getattr(self.instance, "discount", 0)))
        gst_percentage = money(attrs.get("gst_percentage", getattr(self.instance, "gst_percentage", 0)))
        subtotal = unit_price * quantity
        taxable_amount = max(subtotal - discount, ZERO)

        attrs["gst_amount"] = (taxable_amount * gst_percentage / Decimal("100")).quantize(
            Decimal("0.01"),
            rounding=ROUND_HALF_UP,
        )
        attrs["total_price"] = taxable_amount + attrs["gst_amount"]
        return attrs

    def create(self, validated_data):
        validated_data.pop("customer", None)
        cart = validated_data["cart"]
        product = validated_data["product"]
        quantity = validated_data.get("quantity", 1)
        existing_item = CartItem.objects.filter(cart=cart, product=product).first()

        if existing_item:
            existing_item.quantity += quantity
            for field in ("unit_price", "discount", "gst_percentage"):
                if field in validated_data:
                    setattr(existing_item, field, validated_data[field])
            update_cart_item_totals(existing_item)
            existing_item.save()
            return existing_item

        return CartItem.objects.create(**validated_data)

    def update(self, instance, validated_data):
        validated_data.pop("customer", None)
        return super().update(instance, validated_data)


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = [
            "cart_id",
            "customer",
            "subtotal",
            "discount",
            "tax_amount",
            "shipping_charge",
            "grand_total",
            "created_at",
            "updated_at",
            "items",
        ]


class OrderItemSerializer(serializers.ModelSerializer):
    product_details = OpeningTagsEntrySerializer(source="product", read_only=True)

    class Meta:
        model = OrderItems
        fields = "__all__"
        extra_kwargs = {
            "order": {"required": False},
        }


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, required=False)

    class Meta:
        model = Orders
        fields = [
            "order_id",
            "order_number",
            "invoice_number",
            "invoice_date",
            "customer",
            "shipping_address",
            "billing_address",
            "subtotal",
            "discount",
            "shipping_charge",
            "tax_amount",
            "grand_total",
            "payment_method",
            "payment_status",
            "order_status",
            "remarks",
            "placed_at",
            "expected_delivery",
            "delivered_at",
            "cancelled_at",
            "created_at",
            "updated_at",
            "items",
        ]
        extra_kwargs = {
            "order_number": {"required": False},
            "invoice_number": {"required": False},
            "invoice_date": {"required": False},
            "grand_total": {"required": False},
            "placed_at": {"required": False},
            "delivered_at": {"required": False},
            "cancelled_at": {"required": False},
        }

    def create(self, validated_data):
        items_data = validated_data.pop("items", [])
        if not validated_data.get("order_number"):
            validated_data["order_number"] = self.generate_order_number()
        if "grand_total" not in validated_data:
            validated_data["grand_total"] = (
                money(validated_data.get("subtotal"))
                - money(validated_data.get("discount"))
                + money(validated_data.get("tax_amount"))
                + money(validated_data.get("shipping_charge"))
            )

        order = Orders.objects.create(**validated_data)

        for item_data in items_data:
            OrderItems.objects.create(order=order, **item_data)

        order_status = validated_data.get("order_status", "Pending")
        if order_status in {"Cancelled", "Returned"}:
            sync_order_item_product_status(order, "Available")
        else:
            sync_order_item_product_status(order, "Sold")

        return order

    @staticmethod
    def generate_order_number():
        return f"ORD-{timezone.now().strftime('%Y%m%d%H%M%S%f')}"


class CheckoutSerializer(serializers.Serializer):
    cart_id = serializers.IntegerField(required=False)
    customer = serializers.PrimaryKeyRelatedField(queryset=AccountDetails.objects.all(), required=False)
    shipping_address = serializers.PrimaryKeyRelatedField(queryset=CustomerAddress.objects.all())
    billing_address = serializers.PrimaryKeyRelatedField(queryset=CustomerAddress.objects.all())
    payment_method = serializers.ChoiceField(choices=Orders.PAYMENT_METHOD)
    remarks = serializers.CharField(required=False, allow_blank=True)

    def validate(self, attrs):
        if not attrs.get("cart_id") and not attrs.get("customer"):
            raise serializers.ValidationError("cart_id or customer is required.")
        return attrs


class OrderTrackingSerializer(serializers.ModelSerializer):
    updated_by_name = serializers.CharField(source="updated_by.full_name", read_only=True)

    class Meta:
        model = OrderTracking
        fields = "__all__"





class CurrentRatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentRates
        fields = "__all__"





class VerifyPaymentSerializer(serializers.Serializer):

    razorpay_order_id = serializers.CharField(
        required=True
    )

    razorpay_payment_id = serializers.CharField(
        required=True
    )

    razorpay_signature = serializers.CharField(
        required=True
    )









class RatesChartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rates
        fields = [
            "rates_id",
            "rate_date",
            "rate_time",
            "rate_9crt",
            "rate_16crt",
            "rate_18crt",
            "rate_22crt",
            "rate_24crt",
            "silver_rate",
        ]
