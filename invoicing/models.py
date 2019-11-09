from django.db import models
from gesstock.models import Provider, Customer, Article
from django.contrib.auth.models import User
#from django.http import request

# Create your models here.

class Invoice(models.Model):

    number          = models.CharField(max_length=20)
    created_at      = models.DateTimeField(auto_now=True)
    document        = models.FileField(upload_to='invoicing/',blank=True, null=True)
    dateline        = models.DateField()
    accounting      = models.BooleanField(default=False)

    user            = models.ForeignKey(User, on_delete=models.PROTECT)
    provider        = models.ForeignKey(Provider, on_delete=models.PROTECT, null=True, blank=True)
    customer        = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True, blank=True)


    def __str__(self):
        if self.provider != None:
            return "Facture {}".format(self.provider.label)
        else:
            return "Facture {}".format(self.customer.label)
    
    # return the solde without tva 
    def pretaxAmount(self):
        amount = 0 
        for item in self.invoiceitem_set.all():
            amount += item.computeSolde()
        return amount 
    
    # return the TVA solde only
    def tvaAmount(self):
        amount = 0 
        for item in self.invoiceitem_set.all():
            amount += item.computeTva()
        return amount 
    
    # return the total solde tva+localAmount 
    def totalAmount(self):
        return self.pretaxAmount()+self.tvaAmount() 

    # return the total that are peyed by client
    def totalPay(self):
        amount = 0 
        for item in self.invoicepay_set.all():
            amount += item.amount
        return amount 

    # return the remining solde that client must pay 
    def remainingPay(self):
        return self.totalAmount() - self.totalPay()

    # true if total solde is payed else false
    def isPayed(self):
        return True if self.remainingPay() <= 0 else False


class InvoiceItem(models.Model):

    article     = models.ForeignKey(Article, on_delete=models.PROTECT, null=True, blank=True)
    label       = models.CharField(max_length=50) 
    quantity    = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price       = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tva         = models.IntegerField(default=18)

    invoice     = models.ForeignKey("Invoice", on_delete=models.PROTECT)


    def __str__(self):
        return "{} -- {}".format(self.article.label, self.invoice.number)

    # return Solde without tva
    def computeSolde(self):
        return round(self.quantity*self.price, 2)
    
    # return TVA solde
    def computeTva(self):
        return (self.tva*self.computeSolde())/100


    
class InvoicePay(models.Model):

    amount              = models.DecimalField(max_digits=10, decimal_places=2)
    means_of_payment    = models.CharField(max_length=10, choices=[('CASH','CASH'), ('BANK','BANK')])
    created_at          = models.DateTimeField(auto_now=True)

    document            = models.FileField(upload_to='invoicing/',blank=True, null=True)

    invoice             = models.ForeignKey("Invoice", on_delete=models.PROTECT)


    def __str__(self):
        return "{} -- {}".format(self.amount, self.invoice.number)


