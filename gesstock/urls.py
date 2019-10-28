from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='gesstockHome'),
    path('provider/', views.provider, name='gesstockProvider'),
    path('customer/', views.customer, name='gesstockCustomer'),
    path('article/', views.article, name='gesstockArticle'),
    path('procurement/', views.procurement, name='gesstockProcurement'),
    path('delivery/', views.delivery, name='gesstockDelivery'),

    path('deliveryShow-<int:id>', views.deliveryShow, name='gesstockDeliveryShow'),
    path('providerShow-<int:id>', views.providerShow, name='gesstockProviderShow'),
    path('customerShow-<int:id>', views.customerShow, name='gesstockCustomerShow'),
    path('articleShow-<int:id>', views.articleShow, name='gesstockArticleShow'),
    path('procurementShow-<int:id>', views.procurementShow, name='gesstockProcurementShow'),
    path('delProcurementItem-<int:id>-<int:idp>', views.delProcurementItem, name='delProcurementItem'),
    path('delDeliveryItem-<int:id>-<int:idd>', views.delDeliveryItem, name='delDeliveryItem'),
]
