from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required , user_passes_test
from .models import *
from .forms import *
from entrepriseinfo.models import EntrepriseInfo
from accounting.models import Account, Operation
from django.contrib import messages

from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
from django.conf import settings 


# Create your views here.
@login_required(login_url='/website/login_user')
def home(request):
    invoices = Invoice.objects.filter(accounting=False).order_by("-created_at")
    
    return render(request, 'invoicing.html', locals())



"""
# Generate PDF of invoicing client or provider
"""

@login_required(login_url='/website/login_user')
def generateInvoicePDF(request, id):
    """Generate pdf."""
    # Model data
    invoice = Invoice.objects.get(id=id)
    entreprise = EntrepriseInfo.objects.all()[0]

    # Rendered
    html_string = render_to_string('pdf.html', {'invoice': invoice, 'entrepriseinfo':entreprise })
    html = HTML(string=html_string)
    result = html.write_pdf(stylesheets=[settings.BASE_DIR + '/static/css/invoice.css',])

    # Creating http response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=facture.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        out = output.read()
        response.write(out)

    return response


"""
# functions that impact on client sheduling 
"""

# display the list of customer invoices 
@login_required(login_url='/website/login_user')
def customerInvoicing(request):

    if request.method == "POST":
        invoiceForm = InvoiceForm(request.POST)
        if invoiceForm.is_valid():
            invoiceForm.save()
            messages.success(request, "facture enregistré avec succés")
        else:
            messages.warning(request, "facture non valide {}".format(invoiceForm.errors))


    invoices = Invoice.objects.filter(provider=None).order_by('-created_at')
    invoiceForm = InvoiceForm()
    currentUserId = request.user.id
    
    return render(request, 'customerInvoicing.html', locals())

# display one invoice end his details for adding items end other operations 
@login_required(login_url='/website/login_user')
def customerInvoicingShow(request, id):

    invoice = Invoice.objects.get(id=id)
    itemForm = InvoiceItemForm() 
    invoicePayForm = InvoicePayForm()
    if request.method == "POST":
        invoiceItem = InvoiceItem()
        try:
            acc = Account.objects.get(id=request.POST['account'])
            invoiceItem.account = acc
        except:
            print("no account selected")
            
        try:
            art = Article.objects.get(id=request.POST['article'])

            invoiceItem.article = art
        except:
            print("no article selected")
        try:
            invoiceItem.invoice = invoice
            invoiceItem.label   = request.POST['label']
            invoiceItem.quantity= request.POST['quantity']
            invoiceItem.price   = request.POST['price']
            invoiceItem.tva     = request.POST['tva']
            invoiceItem.save()
        except:
            messages.warning(request, "une erreur s'est produite lors de l'enregistrement veuillez contacter l'admin si ça persiste")


        return redirect('customerInvoicingShow', id)

    return render(request, 'customerInvoicingShow.html', locals())

# del an item in one invoice
@login_required(login_url='/website/login_user')
def delCustomerInvoicingItem(request, idInvoice, idItem):

    try:
        invoiceItem = InvoiceItem.objects.get(id=idItem)
        invoiceItem.delete()
    except:
        print("item n'existe pas")
    
    return redirect('customerInvoicingShow', idInvoice)

