from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required , user_passes_test
from .forms import *
from .models import *
from django.contrib import messages

# Create your views here.

@login_required(login_url='/website/login_user')
def home(request):

    return render(request, 'gesstock.html')


@login_required(login_url='/website/login_user')
def provider(request):
    if request.method == 'POST':
        form = ProviderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Fournisseur enregistré avec succé" )            
            return redirect('gesstockProvider')
        else:
            messages.success(request, "une erreur c'est produit lors de l'enregistrement" )            
    else:
        form = ProviderForm()
        providers = Provider.objects.all()

    return render(request, 'provider.html', locals())

@login_required(login_url='/website/login_user')
def providerShow(request, id):
    provider = Provider.objects.get(id=id)
    providerForm = ProviderForm(instance=provider)
    
    if request.method == "POST":
        if 'updateProvider' in request.POST:
            providerForm = ProviderForm(request.POST, instance=provider) 
            if providerForm.is_valid():
                providerForm.save()
                messages.success(request, "fourisseur modifier avec succé" )            
                return redirect('gesstockProviderShow', id)
        
    
    return render(request, 'providerShow.html', locals())

@login_required(login_url='/website/login_user')
def customer(request):
    if request.method == 'POST':
        customerForm = CustomerForm(request.POST, request.FILES)
        if customerForm.is_valid():
            customerForm.save()
            messages.success(request, "Client enregistré avec succé" )            
            return redirect('gesstockCustomer')
        else:
            messages.warning(request, "une erreur c'est produit lors de l'enregistrement du client")
    else:
        customers = Customer.objects.all()
        customerForm = CustomerForm()

    return render(request, 'customer.html', locals())

@login_required(login_url='/website/login_user')
def customerShow(request, id):
    customer = Customer.objects.get(id=id)
    customerForm = CustomerForm(instance=customer) 
    if request.method == "POST":
        if 'updateCustomer' in request.POST:
            customerForm = ProviderForm(request.POST, instance=customer) 
            if customerForm.is_valid():
                customerForm.save()
                messages.success(request, "Client modifier avec succé" )            
                return redirect('gesstockCustomerShow', id)
    
    return render(request, 'customerShow.html', locals())


@login_required(login_url='/website/login_user')
def article(request):

    if request.method == 'POST':
        if 'addArticle' in request.POST:
            articleForm = ArticleForm(request.POST)
            if articleForm.is_valid():
                articleForm.save()
                messages.success(request, "Article enregistrer avec succé" )
                return redirect('gesstockArticle')            
            else:
                messages.warning(request, "echec de l'enregistrement de l'article {}".format(articleForm.errors) )
        elif 'addCategory' in request.POST:
            categoryForm = CategoryForm(request.POST)
            if categoryForm.is_valid():
                categoryForm.save()
                messages.success(request, "Categorie enregistre avec succé")
                return redirect('gesstockArticle')
            else:
                messages.warning(request, "echec de l'enregistrement")         
    
    articles = Article.objects.all()
    articleForm = ArticleForm()

    categorys = Category.objects.all()
    categoryForm = CategoryForm()

    return render(request, 'article.html', locals())

@login_required(login_url='/website/login_user')
def articleShow(request, id):
    article = Article.objects.get(id=id)
    articleForm = ArticleForm(instance=article)
    if request.method == "POST":
        if 'updateArticle' in request.POST:
            articleForm = ArticleForm(request.POST, instance=article) 
            if articleForm.is_valid():
                print(articleForm)
                articleForm.save()
                messages.success(request, "Article modifié avec succé" )            
                return redirect('gesstockArticleShow', id)
            else:   
                messages.warning(request, "echec de la modification {}".format(articleForm.errors) )

    
    return render(request, 'articleShow.html', locals())



@login_required(login_url='/website/login_user')
def procurement(request):
    
    procurements = Procurement.objects.all()
    procurementForm = ProcurementForm()
    if request.method == 'POST':
        procurementForm = ProcurementForm(request.POST)
        if procurementForm.is_valid():
            procurementForm.save()
            return redirect('gesstockProcurement')



    return render(request, 'procurement.html', locals())

@login_required(login_url='/website/login_user')
def procurementShow(request, id):
    procurement = Procurement.objects.get(id=id)
    procurementForm = ProcurementForm(instance=procurement)  
    
    procurementItemForm = ProcurementItemForm()  

    if request.method == "POST":
        if 'updateProcurement' in request.POST:
            procurementForm = ProcurementForm(request.POST, instance=procurement) 
            if procurementForm.is_valid():
                procurementForm.save()
                procurement = Procurement.objects.get(id=id)
                if procurement.received == True:
                    for item in procurement.procurementitem_set.all():
                        art = Article.objects.get(id=item.article.id)
                        art.quantity += item.quantity
                        art.save()
                    messages.success(request, "Stock approvisionné" )
                messages.success(request, "Approvisionnement modifié avec succé" )            
                return redirect('gesstockProcurementShow', id)
            else:
                messages.success(request, "echec de la modification" )
        elif 'addItem' in request.POST:
            print(request.POST['quantity'])
            art = Article.objects.get(id=request.POST['article'])
            item = ProcurementItem()
            item.article     = art
            item.quantity    = request.POST['quantity'] 
            item.procurement = procurement
            item.save()
            return redirect('gesstockProcurementShow', id)

    
    return render(request, 'procurementShow.html', locals())

@login_required(login_url='/website/login_user')
def delProcurementItem(request, id, idp):
    procurement = Procurement.objects.get(id=idp)
    if procurement.received != True:
        item = ProcurementItem.objects.get(id=id)
        item.delete()
    return redirect('gesstockProcurementShow', idp)
    

@login_required(login_url='/website/login_user')
def delivery(request):

    deliverys = Delivery.objects.all()
    deliveryForm = DeliveryForm()
    if request.method == 'POST':
        deliveryForm = DeliveryForm(request.POST)
        if deliveryForm.is_valid:
            deliveryForm.save()
            return redirect('gesstockDelivery')
    return render(request, 'delivery.html', locals())


@login_required(login_url='/website/login_user')
def deliveryShow(request, id):
    delivery = Delivery.objects.get(id=id)
    deliveryForm = DeliveryForm(instance=delivery)  
    
    deliveryItemForm = DeliveryItemForm()  

    if request.method == "POST":
        if 'updateDelivery' in request.POST:
            deliveryForm = DeliveryForm(request.POST, instance=delivery) 
            if deliveryForm.is_valid():
                deliveryForm.save()
                delivery = Delivery.objects.get(id=id)
                if delivery.delivered == True:
                    for item in delivery.deliveryitem_set.all():
                        art = Article.objects.get(id=item.article.id)
                        art.quantity -= item.quantity
                        art.save()
                    messages.success(request, "Livraison effectué" )
                messages.success(request, "Livraison modifié avec succé" )            
                return redirect('gesstockDeliveryShow', id)
            else:
                messages.success(request, "echec de la modification" )
        elif 'addItem' in request.POST:
            art = Article.objects.get(id=request.POST['article'])
            item = DeliveryItem()
            item.article     = art
            item.quantity    = request.POST['quantity'] 
            item.delivery    = delivery
            item.save()
            return redirect('gesstockDeliveryShow', id)

    
    return render(request, 'deliveryShow.html', locals())

@login_required(login_url='/website/login_user')
def delDeliveryItem(request, id, idd):
    delivery = Delivery.objects.get(id=idd)
    if delivery.delivered != True:
        item = DeliveryItem.objects.get(id=id)
        item.delete()

    return redirect('gesstockDeliveryShow', idd)
    

