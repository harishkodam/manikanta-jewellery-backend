# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    retype_password = models.CharField(max_length=50, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)
    user_type_id = models.IntegerField(blank=True, null=True)
    full_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class AccountDetails(models.Model):
    account_id = models.AutoField(primary_key=True)
    account_name = models.CharField(max_length=255, blank=True, null=True)
    print_name = models.CharField(max_length=255, blank=True, null=True)
    account_group = models.CharField(max_length=255, blank=True, null=True)
    op_bal = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    metal_balance = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    dr_cr = models.CharField(max_length=2, blank=True, null=True)
    address1 = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    state_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    anniversary = models.DateField(blank=True, null=True)
    bank_account_no = models.CharField(max_length=50, blank=True, null=True)
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    ifsc_code = models.CharField(max_length=20, blank=True, null=True)
    branch = models.CharField(max_length=255, blank=True, null=True)
    gst_in = models.CharField(max_length=15, blank=True, null=True)
    aadhar_card = models.CharField(max_length=12, blank=True, null=True)
    pan_card = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField()
    religion = models.CharField(max_length=100, blank=True, null=True)
    images = models.CharField(max_length=450, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    joining_date = models.DateField(blank=True, null=True)
    kyc_status = models.CharField(max_length=8, blank=True, null=True)
    aadhaar_document = models.CharField(max_length=450, blank=True, null=True)
    pan_document = models.CharField(max_length=450, blank=True, null=True)
    verified_by = models.IntegerField(blank=True, null=True)
    rejection_reason = models.TextField(blank=True, null=True)
    referred_person_name = models.CharField(max_length=200, blank=True, null=True)
    referred_person_id = models.CharField(max_length=50, blank=True, null=True)
    referred_person_referral_code = models.CharField(max_length=50, blank=True, null=True)
    customer_referral_code = models.CharField(unique=True, max_length=30, blank=True, null=True)
    nominee_name = models.CharField(max_length=200, blank=True, null=True)
    nominee_email = models.CharField(max_length=255, blank=True, null=True)
    nominee_phone_number = models.CharField(max_length=15, blank=True, null=True)
    relationship = models.CharField(max_length=100, blank=True, null=True)
    nominee_aadhaar_number = models.CharField(max_length=20, blank=True, null=True)
    nominee_pan_number = models.CharField(max_length=20, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_details'


class OpeningTagsEntry(models.Model):
    opentag_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField(blank=True, null=True)
    subcategory_id = models.IntegerField(blank=True, null=True)
    sub_category = models.CharField(max_length=200, blank=True, null=True)
    pricing = models.CharField(db_column='Pricing', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prefix = models.CharField(db_column='Prefix', max_length=255, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=200, blank=True, null=True)
    purity = models.CharField(db_column='Purity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    metal_type = models.CharField(max_length=255, blank=True, null=True)
    pcode_barcode = models.CharField(db_column='PCode_BarCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gross_weight = models.DecimalField(db_column='Gross_Weight', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    stones_weight = models.DecimalField(db_column='Stones_Weight', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    stones_price = models.DecimalField(db_column='Stones_Price', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    weight_bw = models.DecimalField(db_column='Weight_BW', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    huid_no = models.CharField(db_column='HUID_No', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wastage_on = models.CharField(db_column='Wastage_On', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wastage_percentage = models.DecimalField(db_column='Wastage_Percentage', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    wastageweight = models.DecimalField(db_column='WastageWeight', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    mc_per_gram = models.DecimalField(db_column='MC_Per_Gram', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    making_charges_on = models.CharField(db_column='Making_Charges_On', max_length=200, blank=True, null=True)  # Field name made lowercase.
    totalweight_aw = models.DecimalField(db_column='TotalWeight_AW', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    making_charges = models.DecimalField(db_column='Making_Charges', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tax = models.CharField(max_length=20, blank=True, null=True)
    tax_amt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    status = models.CharField(db_column='Status', max_length=200, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=200, blank=True, null=True)  # Field name made lowercase.
    stock_point = models.CharField(db_column='Stock_Point', max_length=255, blank=True, null=True)  # Field name made lowercase.
    making_on = models.CharField(max_length=250, blank=True, null=True)
    dropdown = models.CharField(max_length=250, blank=True, null=True)
    selling_price = models.IntegerField(blank=True, null=True)
    pcs = models.IntegerField(blank=True, null=True)
    pieace_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    design_master = models.CharField(max_length=200, blank=True, null=True)
    product_name = models.CharField(db_column='product_Name', max_length=200, blank=True, null=True)  # Field name made lowercase.
    qr_status = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField()
    cut = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    clarity = models.CharField(max_length=255, blank=True, null=True)
    stone_price_per_carat = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    deduct_st_wt = models.CharField(db_column='deduct_st_Wt', max_length=5, blank=True, null=True)  # Field name made lowercase.
    mc_per_gram_label = models.CharField(db_column='MC_Per_Gram_Label', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pur_gross_weight = models.DecimalField(db_column='pur_Gross_Weight', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pur_stones_weight = models.DecimalField(db_column='pur_Stones_Weight', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pur_deduct_st_wt = models.CharField(db_column='pur_deduct_st_Wt', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pur_stone_price_per_carat = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pur_stones_price = models.DecimalField(db_column='pur_Stones_Price', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pur_weight_bw = models.DecimalField(db_column='pur_Weight_BW', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pur_making_charges_on = models.CharField(db_column='pur_Making_Charges_On', max_length=30, blank=True, null=True)  # Field name made lowercase.
    pur_mc_per_gram = models.DecimalField(db_column='pur_MC_Per_Gram', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pur_making_charges = models.DecimalField(db_column='pur_Making_Charges', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pur_wastage_on = models.CharField(db_column='pur_Wastage_On', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pur_wastage_percentage = models.DecimalField(db_column='pur_Wastage_Percentage', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pur_wastageweight = models.DecimalField(db_column='pur_WastageWeight', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pur_totalweight_aw = models.DecimalField(db_column='pur_TotalWeight_AW', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    tag_id = models.IntegerField(blank=True, null=True)
    tag_weight = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    size = models.CharField(max_length=45, blank=True, null=True)
    account_name = models.CharField(max_length=100, blank=True, null=True)
    invoice = models.CharField(max_length=100, blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    item_prefix = models.CharField(max_length=45, blank=True, null=True)
    suffix = models.CharField(max_length=45, blank=True, null=True)
    pur_mc_per_gram_label = models.CharField(db_column='pur_MC_Per_Gram_Label', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tax_percent = models.CharField(max_length=30, blank=True, null=True)
    mrp_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_pcs_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pur_rate_cut = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pur_purity = models.CharField(db_column='pur_Purity', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pur_puritypercentage = models.CharField(db_column='pur_purityPercentage', max_length=45, blank=True, null=True)  # Field name made lowercase.
    printing_purity = models.CharField(max_length=45, blank=True, null=True)
    is_display = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'opening_tags_entry'






class CustomerAddress(models.Model):

    ADDRESS_TYPE = (
        ('Home', 'Home'),
        ('Office', 'Office'),
        ('Other', 'Other'),
    )

    address_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(AccountDetails,on_delete=models.CASCADE)

    address_type = models.CharField(
        max_length=20,
        choices=ADDRESS_TYPE,
        default='Home'
    )

    full_name = models.CharField(max_length=150)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(max_length=150,blank=True,null=True)

    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255,blank=True)

    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100,default='India')
    pincode = models.CharField(max_length=10)

    landmark = models.CharField(max_length=200,blank=True)

    is_default=models.BooleanField(default=False)

    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "customer_addresses"
        ordering = ['-address_id']

    def __str__(self):
        return f"{self.full_name} - {self.city}"


class Wishlist(models.Model):

    wishlist_id = models.AutoField(primary_key=True)

    customer = models.ForeignKey(
        AccountDetails,
        on_delete=models.CASCADE,
        related_name='wishlist_items'
    )

    product = models.ForeignKey(
        OpeningTagsEntry,
        on_delete=models.CASCADE,
        related_name='wishlisted_by'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "wishlist"
        ordering = ['-wishlist_id']
        unique_together = ('customer', 'product')

    def __str__(self):
        return f"{self.customer.account_name} - {self.product.product_name}"


class Cart(models.Model):

    cart_id = models.AutoField(primary_key=True)

    customer = models.OneToOneField(
        AccountDetails,
        on_delete=models.CASCADE,
        related_name='cart'
    )

    subtotal = models.DecimalField(max_digits=12,decimal_places=2,default=0)

    discount = models.DecimalField(max_digits=12,decimal_places=2,default=0)

    tax_amount = models.DecimalField(max_digits=12,decimal_places=2,default=0, null=True, blank=True)

    shipping_charge = models.DecimalField(max_digits=12,decimal_places=2,default=0, null=True, blank=True)

    grand_total = models.DecimalField(max_digits=12,decimal_places=2,default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "cart"
        ordering = ['-cart_id']

    def __str__(self):
        return f"Cart - {self.customer.account_name}"     
class CartItem(models.Model):

    cart_item_id = models.AutoField(primary_key=True)

    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items'
    )

    product = models.ForeignKey(
        OpeningTagsEntry,
        on_delete=models.CASCADE,
        related_name='cart_items'
    )

    quantity = models.PositiveIntegerField(default=1)

    unit_price = models.DecimalField(max_digits=12,decimal_places=2)

    discount = models.DecimalField(max_digits=12,decimal_places=2,default=0)

    gst_percentage = models.DecimalField(max_digits=5,decimal_places=2,default=0)

    gst_amount = models.DecimalField(max_digits=12,decimal_places=2,default=0)

    total_price = models.DecimalField(max_digits=12,decimal_places=2)

    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "cart_items"
        ordering = ['-cart_item_id']
        unique_together = ('cart', 'product')

    def __str__(self):
        return f"{self.product.product_name}"

class Orders(models.Model):

    ORDER_STATUS = (
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Packed', 'Packed'),
        ('Shipped', 'Shipped'),
        ('Out For Delivery', 'Out For Delivery'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
        ('Returned', 'Returned'),
    )

    PAYMENT_STATUS = (
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
        ('Failed', 'Failed'),
        ('Refunded', 'Refunded'),
    )

    PAYMENT_METHOD = (
        ('Online', 'Online'),
        ('COD', 'Cash On Delivery'),
        ('Wallet', 'Wallet'),
    )

    order_id = models.AutoField(primary_key=True)

    order_number = models.CharField(max_length=30,unique=True)

    invoice_number = models.CharField(max_length=30,unique=True,blank=True,null=True)

    invoice_date = models.DateTimeField(blank=True,null=True)
    
    customer = models.ForeignKey(
        AccountDetails,
        on_delete=models.PROTECT,
        related_name='orders'
    )

    shipping_address = models.ForeignKey(
        CustomerAddress,
        on_delete=models.PROTECT,
        related_name='shipping_orders'
    )

    billing_address = models.ForeignKey(
        CustomerAddress,
        on_delete=models.PROTECT,
        related_name='billing_orders'
    )

    subtotal = models.DecimalField(max_digits=12,decimal_places=2,default=0)

    discount = models.DecimalField(max_digits=12,decimal_places=2,default=0)

    shipping_charge = models.DecimalField(max_digits=12,decimal_places=2,default=0)

    tax_amount = models.DecimalField(max_digits=12,decimal_places=2,default=0)

    grand_total = models.DecimalField(max_digits=12,decimal_places=2)

    payment_method = models.CharField(max_length=20,choices=PAYMENT_METHOD)

    payment_status = models.CharField(max_length=20,choices=PAYMENT_STATUS,default='Pending')

    order_status = models.CharField(max_length=30,choices=ORDER_STATUS,default='Pending')

    remarks = models.TextField(blank=True,null=True)

    placed_at = models.DateTimeField(auto_now_add=True)

    expected_delivery = models.DateField(blank=True,null=True)

    delivered_at = models.DateTimeField(blank=True,null=True)

    cancelled_at = models.DateTimeField(blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "orders"
        ordering = ['-order_id']

    def __str__(self):
        return self.order_number
class OrderItems(models.Model):

    order_item_id = models.AutoField(primary_key=True)

    order = models.ForeignKey(
        Orders,
        on_delete=models.CASCADE,
        related_name='items'
    )

    product = models.ForeignKey(
        OpeningTagsEntry,
        on_delete=models.PROTECT,
        related_name='order_items'
    )

    barcode = models.CharField(max_length=100,blank=True,null=True)

    huid_number = models.CharField(max_length=100,blank=True,null=True)

    hsn_number = models.CharField(max_length=100,blank=True,null=True)

    product_name = models.CharField(max_length=255)

    category = models.CharField(max_length=100,blank=True,null=True)

    metal_type = models.CharField(max_length=50,blank=True,null=True)

    purity = models.CharField(max_length=50,blank=True,null=True)

    gross_weight = models.DecimalField(max_digits=10,decimal_places=3,default=0)

    net_weight = models.DecimalField(max_digits=10,decimal_places=3,default=0)

    stone_weight = models.DecimalField(max_digits=10,decimal_places=3,default=0)

    making_charge = models.DecimalField(max_digits=12,decimal_places=2,default=0)

    wastage = models.DecimalField(max_digits=12,decimal_places=2,default=0)

    unit_price = models.DecimalField(max_digits=12,decimal_places=2)

    quantity = models.PositiveIntegerField(default=1)

    discount = models.DecimalField(max_digits=12,decimal_places=2,default=0)

    gst_percentage = models.DecimalField(max_digits=5,decimal_places=2,default=0)

    gst_amount = models.DecimalField(max_digits=12,decimal_places=2,default=0)

    total_price = models.DecimalField(max_digits=12,decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "order_items"

    def __str__(self):
        return f"{self.order.order_number} - {self.product_name}"

# class Payments(models.Model):

#     PAYMENT_GATEWAY = (
#         ('Razorpay', 'Razorpay'),
#         ('PhonePe', 'PhonePe'),
#         ('Cashfree', 'Cashfree'),
#         ('PayU', 'PayU'),
#         ('Stripe', 'Stripe'),
#         ('COD', 'Cash On Delivery'),
#     )

#     PAYMENT_STATUS = (
#         ('Pending', 'Pending'),
#         ('Success', 'Success'),
#         ('Failed', 'Failed'),
#         ('Refunded', 'Refunded'),
#         ('Cancelled', 'Cancelled'),
#     )

#     payment_id = models.AutoField(primary_key=True)

#     order = models.ForeignKey(
#         Orders,
#         on_delete=models.CASCADE,
#         related_name='payments'
#     )

#     payment_gateway = models.CharField(max_length=30,choices=PAYMENT_GATEWAY)

#     gateway_order_id = models.CharField(max_length=150,blank=True,null=True)

#     transaction_id = models.CharField(max_length=150,blank=True,null=True)

#     payment_reference = models.CharField(max_length=150,blank=True,null=True)

#     amount = models.DecimalField(max_digits=12,decimal_places=2)

#     currency = models.CharField(max_length=10,default='INR')

#     payment_status = models.CharField(max_length=20,choices=PAYMENT_STATUS,default='Pending')

#     gateway_response = models.JSONField(blank=True,null=True)

#     remarks = models.TextField(blank=True,null=True)

#     paid_at = models.DateTimeField(blank=True,null=True)

#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         db_table = "payments"
#         ordering = ['-payment_id']

#     def __str__(self):
#         return self.transaction_id or str(self.payment_id)





class PaymentTransaction(models.Model):

    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("success", "Success"),
        ("failed", "Failed"),
        ("refunded", "Refunded"),
    )

    payment_transaction_id = models.AutoField(
        primary_key=True
    )

    order = models.ForeignKey(
        Orders,
        on_delete=models.CASCADE,
        related_name="payments"
    )

    customer = models.ForeignKey(
        AccountDetails,
        on_delete=models.CASCADE
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    currency = models.CharField(
        max_length=10,
        default="INR"
    )
    payment_mode = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )

    razorpay_order_id = models.CharField(
        max_length=200,
        unique=True
    )

    razorpay_payment_id = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    razorpay_signature = models.TextField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    gateway_response = models.JSONField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "payment_transactions"

    def __str__(self):
        return self.razorpay_order_id



class Shipment(models.Model):

    SHIPPING_STATUS = (
        ('Pending', 'Pending'),
        ('Packed', 'Packed'),
        ('Ready To Ship', 'Ready To Ship'),
        ('Shipped', 'Shipped'),
        ('Out For Delivery', 'Out For Delivery'),
        ('Delivered', 'Delivered'),
        ('Returned', 'Returned'),
    )

    shipment_id = models.AutoField(primary_key=True)

    order = models.OneToOneField(
        Orders,
        on_delete=models.CASCADE,
        related_name='shipment'
    )

    courier_name = models.CharField(max_length=100,blank=True,null=True)

    tracking_number = models.CharField(max_length=100,blank=True,null=True)

    tracking_url = models.URLField(blank=True,null=True)

    shipping_status = models.CharField(max_length=30,choices=SHIPPING_STATUS,default='Pending')

    shipped_at = models.DateTimeField(blank=True,null=True)

    expected_delivery = models.DateField(blank=True,null=True)

    delivered_at = models.DateTimeField(blank=True,null=True)

    shipping_charge = models.DecimalField(max_digits=10,decimal_places=2,default=0)

    remarks = models.TextField(blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "shipment"

    def __str__(self):
        return self.order.order_number    

class OrderTracking(models.Model):

    tracking_id = models.AutoField(primary_key=True)

    order = models.ForeignKey(
        Orders,
        on_delete=models.CASCADE,
        related_name='tracking_history'
    )

    status = models.CharField(max_length=50)

    remarks = models.TextField(blank=True,null=True)

    updated_by = models.ForeignKey(
        Users,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "order_tracking"
        ordering = ['tracking_id']

    def __str__(self):
        return f"{self.order.order_number} - {self.status}"


class ProductReview(models.Model):

    REVIEW_STATUS = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    review_id = models.AutoField(primary_key=True)

    customer = models.ForeignKey(
        AccountDetails,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    product = models.ForeignKey(
        OpeningTagsEntry,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    order = models.ForeignKey(
        Orders,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    rating = models.PositiveSmallIntegerField()

    review_title = models.CharField(max_length=200,blank=True,null=True)

    review = models.TextField(blank=True,null=True)

    is_verified_purchase = models.BooleanField(default=False)

    status = models.CharField(max_length=20,choices=REVIEW_STATUS,default='Pending')

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "product_reviews"

    def __str__(self):
        return self.product.product_name

        
class Coupons(models.Model):

    DISCOUNT_TYPE = (
        ('Percentage', 'Percentage'),
        ('Flat', 'Flat Amount'),
    )

    coupon_id = models.AutoField(primary_key=True)

    coupon_code = models.CharField(max_length=30,unique=True)

    coupon_name = models.CharField(max_length=100)

    discount_type = models.CharField(max_length=20,choices=DISCOUNT_TYPE)

    discount_value = models.DecimalField(max_digits=10,decimal_places=2)

    minimum_order_amount = models.DecimalField(max_digits=10,decimal_places=2,default=0)

    maximum_discount = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)

    start_date = models.DateTimeField()

    expiry_date = models.DateTimeField()

    usage_limit = models.IntegerField(default=0)

    used_count = models.IntegerField(default=0)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "coupons"

    def __str__(self):
        return self.coupon_code

class OrderCoupon(models.Model):

    id = models.AutoField(primary_key=True)

    order = models.OneToOneField(
        Orders,
        on_delete=models.CASCADE,
        related_name='coupon'
    )

    coupon = models.ForeignKey(Coupons,on_delete=models.PROTECT)

    discount_amount = models.DecimalField(max_digits=10,decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "order_coupon"             

class Notifications(models.Model):

    notification_id = models.AutoField(primary_key=True)

    customer = models.ForeignKey(
        AccountDetails,
        on_delete=models.CASCADE,
        related_name='notifications'
    )

    title = models.CharField(max_length=200)

    message = models.TextField()

    notification_type = models.CharField(max_length=50,blank=True,null=True)

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "notifications"

    def __str__(self):
        return self.title        


class ProductImages(models.Model):

    image_id = models.AutoField(primary_key=True)

    product = models.ForeignKey(
        OpeningTagsEntry,
        on_delete=models.CASCADE,
        related_name='images'
    )

    image = models.ImageField(upload_to='product_images/')

    is_primary = models.BooleanField(default=False)

    display_order = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "product_images"    


class ProductVideos(models.Model):

    video_id = models.AutoField(primary_key=True)

    product = models.ForeignKey(
        OpeningTagsEntry,
        on_delete=models.CASCADE,
        related_name='videos'
    )

    video = models.FileField(upload_to='product_videos/')

    thumbnail = models.ImageField(upload_to='video_thumbnails/',blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "product_videos"        









class CurrentRates(models.Model):
    current_rates_id = models.AutoField(primary_key=True)
    rate_date = models.DateField()
    rate_time = models.TimeField()
    rate_9crt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rate_16crt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rate_18crt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rate_22crt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rate_24crt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    silver_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'current_rates'
        unique_together = (('rate_date', 'rate_time'),)


class Rates(models.Model):
    rates_id = models.AutoField(primary_key=True)
    rate_date = models.DateField()
    rate_time = models.TimeField()
    rate_9crt = models.IntegerField(blank=True, null=True)
    rate_16crt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rate_18crt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rate_22crt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rate_24crt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    silver_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rates'