# for adding one payment for ane customer invoice
@login_required(login_url='/website/login_user')
def addCustomerPayment(request, idInvoice):
    invoice = Invoice.objects.get(id=idInvoice)
    if request.method == 'POST':
        invoicePayForm = InvoicePayForm(request.POST, request.FILES)
        if invoicePayForm.is_valid():
            pay = invoicePayForm.save()
            # triger a debit operation on a client account 
            clientAccount = Account.objects.get(account_number=411)
            opCreditClient = Operation()
            opCreditClient.label = "reglement client {}".format(invoice.number)
            opCreditClient.solde = pay.amount
            opCreditClient.type_operation = "credit"
            opCreditClient.account = clientAccount
            opCreditClient.customer= invoice.customer
            if pay.document is not None:
                opCreditClient.document = pay.document
            opCreditClient.save()   


            # triger a debit operation on a cash or bank account  
            if pay.means_of_payment == "CASH":
                paymentMeanAccount = Account.objects.get(account_number=571)
            else:
                paymentMeanAccount = Account.objects.get(account_number=501)
            opDebitMean = Operation()
            opDebitMean.label = "paiement client {}".format(invoice.number)
            opDebitMean.solde = pay.amount 
            opDebitMean.type_operation = "DEBIT" 
            opDebitMean.account = paymentMeanAccount
            opDebitMean.customer= invoice.customer
            if pay.document is not None:
                opDebitMean.document = pay.document
            opDebitMean.save()

            messages.success(request, "paiement ajouté avec succées")
        else:
            messages.warning(request, "echec de l'ajout du paiement")
    return redirect('customerInvoicingShow', idInvoice)


# for accounting one invoice 
@login_required(login_url='/website/login_user')
def customerInvoicingAccounting(request, idInvoice):
    
    try:
        invoice = Invoice.objects.get(id=idInvoice)
        invoice.accounting = True 
        invoice.save()
        # traitement des transactions dans la comptabilité a faire
        clientAccount = Account.objects.get(account_number=411)
        opDebitClient = Operation()
        opDebitClient.label = invoice.number
        opDebitClient.solde = invoice.totalAmount()
        opDebitClient.type_operation = "DEBIT"
        opDebitClient.account = clientAccount
        opDebitClient.customer= invoice.customer
        opDebitClient.save()

        for item in invoice.invoiceitem_set.all():
            productAccount = Account.objects.get(account_number=item.account.account_number)
            opCreditVente = Operation()
            opCreditVente.label = "facture {}".format(invoice.customer.label)
            opCreditVente.solde = item.computeSolde()
            opCreditVente.type_operation = "credit"
            opCreditVente.account = productAccount
            opCreditVente.customer= invoice.customer
            opCreditVente.save()

        tvaAccount = Account.objects.get(account_number=443)
        opCreditTva = Operation()
        opCreditTva.label = "retenue TVA"
        opCreditTva.solde = invoice.tvaAmount()
        opCreditTva.type_operation = "credit"
        opCreditTva.account = tvaAccount
        opCreditTva.customer= invoice.customer
        opCreditTva.save()

        messages.success(request,"Comptabilisé avec succees")


    except:
        messages.warning(request, "facture non trouvé")

    return redirect('customerInvoicingShow', idInvoice)



"""
# functions that impact on a provider sheduling 
"""


@login_required(login_url='/website/login_user')
def providerInvoicing(request):

    if request.method == "POST":
        invoiceForm = InvoiceForm(request.POST)
        if invoiceForm.is_valid():
            invoiceForm.save()
            messages.success(request, "facture enregistré avec succés")
        else:
            messages.warning(request, "facture non valide {}".format(invoiceForm.errors))


    invoices = Invoice.objects.filter(customer=None).order_by('-created_at')
    invoiceForm = InvoiceForm() 
    currentUserId = request.user.id
    return render(request, 'providerInvoicing.html', locals())

# display one invoice end his details for adding items end other operations 
@login_required(login_url='/website/login_user')
def providerInvoicingShow(request, id):

    invoice = Invoice.objects.get(id=id)
    itemForm = InvoiceItemForm() 
    invoicePayForm = InvoicePayForm()
    if request.method == "POST":
        invoiceItem = InvoiceItem()
        try:
            acc = Account.objects.get(id=request.POST['account'])
            invoiceItem.account = acc
        except:
            print("no account selected")
            
        try:
            art = Article.objects.get(id=request.POST['article'])

            invoiceItem.article = art
        except:
            print("no article selected")
       
        try:
            invoiceItem.invoice = invoice
            invoiceItem.label   = request.POST['label']
            invoiceItem.quantity= request.POST['quantity']
            invoiceItem.price   = request.POST['price']
            invoiceItem.tva     = request.POST['tva']
            invoiceItem.save()
        except:
            messages.warning(request, "une erreur s'est produite lors de l'enregistrement veuillez contacter l'admin si ça persiste")


        return redirect('providerInvoicingShow', id)

    return render(request, 'providerInvoicingShow.html', locals())


