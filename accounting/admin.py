from django.contrib import admin
from .models import *
# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display   = ('label', 'account_number','created_at' )

class OperationAdmin(admin.ModelAdmin):
    list_display   = ('label', 'solde','type_operation' )



admin.site.register(Account, AccountAdmin)
admin.site.register(Operation, OperationAdmin)
