from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='invoicingHome'),
    path('customerInvoicing/', views.customerInvoicing, name='customerInvoicing'),
    path('customerInvoicingShow-<int:id>', views.customerInvoicingShow, name='customerInvoicingShow'),
    path('customerInvoicingAccounting-<int:idInvoice>', views.customerInvoicingAccounting, name='customerInvoicingAccounting'),
    path('addCustomerPayment-<int:idInvoice>', views.addCustomerPayment, name='addCustomerPayment'),
    path('delCustomerInvoicingItem-<int:idInvoice>-<int:idItem>', views.delCustomerInvoicingItem, name='delCustomerInvoicingItem'),

    path('providerInvoicing/', views.providerInvoicing, name='providerInvoicing'),
    path('providerInvoicingShow-<int:id>', views.providerInvoicingShow, name='providerInvoicingShow'),
    path('providerInvoicingAccounting-<int:idInvoice>', views.providerInvoicingAccounting, name='providerInvoicingAccounting'),
    path('addProviderPayment-<int:idInvoice>', views.addProviderPayment, name='addProviderPayment'),
    path('delProviderInvoicingItem-<int:idInvoice>-<int:idItem>', views.delProviderInvoicingItem, name='delProviderInvoicingItem'),

]
