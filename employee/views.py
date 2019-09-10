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
from django.contrib import messages
from datetime import datetime


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
    try:
        employee = Employee.objects.get(id=id)
    except:
        return redirect("employeeHome")

    form = ContractForm()
    formDiploma = DiplomaForm()
    formExperience = ExperienceForm()

    contracts = employee.contract_set.all()
    salarys    = employee.salary_set.all()
    print( type(salarys) )
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

    if request.method == 'POST' :
        if 'bulletin' in request.POST:
            desi = SalaryDesignation()
            desi.label = request.POST['designation']
            desi.code = request.POST['code']
            desi.save() 
            return redirect('gestionPost')


    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('gestionPost')

    posts = Post.objects.all()
    salary_designation = SalaryDesignation.objects.all()
    salary = SalaryDesignationForm()
    return render(request, 'gestionPost.html', locals())


@login_required(login_url='/website/login_user')
def add_salary_designation(request):
    
    salary = SalaryDesignationForm(request.POST or None)
    if salary.is_valid():
        salary.save()

    return redirect('gestionPost')

@login_required(login_url='/website/login_user')
def contract_add(request, id):
    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
       
    return redirect('employeeShow', id)


@login_required(login_url='/website/login_user')
def show_salary(request, idEmp, id):
    try:
        emp = Employee.objects.get(id=idEmp)
    except:
        return redirect("employeeHome")

    salary = Salary.objects.get(id=id)


    return render(request, 'salaryshow.html', locals())




@login_required(login_url='/website/login_user')
def del_salary(request, idEmp, id):
    salary = Salary.objects.get(id=id)
    
    for item in salary.salaryitems_set.all() :
        item.delete()
    salary.delete()
    
    return redirect('employeeShow', idEmp)

@login_required(login_url='/website/login_user')
def add_salary(request, id):
    try:
        emp = Employee.objects.get(id=id)
    except:
        return redirect("employeeHome")
    if request.method == 'POST':
        print(request.POST)
        salary_desig = SalaryDesignation.objects.all()
        salary = Salary()
        salary.employee = emp
        salary.salary_period = request.POST['month']
        salary.save()
        for sdg in salary_desig:
            keys = sdg.__dict__.keys()
            keys = [ k for k in keys ]
            keys.remove('code')
            keys.remove('label')
            keys.remove('_state')
            keys.remove('id')
            item = SalaryItems()
            item.code =  sdg.code
            item.label=  sdg.label
            item.salary = salary 
            for k in keys:
                item.setAttr(k, request.POST['-'.join([str(sdg.code), k])] )
                #print("{} : {}".format('-'.join([str(sdg.code), k]), request.POST['-'.join([str(sdg.code), k])]) )

            item.save()
        messages.success(request, "Bulletin de salaire generer avec succes!" )
        return redirect('employeeShow', id)
    
    now = datetime.now().strftime('%d/%m/%Y %H:%M:%S') 
    salary_desig = SalaryDesignation.objects.all()
    return render(request, 'salaryAdd.html', locals())

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
    