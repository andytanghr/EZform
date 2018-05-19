from django.db import models

# Create your models here.
# class PollsVehicle(models.Model):
#     v_date_added = models.DateField()
#     v_date_last_changed = models.DateField()
#     v_vin = models.CharField(max_length=17, blank=True, null=True)
#     v_year = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
#     v_make = models.CharField(max_length=200, blank=True, null=True)
#     v_body_style = models.CharField(max_length=200, blank=True, null=True)
#     v_model = models.CharField(max_length=200, blank=True, null=True)
#     v_purchased_from_name = models.CharField(max_length=200, blank=True, null=True)
#     v_purchased_from_city = models.CharField(max_length=200, blank=True, null=True)
#     v_purchased_from_state = models.CharField(max_length=200, blank=True, null=True)
#     v_odometer_reading = models.IntegerField(blank=True, null=True)
#     v_purchase_date = models.DateField(blank=True, null=True)
#     v_purchase_price_usd = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
#     v_plate_number = models.CharField(max_length=8, blank=True, null=True)
#     v_empty_weight = models.IntegerField(blank=True, null=True)
#     v_lienholder_name_first = models.CharField(max_length=200, blank=True, null=True)
#     v_seller_signature = models.CharField(max_length=200, blank=True, null=True)
#     v_bond_request_explanation = models.TextField(blank=True, null=True)
#     v_flag_last_titled_in_tx = models.NullBooleanField()
#     v_flag_abandoned = models.NullBooleanField()
#     v_flag_subject_to_charges = models.NullBooleanField()
#     v_flag_subject_to_lien = models.NullBooleanField()
#     v_flag_nonrepairable = models.NullBooleanField()
#     v_flag_salvage = models.NullBooleanField()
#     v_flag_pending_lawsuits = models.NullBooleanField()
#     v_flag_legal_posession = models.NullBooleanField()
#     v_flag_legal_control = models.NullBooleanField()
#     v_flag_manufactured_us = models.NullBooleanField()
#     v_flag_assembled = models.NullBooleanField()
#     v_flag_complete = models.NullBooleanField()
#     v_flag_25_or_older = models.NullBooleanField()
#     v_flag_no_plates = models.CharField(max_length=200, blank=True, null=True)
#     # customer = models.ForeignKey('PollsCustomer', models.DO_NOTHING, db_column='Customer_id')  # Field name made lowercase.
#
#     class Meta:
#         managed = True
#         db_table = 'polls_vehicle'

class PersonToRegister(models.Model):
    last_name = models.CharField(max_length=200, blank=True, null=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    middle_name = models.CharField(max_length=200, blank=True, null=True)
    suffix = models.CharField(max_length=10, blank=True, null=True)
    maiden_name = models.CharField(max_length=200, blank=True, null=True)
    birth_month = models.PositiveIntegerField(blank=True, null=True)
    birthday = models.PositiveIntegerField(blank=True, null=True)
    birth_year = models.PositiveIntegerField(blank=True, null=True)
    SSN1 = models.CharField(max_length=3, blank=True, null=True)
    SSN2 = models.CharField(max_length=2, blank=True, null=True)
    SSN3 = models.CharField(max_length=4, blank=True, null=True)
