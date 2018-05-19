from django.contrib import admin
import os

# Register your models here.
from .fill_form_watermark import makePDF

from .models import PersonToRegister

def populatePDF(modelAdmin, request, queryset):
    peopleToRegister = queryset.values()
    for person in peopleToRegister:
        if os.path.exists('overlay_PDF.pdf'):
            print('euruka')
            os.remove('overlay_PDF.pdf')
        makePDF(person)

# class VehicleAdmin(admin.ModelAdmin):
#     list_display = ['v_vin', 'v_make', 'v_model']
#     ordering = ['v_date_last_changed']
#     actions = [populatePDF]


class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'middle_name']
    ordering = ['last_name']
    actions = [populatePDF]


admin.site.register(PersonToRegister, PersonAdmin)
