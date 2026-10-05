from django.urls import path
from .views import (
    CartAPIView,
    CartAddItemAPIView,
    CartItemListCreateAPIView,
    CartItemRetrieveUpdateDeleteAPIView,
    CartRetrieveUpdateDeleteAPIView,
    CartUpdateItemAPIView,
    CartRemoveItemAPIView,
    CartClearAPIView,
    CheckoutAPIView,
    CustomerAddressListCreateAPIView,
    CustomerAddressRetrieveUpdateDeleteAPIView,
    OpeningTagsEntryListAPIView,
    OpeningTagsEntryRetrieveAPIView,
    OrderCancelAPIView,
    OrderInvoiceAPIView,
    OrderListCreateAPIView,
    OrderReturnAPIView,
    OrderRetrieveUpdateDeleteAPIView,
    OrderTrackingAPIView,
    WishlistListCreateAPIView,
    WishlistRetrieveDeleteAPIView,
    CurrentRatesAPIView,
    VerifyPaymentAPIView,
    PaymentTransactionListAPIView,
    RatesChartAPIView,
)

urlpatterns = [
    # Get all products (supports filters)
    path("opening-tags/", OpeningTagsEntryListAPIView.as_view(), name="opening-tags-list"),
    path("opening-tags/<int:pk>/", OpeningTagsEntryRetrieveAPIView.as_view(), name="opening-tags-detail"),

    # Customer addresses
    path("customer-addresses/", CustomerAddressListCreateAPIView.as_view(), name="customer-address-list"),
    path("customer-addresses/<int:pk>/", CustomerAddressRetrieveUpdateDeleteAPIView.as_view(), name="customer-address-detail"),

    # Wishlist
    path("wishlist/", WishlistListCreateAPIView.as_view(), name="wishlist-list"),
    path("wishlist/<int:pk>/", WishlistRetrieveDeleteAPIView.as_view(), name="wishlist-detail"),

    # Cart endpoints
    path("cart/", CartAPIView.as_view(), name="cart-detail"),
    path("cart/<int:pk>/", CartRetrieveUpdateDeleteAPIView.as_view(), name="cart-crud-detail"),
    path("cart/add-item/", CartAddItemAPIView.as_view(), name="cart-add-item"),
    path("cart/update-item/", CartUpdateItemAPIView.as_view(), name="cart-update-item"),
    path("cart/remove-item/<int:cart_item_id>/", CartRemoveItemAPIView.as_view(), name="cart-remove-item"),
    path("cart/clear/", CartClearAPIView.as_view(), name="cart-clear"),
    path("cart-items/", CartItemListCreateAPIView.as_view(), name="cart-item-list"),
    path("cart-items/<int:pk>/", CartItemRetrieveUpdateDeleteAPIView.as_view(), name="cart-item-detail"),

    # Checkout endpoints
    path("checkout/", CheckoutAPIView.as_view(), name="checkout"),
    path("verify-payment/",VerifyPaymentAPIView.as_view(),name="verify-payment"),

    # Orders
    path("orders/", OrderListCreateAPIView.as_view(), name="order-list"),
    path("orders/<int:pk>/", OrderRetrieveUpdateDeleteAPIView.as_view(), name="order-detail"),
    path("orders/<int:pk>/cancel/", OrderCancelAPIView.as_view(), name="order-cancel"),
    path("orders/<int:pk>/return/", OrderReturnAPIView.as_view(), name="order-return"),
    path("orders/<int:pk>/invoice/", OrderInvoiceAPIView.as_view(), name="order-invoice"),
    path("orders/<int:pk>/tracking/", OrderTrackingAPIView.as_view(), name="order-tracking"),

    path(
        "current-rates/",
        CurrentRatesAPIView.as_view(),
        name="current-rates"
    ),

    path(
        "payment-transactions/",
        PaymentTransactionListAPIView.as_view(),
        name="payment-transactions"
    ),
    path(
        "rates/",
        RatesChartAPIView.as_view(),
        name="rates-chart"
    ),
]
