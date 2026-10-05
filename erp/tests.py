from django.db import connection
from django.test import TransactionTestCase
from django.utils import timezone
from rest_framework.test import APIClient

from .models import AccountDetails, Cart, CartItem, CustomerAddress, OpeningTagsEntry, Orders, Users


class EcommerceCartOrderAPITests(TransactionTestCase):
    reset_sequences = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls._ensure_unmanaged_tables()

    @classmethod
    def _ensure_unmanaged_tables(cls):
        existing_tables = connection.introspection.table_names()
        with connection.schema_editor() as schema_editor:
            for model in (AccountDetails, OpeningTagsEntry, Users):
                if model._meta.db_table not in existing_tables:
                    schema_editor.create_model(model)

    def setUp(self):
        self.client = APIClient()
        self.customer = AccountDetails.objects.create(
            account_name="Test Customer",
            created_at=timezone.now(),
        )
        self.product = OpeningTagsEntry.objects.create(
            product_name="Gold Ring",
            pcode_barcode="BR001",
            huid_no="HUID001",
            category="Rings",
            metal_type="Gold",
            purity="22K",
            gross_weight="10.000",
            weight_bw="9.500",
            stones_weight="0.500",
            making_charges="100.00",
            wastageweight="0.100",
            selling_price=1000,
            date=timezone.now(),
            is_display=1,
            status="Available",
        )
        self.address = CustomerAddress.objects.create(
            customer=self.customer,
            full_name="Test Customer",
            mobile="9999999999",
            address_line1="Main Road",
            city="Hyderabad",
            state="Telangana",
            pincode="500001",
        )

    def test_add_item_creates_cart_and_merges_duplicate_product(self):
        payload = {
            "customer": self.customer.pk,
            "product": self.product.pk,
            "quantity": 2,
            "unit_price": "1000.00",
            "discount": "50.00",
            "gst_percentage": "18.00",
        }

        first_response = self.client.post("/api/cart/add-item/", payload, format="json")
        second_response = self.client.post("/api/cart/add-item/", payload, format="json")

        self.assertEqual(first_response.status_code, 201)
        self.assertEqual(second_response.status_code, 201)
        self.assertEqual(Cart.objects.count(), 1)
        self.assertEqual(CartItem.objects.count(), 1)

        item = CartItem.objects.get()
        cart = Cart.objects.get()
        self.assertEqual(item.quantity, 4)
        self.assertEqual(str(item.gst_percentage), "18.00")
        self.assertEqual(str(cart.subtotal), "4000.00")
        self.assertEqual(str(cart.tax_amount), "711.00")
        self.assertEqual(str(cart.grand_total), "4661.00")

    def test_checkout_by_cart_id_creates_order_and_clears_cart(self):
        cart = Cart.objects.create(customer=self.customer)
        CartItem.objects.create(
            cart=cart,
            product=self.product,
            quantity=1,
            unit_price="1000.00",
            discount="0.00",
            gst_percentage="18.00",
            gst_amount="180.00",
            total_price="1180.00",
        )

        response = self.client.post(
            "/api/checkout/",
            {
                "cart_id": cart.pk,
                "shipping_address": self.address.pk,
                "billing_address": self.address.pk,
                "payment_method": "COD",
            },
            format="json",
        )

        self.assertEqual(response.status_code, 201)
        order = Orders.objects.get()
        self.assertTrue(order.order_number.startswith("ORD-"))
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.items.count(), 1)
        self.assertFalse(cart.items.exists())

    def test_checkout_marks_product_sold_and_cancel_restores_availability(self):
        cart = Cart.objects.create(customer=self.customer)
        CartItem.objects.create(
            cart=cart,
            product=self.product,
            quantity=1,
            unit_price="1000.00",
            discount="0.00",
            gst_percentage="18.00",
            gst_amount="180.00",
            total_price="1180.00",
        )

        checkout_response = self.client.post(
            "/api/checkout/",
            {
                "cart_id": cart.pk,
                "shipping_address": self.address.pk,
                "billing_address": self.address.pk,
                "payment_method": "COD",
            },
            format="json",
        )

        self.assertEqual(checkout_response.status_code, 201)
        self.product.refresh_from_db()
        self.assertEqual(self.product.status, "Sold")

        order = Orders.objects.get()
        cancel_response = self.client.post(f"/api/orders/{order.order_id}/cancel/")

        self.assertEqual(cancel_response.status_code, 200)
        self.product.refresh_from_db()
        self.assertEqual(self.product.status, "Available")
