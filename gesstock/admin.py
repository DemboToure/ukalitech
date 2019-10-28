from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Provider)
admin.site.register(Customer)
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Procurement)
admin.site.register(ProcurementItem)
admin.site.register(Delivery)
admin.site.register(DeliveryItem)
