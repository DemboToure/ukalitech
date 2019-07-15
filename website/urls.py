from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home') ,
    path('login_user', views.login_user, name='login_user'), 
    path('logout_user', views.logout_user, name='logout_user'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('applications', views.applications, name='applications'),
]
