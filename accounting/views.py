from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *
import xlrd 
from django.contrib.auth.decorators import login_required , user_passes_test
from django.core.files.storage import FileSystemStorage
import os
from ukalierp import settings
import time



# Create your views here.
@login_required(login_url='/website/login_user')
def accounting_home(request):

    return render(request, "accountingHome.html")


@login_required(login_url='/website/login_user')
def accounting_account(request):
    accounts = Account.objects.order_by('account_number')
    accountForm = AccountForm(request.POST or None)
    if accountForm.is_valid():
        accountForm.save()
        return redirect('accountingAccount')
    return render(request, "accountingAccount.html", locals())


@login_required(login_url='/website/login_user')
def accounting_import(request):

    if request.method == 'POST':
        myFile = request.FILES['excelfile'] 
        fs = FileSystemStorage()
        filename = fs.save(myFile.name, myFile)
        uploaded_file_url = fs.url(filename)
        name, ext = myFile.name.split('.')
        time.sleep(2)
        if ext == "xlsx":
            print("format matched")
            data = xlrd.open_workbook('uploads/'+myFile.name)
            sh = data.sheet_by_name('Sheet1')
            for row in range(1, sh.nrows):
                tab = sh.row_values(row)
                account = Account()
                account.account_number = tab[0]
                account.label = tab[1] 
                account.account_type = tab[2]
                account.save()

            filepath = os.path.join(settings.MEDIA_ROOT, myFile.name)
            os.remove(filepath)
            messages.success(request, "Import effectué avec succe" )
        else:
            messages.warning(request, "Une erreur c'est produite lors de l'importation format non adequat" )            
    else:
        messages.warning(request, "Aucun fichier importé " )            
    return redirect('accountingAccount')



@login_required(login_url='/website/login_user')
def accounting_journal(request):
    operations = Operation.objects.order_by('-created_at')
    if request.method == 'POST' :
        operationForm = OperationForm(request.POST, request.FILES)
        if operationForm.is_valid(): 
            operationForm.save()
            messages.success(request, "Operation enregistrée avec success" )
            return redirect("accountingJournal")
        else:
            messages.success(request, "Operation enregistrée avec success {}".format(operationForm.errors) )


    operationForm = OperationForm()    
    return render(request, "accountingJournal.html", locals())



@login_required(login_url='/website/login_user')
def accounting_book(request):

    accounts = Account.objects.all() 

    return render(request, "accountingBook.html", locals())


@login_required(login_url='/website/login_user')
def accounting_bilan(request):

    accounts = Account.objects.all() 

    return render(request, "accountingBilan.html", locals())



@login_required(login_url='/website/login_user')
def accounting_balance(request):

    accounts = Account.objects.order_by('account_number') 
    total_credit = sum( [ ac.get_total_credit() for ac in accounts ] )
    total_debit  = sum( [ ac.get_total_debit() for ac in accounts ] )

    return render(request, "accountingBalance.html", locals())


@login_required(login_url='/website/login_user')
def accounting_result(request):

    return render(request, "accountingResult.html", locals())
