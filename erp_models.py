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
