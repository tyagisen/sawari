from django.contrib import admin

from .models import Driver

@admin.register(Driver)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'vehicle_type']
