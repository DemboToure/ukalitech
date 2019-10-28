from django.db import models

# Create your models here.

class Provider(models.Model):

    label       = models.CharField(max_length=20)
    adress      = models.CharField(max_length=50, blank=True)
    tel         = models.CharField(max_length=20, blank=True)
    fix         = models.CharField(max_length=20, blank=True)
    created_at  = models.DateTimeField(auto_now=True)
    logo        = models.ImageField(upload_to='gesstock/', default='gesstock/provider-icon.png', blank=True)

    def __str__(self):
        return self.label


class Customer(models.Model):

    label       = models.CharField(max_length=20)
    adress      = models.CharField(max_length=50)
    tel         = models.CharField(max_length=20, blank=True)
    fix         = models.CharField(max_length=20, blank=True)
    created_at  = models.DateTimeField(auto_now=True)
    logo        = models.ImageField(upload_to='gesstock/', default='gesstock/customer-icon.png', blank=True)

    def __str__(self):
        return self.label

class Category(models.Model):

    label       = models.CharField(max_length=20)
    ref         = models.CharField(max_length=20, blank=True)


    def __str__(self):
        return self.label

class Article(models.Model):

    label       = models.CharField(max_length=20)
    quantity    = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    price       = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    ref         = models.CharField(max_length=20, blank=True)
    unite       = models.CharField(max_length=20, blank=True)

    category  = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.label


class   Procurement(models.Model):

    procurementDate = models.DateField()
    provider    = models.ForeignKey('Provider', on_delete=models.PROTECT)
    received    = models.BooleanField(default=False)

    def __str__(self):
        return "{}--{}".format(self.provider.label, self.received)

    def receivedLab(self):
        return "OUI" if self.received else "NON"
    def color(self):
        return "green" if self.received else "red"



class   ProcurementItem(models.Model):

    article     = models.ForeignKey('Article', on_delete=models.PROTECT)
    procurement = models.ForeignKey('Procurement', on_delete=models.PROTECT)
    quantity    = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return "{}--{}".format(self.article.label, self.quantity)


class   Delivery(models.Model):

    deliveryDate = models.DateField()
    customer     = models.ForeignKey('Customer', on_delete=models.PROTECT)
    delivered    = models.BooleanField(default=False)

    def __str__(self):
        return "{}--{}".format(self.customer.label, self.delivered)

    def deliveredLab(self):
        return "OUI" if self.delivered else "NON"
    def color(self):
        return "green" if self.delivered else "red"


class   DeliveryItem(models.Model):

    article     = models.ForeignKey('Article', on_delete=models.PROTECT)
    delivery    = models.ForeignKey('Delivery', on_delete=models.PROTECT)
    quantity    = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return "{}--{}".format(self.article.label, self.quantity)

