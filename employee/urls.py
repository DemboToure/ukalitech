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
    path('addSalary-<int:id>', views.add_salary, name='addSalary'),
    path('addSalary-<int:id>-<int:idSalary>/', views.add_salary, name='addSalary'),
    path('showSalary-<int:idEmp>-<int:id>/', views.show_salary, name='showSalary'),
    path('delSalary-<int:idEmp>-<int:id>/', views.del_salary, name='delSalary'),
    path('closeSalary-<int:idEmp>-<int:idSalary>/', views.close_salary, name='closeSalary'),
    path('duplicateSalary-<int:idEmp>-<int:idSalary>/', views.duplicate_salary, name='duplicateSalary'),
    path('addSalaryDesignation/', views.add_salary_designation, name='addSalaryDesignation'),
]
