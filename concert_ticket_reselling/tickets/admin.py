from django.contrib import admin
from .models import AdminSettings

# Register your models here.
@admin.register(AdminSettings)
class AdminSettingsAdmin(admin.ModelAdmin):
    list_display = ('admin_whatsapp_number',)