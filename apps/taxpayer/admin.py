from django.contrib import admin

from apps.taxpayer.models import Taxpayer
from billing.admin import TESTLUISSite


# Register your models here.
@admin.register(Taxpayer, site=TESTLUISSite)
class TaxpayerAdmin(admin.ModelAdmin):
    list_display = ["identification", "full_name"]
    search_fields = ["identification", "full_name"]