# for accounting one provider invoice 
@login_required(login_url='/website/login_user')
def providerInvoicingAccounting(request, idInvoice):
    
    try:
        invoice = Invoice.objects.get(id=idInvoice)
        invoice.accounting = True 
        invoice.save()
        # traitement des transactions dans la comptabilité a faire
        for item in invoice.invoiceitem_set.all():
            chargeAccount = Account.objects.get(account_number=item.account.account_number)
            opDebitCharge = Operation()
            opDebitCharge.label = invoice.number 
            opDebitCharge.solde = item.computeSolde() 
            opDebitCharge.type_operation = "DEBIT" 
            opDebitCharge.account = chargeAccount 
            opDebitCharge.provider = invoice.provider 
            opDebitCharge.save() 

        tvaAccount = Account.objects.get(account_number=445)
        opDebitCharge = Operation()
        opDebitCharge.label = "TVA facture {}".format(invoice.number)
        opDebitCharge.solde = invoice.tvaAmount()
        opDebitCharge.type_operation = "DEBIT"
        opDebitCharge.account = tvaAccount
        opDebitCharge.provider = invoice.provider
        opDebitCharge.save()

        prividerAccount = Account.objects.get(account_number=401)
        opCreditTva = Operation()
        opCreditTva.label = "facture fournisseur {}".format(invoice.provider.label)
        opCreditTva.solde = invoice.totalAmount()
        opCreditTva.type_operation = "credit"
        opCreditTva.account = prividerAccount
        opCreditTva.provider= invoice.provider 
        opCreditTva.save()

        messages.success(request,"Comptabilisé avec succees")


    except:
        messages.warning(request, "facture non trouvé")

    return redirect('providerInvoicingShow', idInvoice)


# for adding one payment for ane customer invoice
@login_required(login_url='/website/login_user')
def addProviderPayment(request, idInvoice):
    invoice = Invoice.objects.get(id=idInvoice)
    if request.method == 'POST':
        invoicePayForm = InvoicePayForm(request.POST, request.FILES) 
        if invoicePayForm.is_valid():
            pay = invoicePayForm.save()
            # triger a debit operation on a client account 
            providerAccount = Account.objects.get(account_number=401)
            opDebitClient = Operation()
            opDebitClient.label = "reglement Fournisseur {}".format(invoice.number)
            opDebitClient.solde = pay.amount
            opDebitClient.type_operation = "DEBIT"
            opDebitClient.account = providerAccount
            opDebitClient.provider= invoice.provider
            if pay.document is not None:
                opDebitClient.document = pay.document
            opDebitClient.save()   


            # triger a debit operation on a cash or bank account  
            if pay.means_of_payment == "CASH":
                paymentMeanAccount = Account.objects.get(account_number=571)
            else:
                paymentMeanAccount = Account.objects.get(account_number=501)
            opCreditMean = Operation()
            opCreditMean.label = "reglement fournisseur {}".format(invoice.number)
            opCreditMean.solde = pay.amount 
            opCreditMean.type_operation = "credit" 
            opCreditMean.account = paymentMeanAccount
            opCreditMean.provider= invoice.provider
            if pay.document is not None:
                opCreditMean.document = pay.document
            opCreditMean.save()

            messages.success(request, "paiement ajouté avec succées")
        else:
            messages.warning(request, "echec de l'ajout du paiement")
    return redirect('providerInvoicingShow', idInvoice)

# del an item in one invoice
@login_required(login_url='/website/login_user')
def delProviderInvoicingItem(request, idInvoice, idItem):

    try:
        invoiceItem = InvoiceItem.objects.get(id=idItem)
        invoiceItem.delete()
    except:
        print("item n'existe pas")
    
    return redirect('providerInvoicingShow', idInvoice)
