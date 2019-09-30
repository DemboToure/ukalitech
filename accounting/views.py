from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *
# Create your views here.

def accounting_home(request):

    return render(request, "accountingHome.html")

def accounting_account(request):
    accounts = Account.objects.all()
    accountForm = AccountForm(request.POST or None)
    if accountForm.is_valid():
        accountForm.save()
        return redirect('accountingAccount')
    return render(request, "accountingAccount.html", locals())


def accounting_journal(request):
    operations = Operation.objects.order_by('-created_at')
    if request.method == 'POST' :
        operationForm = OperationForm(request.POST, request.FILES)
        if operationForm.is_valid(): 
            operationForm.save()
            messages.success(request, "Operation enregistrée avec success" )
            return redirect("accountingJournal")
    operationForm = OperationForm()    
    return render(request, "accountingJournal.html", locals())

def accounting_book(request):

    accounts = Account.objects.all() 

    return render(request, "accountingBook.html", locals())

def accounting_bilan(request):

    accounts = Account.objects.all() 

    return render(request, "accountingBilan.html", locals())


def accounting_balance(request):

    accounts = Account.objects.order_by('account_number') 
    total_credit = sum( [ ac.get_total_credit() for ac in accounts ] )
    total_debit  = sum( [ ac.get_total_debit() for ac in accounts ] )

    return render(request, "accountingBalance.html", locals())

def accounting_result(request):


    return render(request, "accountingResult.html", locals())
