from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.hashers import identify_hasher, make_password
import random,string
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db.models import Sum
import re


# from .erp_models import Users
# from .erp_models import AccountDetails



from erp.models import Users
from erp.models import AccountDetails


class Scheme(models.Model):

    BENEFIT_CHOICES = (
        ('no_wastage', 'No wastage'),
        ('no_making_charges', 'No making charges'),
        ('no_making_no_wastage', 'No making and no wastage'),
        ('x_plus_y', 'x+y installments (pay x + get y installment benefit)'),
    )

    scheme_id = models.AutoField(primary_key=True)

    scheme_name = models.CharField(
        max_length=200,
        unique=True
    )

    scheme_maturity_period = models.IntegerField(
        null=True,
        blank=True
    )

    scheme_benefit = models.CharField(
        max_length=50,
        choices=BENEFIT_CHOICES
    )

    scheme_installment_amount = models.IntegerField(
        null=True,
        blank=True
    )

    x_value = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    y_value = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    payable_installments = models.IntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    # created_by = models.ForeignKey(
    #     'User',
    #     null=True,
    #     blank=True,
    #     related_name='schemes_created',
    #     on_delete=models.SET_NULL
    # )

    created_by = models.ForeignKey(
    Users,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="schemes_created"
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    # updated_by = models.ForeignKey(
    #     'User',
    #     null=True,
    #     blank=True,
    #     related_name='schemes_updated',
    #     on_delete=models.SET_NULL
    # )

    updated_by = models.ForeignKey(
    Users,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="schemes_updated"
    )

    def save(self, *args, **kwargs):

        if self.scheme_installment_amount and self.scheme_installment_amount > 0:

            if self.scheme_benefit == 'x_plus_y':
                self.payable_installments = self.x_value or 0
            else:
                self.payable_installments = self.scheme_maturity_period or 0

        else:
            self.payable_installments = 0

        super().save(*args, **kwargs)

    def __str__(self):
        return self.scheme_name
    
class CustomerSchemeEnrollment(models.Model):

    STATUS_CHOICES = (
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('closed', 'Closed'),
        ('cancelled', 'Cancelled'),
        ('defaulted', 'Defaulted'),
    )

    enrollment_id = models.AutoField(
        primary_key=True
    )

    enrollment_number = models.CharField(
        max_length=50,
        unique=True,
        db_index=True
    )

    # customer = models.ForeignKey(
    #     'Customer',
    #     on_delete=models.CASCADE,
    #     related_name='enrollments'
    # )

    customer = models.ForeignKey(
    AccountDetails,
    on_delete=models.CASCADE,
    related_name="scheme_enrollments"
    )

    scheme = models.ForeignKey(
        'Scheme',
        on_delete=models.PROTECT,
        related_name='enrollments'
    )

    enrollment_date = models.DateField(
        default=timezone.now
    )

    maturity_date = models.DateField()

    installment_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    total_installments = models.PositiveIntegerField()

    paid_installments = models.PositiveIntegerField(
        default=0
    )

    pending_installments = models.PositiveIntegerField(
        default=0
    )

    total_paid_amount = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0
    )

    remarks = models.TextField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active'
    )

    # created_by = models.ForeignKey(
    #     User,
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True
    # )

    created_by = models.ForeignKey(
    Users,
    on_delete=models.SET_NULL,
    null=True,
    blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):

        if not self.pk:

            if not self.enrollment_number:
                self.enrollment_number = (
                    self.generate_enrollment_number()
                )

            self.paid_installments = 0
            self.pending_installments = self.total_installments
            self.total_paid_amount = 0

        super().save(*args, **kwargs)

    def generate_enrollment_number(self):

        last_enrollment = CustomerSchemeEnrollment.objects.order_by(
            '-enrollment_id'
        ).first()

        if last_enrollment and last_enrollment.enrollment_number:

            match = re.search(
                r'(\d+)$',
                last_enrollment.enrollment_number
            )

            if match:
                next_number = int(match.group(1)) + 1
            else:
                next_number = 1

        else:
            next_number = 1

        return f"ENR{next_number:06d}"    

    def update_installment_summary(self):

        paid_count = self.installments.filter(
            status='paid'
        ).count()

        total_paid = self.installments.aggregate(
            total=Sum('paid_amount')
        )['total'] or 0

        self.paid_installments = paid_count

        self.pending_installments = (
            self.total_installments - paid_count
        )

        self.total_paid_amount = total_paid

        # Auto Complete Enrollment
        if (
            self.total_installments > 0 and
            paid_count >= self.total_installments
        ):
            self.status = 'completed'

        self.save(
            update_fields=[
                'paid_installments',
                'pending_installments',
                'total_paid_amount',
                'status'
            ]
        )

    def __str__(self):
        return self.enrollment_number

class SchemeInstallment(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('overdue', 'Overdue'),
        ('cancelled', 'Cancelled'),
    )

    installment_id = models.AutoField(
        primary_key=True
    )

    enrollment = models.ForeignKey(
        CustomerSchemeEnrollment,
        on_delete=models.CASCADE,
        related_name='installments'
    )

    installment_no = models.PositiveIntegerField()

    due_date = models.DateField()

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    paid_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    paid_date = models.DateField(
        null=True,
        blank=True
    )

    receipt_number = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    payment_mode = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    transaction_reference = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    remarks = models.TextField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        unique_together = (
            'enrollment',
            'installment_no'
        )
        ordering = ['installment_no']

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

        # Update Enrollment Summary
        self.enrollment.update_installment_summary()

    def __str__(self):
        return (
            f"{self.enrollment.enrollment_number} - "
            f"Installment {self.installment_no}"
        )

class SchemeReceipt(models.Model):

    receipt_id = models.AutoField(
        primary_key=True
    )

    installment = models.ForeignKey(
        SchemeInstallment,
        on_delete=models.CASCADE,
        related_name='receipts'
    )

    receipt_number = models.CharField(
        max_length=50,
        unique=True
    )

    receipt_date = models.DateField(
        default=timezone.now
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    payment_mode = models.CharField(
        max_length=20
    )

    transaction_reference = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    remarks = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )            



class SchemeTransaction(models.Model):

    STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('success', 'Success'),
    ('failed', 'Failed'),
    ('refunded', 'Refunded'),
    )

    transaction_id = models.AutoField(primary_key=True)

    # installment = models.ForeignKey(
    #     'SchemeInstallment',
    #     on_delete=models.CASCADE,
    #     related_name='scheme_transactions'
    # )

    # customer = models.ForeignKey(
    #     'Customer',
    #     on_delete=models.CASCADE
    # )

    customer = models.ForeignKey(
    AccountDetails,
    on_delete=models.CASCADE,
    related_name="scheme_transactions"
    )

    scheme = models.ForeignKey(
    'Scheme',
    on_delete=models.PROTECT,
    null=True,
    blank=True,
    related_name='scheme_transactions'
    )

    # enrollment = models.ForeignKey(
    #     'CustomerSchemeEnrollment',
    #     on_delete=models.CASCADE
    # )


    enrollment = models.ForeignKey(
    'CustomerSchemeEnrollment',
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name='scheme_transactions'
    )

    installment = models.ForeignKey(
        'SchemeInstallment',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='scheme_transactions'
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    razorpay_order_id = models.CharField(
        max_length=255,
        unique=True
    )

    razorpay_payment_id = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    razorpay_signature = models.TextField(
        blank=True,
        null=True
    )

    payment_method = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    remarks = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.razorpay_order_id