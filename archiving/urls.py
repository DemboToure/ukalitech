from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='archivingHome'),
    path('showFolder-<int:id>', views.showFolder, name='showFolder'), 

]
