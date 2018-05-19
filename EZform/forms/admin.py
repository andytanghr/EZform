from django.contrib import admin
import os

# Register your models here.
from .fill_form_watermark import makePDF

from .models import PollsVehicle

def populatePDF(modelAdmin, request, queryset):
    people = queryset.values()
    for person in people:
        print(person['person_name'])
        if os.path.exists('overlay_PDF.pdf'):
            print('euruka')
            os.remove('overlay_PDF.pdf')
        makePDF(person)

class VehicleAdmin(admin.ModelAdmin):
    list_display = ['v_vin', 'v_make', 'v_model']
    ordering = ['v_date_last_changed']
    actions = [populatePDF]

print('rawer')
admin.site.register(PollsVehicle, VehicleAdmin)
