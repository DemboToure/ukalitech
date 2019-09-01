from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_home, name='employeeHome'),
    path('addEmployee/', views.employee_add, name='employeeAdd'),
    path('showEmployee-<int:id>', views.employee_show, name='employeeShow'), 
    path('editEmployee-<int:id>', views.employee_edit, name='employeeEdit'),    
    path('gestionPost', views.gestion_post, name='gestionPost'),    
    path('contractAdd-<int:id>', views.contract_add, name='contractAdd'),    
    path('diplomaAdd-<int:id>', views.diploma_add, name='diplomaAdd'),    
    path('experienceAdd-<int:id>', views.experience_add, name='experienceAdd'),    
    path('importEmp/', views.import_emp, name='importEmp'),
    path('addSalaryDesignation/', views.add_salary_designation, name='addSalaryDesignation'),
]
