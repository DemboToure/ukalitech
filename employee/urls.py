from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_home, name='employeeHome'),
    path('addEmployee/', views.employee_add, name='employeeAdd'),
    path('showEmployee-<int:id>', views.employee_show, name='employeeShow'), 
    path('editEmployee-<int:id>', views.employee_edit, name='employeeEdit'),    
    path('gestionPost', views.gestion_post, name='gestionPost'),    
    path('contractAdd-<int:id>', views.contract_add, name='contractAdd'),    
]
