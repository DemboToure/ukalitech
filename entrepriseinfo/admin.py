from django.contrib import admin
from .models import *
# Register your models here.

class EntrepriseAdmin(admin.ModelAdmin):
    list_display   = ('name', 'entreprise_type','adress', 'contact', 'contact_2', 'ninea_number')



admin.site.register(EntrepriseInfo, EntrepriseAdmin)
