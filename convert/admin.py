from django.contrib import admin
from .models import UnitConverter

@admin.register(UnitConverter)
class UnitConverterAdmin(admin.ModelAdmin):
    pass
