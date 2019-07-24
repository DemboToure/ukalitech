from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.utils import timezone
from django.contrib.auth.decorators import login_required , user_passes_test


# Create your views here.
@login_required(login_url='/website/login_user')
def employee_home(request):
    employee = Employee.objects.all() 

    return render(request, 'employeeHome.html', locals())


@login_required(login_url='/website/login_user')
def employee_add(request):
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return redirect('employeeHome')
    else:
        form = EmployeeForm()
    
    return render(request, 'employeeAdd.html', locals())


@login_required(login_url='/website/login_user')
def employee_show(request, id):
    employee = Employee.objects.get(id=id)
    form = ContractForm()
    return render(request, 'employeeShow.html', locals())


@login_required(login_url='/website/login_user')
def employee_edit(request, id):
    employee = Employee.objects.get(id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES , instance = employee)
        if form.is_valid():
            form.save()
            return redirect('employeeShow', id)
    else:
        form = EmployeeForm(instance = employee)

    return render(request, 'employeeEdit.html', locals())


@login_required(login_url='/website/login_user')
def gestion_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('gestionPost')

    posts = Post.objects.all() 
    return render(request, 'gestionPost.html', locals())

@login_required(login_url='/website/login_user')
def contract_add(request, idEmployee):

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return redirect('EmployeeShow', idEmployee)
    