from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.utils import timezone
from datetime import datetime, date
from django.contrib.auth.decorators import login_required , user_passes_test
from django.core.files.storage import FileSystemStorage
import xlrd
import os
from ukalierp import settings

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
    formDiploma = DiplomaForm()
    formExperience = ExperienceForm()

    contracts = employee.contract_set.all()
    curent_contract = None 
    if len( contracts ) > 0 :
        curent_contract = contracts[ len(contracts)-1 ]
        dt = datetime.combine(curent_contract.end, datetime.min.time())
        today = datetime.now()
        print(dt)
        print(today)
        if dt < today :
            curent_contract = None
    
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
def contract_add(request, id):
    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
       
    return redirect('employeeShow', id)
    
@login_required(login_url='/website/login_user')
def diploma_add(request, id):
    if request.method == 'POST':
        form = DiplomaForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
       
    return redirect('employeeShow', id)
    
@login_required(login_url='/website/login_user')
def experience_add(request, id):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
       
    return redirect('employeeShow', id)

@login_required(login_url='/website/login_user')
def import_emp(request):

    if request.method == 'POST':
        myFile = request.FILES['excelfile'] 
        fs = FileSystemStorage()
        filename = fs.save(myFile.name, myFile)
        uploaded_file_url = fs.url(filename)
        name, ext = myFile.name.split('.')
        if ext == "xlsx":
            print("format matched")
            data = xlrd.open_workbook('uploads/'+myFile.name)
            sh = data.sheet_by_name('Feuil1')
            for row in range(1, sh.nrows):
                tab = sh.row_values(row)
                dat = xlrd.xldate.xldate_as_datetime(tab[2], data.datemode)
                tab[2] = dat
                emp = Employee()
                emp.first_name   = tab[0]
                emp.last_name    = tab[1]
                emp.birth_date   = tab[2]
                emp.birth_to     = tab[3]
                emp.regis_number = round(tab[4])
                emp.cni          = round(tab[5])
                emp.save(tab)
                #print(emp)
                
            filepath = os.path.join(settings.MEDIA_ROOT, myFile.name)
            os.remove(filepath)
            return redirect('importEmp')
        else:
            print("format don't matched")
    return render(request, 'importEmp.html')
    