from django.contrib import admin
import os

# Register your models here.
from .fill_form_watermark import makePDF

from .models import PersonToRegister

def populatePDF(modelAdmin, request, queryset):
    peopleToRegister = queryset.values()\

    for person in peopleToRegister:
        # PDF writer will throw errors if field values are null, as such these values must be converted to 'empty' strings
        for dataField in person:
            if (person[dataField] == None):
                person[dataField] = " "
        # Overlay pdf must be dumped at the beginnning of each iteration to prevent same info from being copied
        if os.path.exists('overlay_PDF.pdf'):
            os.remove('overlay_PDF.pdf')
        makePDF(person)



class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'middle_name']
    ordering = ['last_name']
    actions = [populatePDF]


admin.site.register(PersonToRegister, PersonAdmin)
