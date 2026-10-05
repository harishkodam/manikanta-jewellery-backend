import django_filters
from .models import OpeningTagsEntry


class OpeningTagsEntryFilter(django_filters.FilterSet):
    class Meta:
        model = OpeningTagsEntry
        fields = {
            'opentag_id': ['exact'],
            'product_id': ['exact'],
            'subcategory_id': ['exact'],
            'category': ['exact', 'icontains'],
            'sub_category': ['exact', 'icontains'],
            'product_name': ['exact', 'icontains'],
            'pcode_barcode': ['exact', 'icontains'],
            'huid_no': ['exact', 'icontains'],
            'account_name': ['exact', 'icontains'],
            'invoice': ['exact', 'icontains'],
            'status': ['exact'],
            'source': ['exact'],
            'stock_point': ['exact'],
            'metal_type': ['exact'],
            'purity': ['exact'],
            'gross_weight': ['exact', 'gte', 'lte'],
            'weight_bw': ['exact', 'gte', 'lte'],
            'totalweight_aw': ['exact', 'gte', 'lte'],
            'rate': ['exact', 'gte', 'lte'],
            'selling_price': ['exact', 'gte', 'lte'],
            'mrp_price': ['exact', 'gte', 'lte'],
            'total_price': ['exact', 'gte', 'lte'],
            'date': ['exact', 'gte', 'lte'],
            'tag_id': ['exact'],
            'pcs': ['exact', 'gte', 'lte'],
            'size': ['exact'],
            'design_master': ['exact', 'icontains'],
            'qr_status': ['exact'],
            'is_display': ['exact'],
        }



from django_filters import rest_framework as filters

from .models import PaymentTransaction


class PaymentTransactionFilter(filters.FilterSet):

    # =====================================================
    # PAYMENT METHOD
    # From Orders table
    # Online / COD / Wallet
    # =====================================================

    payment_method = filters.CharFilter(
        field_name="order__payment_method",
        lookup_expr="iexact"
    )

    # =====================================================
    # PAYMENT MODE
    # From PaymentTransaction table
    # UPI / Card / NetBanking / etc.
    # =====================================================

    payment_mode = filters.CharFilter(
        field_name="payment_mode",
        lookup_expr="iexact"
    )

    # =====================================================
    # TRANSACTION STATUS
    # pending / success / failed / refunded
    # =====================================================

    status = filters.CharFilter(
        field_name="status",
        lookup_expr="iexact"
    )

    # =====================================================
    # ORDER ID
    # =====================================================

    order_id = filters.NumberFilter(
        field_name="order_id"
    )

    # =====================================================
    # CUSTOMER ID
    # =====================================================

    customer_id = filters.NumberFilter(
        field_name="customer_id"
    )

    # =====================================================
    # RAZORPAY ORDER ID
    # =====================================================

    razorpay_order_id = filters.CharFilter(
        field_name="razorpay_order_id",
        lookup_expr="iexact"
    )

    # =====================================================
    # RAZORPAY PAYMENT ID
    # =====================================================

    razorpay_payment_id = filters.CharFilter(
        field_name="razorpay_payment_id",
        lookup_expr="iexact"
    )

    # =====================================================
    # DATE FROM
    # =====================================================

    date_from = filters.DateFilter(
        field_name="created_at",
        lookup_expr="date__gte"
    )

    # =====================================================
    # DATE TO
    # =====================================================

    date_to = filters.DateFilter(
        field_name="created_at",
        lookup_expr="date__lte"
    )

    # =====================================================
    # MINIMUM AMOUNT
    # =====================================================

    amount_min = filters.NumberFilter(
        field_name="amount",
        lookup_expr="gte"
    )

    # =====================================================
    # MAXIMUM AMOUNT
    # =====================================================

    amount_max = filters.NumberFilter(
        field_name="amount",
        lookup_expr="lte"
    )

    class Meta:
        model = PaymentTransaction

        fields = [
            "payment_method",
            "payment_mode",
            "status",
            "order_id",
            "customer_id",
            "razorpay_order_id",
            "razorpay_payment_id",
            "date_from",
            "date_to",
            "amount_min",
            "amount_max",
        ]
        