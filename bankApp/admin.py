from django.contrib import admin
from .models import Account
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Account)
class AccountAdmin(ImportExportModelAdmin):
    list_display = ('Identifier', 'name', 'balance', 'created_at')
    ordering = ('created_at',)