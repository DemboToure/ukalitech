from django.urls import path
from . import views

urlpatterns = [
    path('', views.ged_home, name='gedHome'),
]
