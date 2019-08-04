from django.shortcuts import render, redirect
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
    operations = Operation.objects.all()
    if request.method == 'POST' :
        operationForm = OperationForm(request.POST, request.FILES)
        if operationForm.is_valid(): 
            operationForm.save()
            return redirect("accountingJournal")
    operationForm = OperationForm()    
    return render(request, "accountingJournal.html", locals())

def accounting_book(request):

    return render(request, "accountingBook.html")

