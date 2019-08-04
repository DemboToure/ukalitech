from django.db import models

# Create your models here.

class Account(models.Model):
    label           = models.CharField(max_length=100)
    account_number  = models.IntegerField()
    created_at  = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.label 



class Operation(models.Model):
    label           = models.CharField(max_length=100)
    solde           = models.IntegerField()
    document        = models.FileField(upload_to='accounting/',blank=True, null=True)
    type_operation  = models.CharField(max_length=10, choices=[('DEBIT','débiter'), ('credit','crediter')])
    created_at  = models.DateTimeField(auto_now=True)

    
    account         = models.ForeignKey('Account', on_delete=models.PROTECT)

