# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
