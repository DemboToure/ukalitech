from django.db import models
from gesstock.models import Provider, Customer
# Create your models here.

class Account(models.Model):
    label           = models.CharField(max_length=100)
    account_number  = models.IntegerField()
    account_type    = models.CharField(max_length=50, null=True)
    created_at      = models.DateTimeField(auto_now=True)


    def __str__(self):
        return "{}--{}".format(self.account_number,self.label) 

    # get all operation that are linked with this account 
    def get_operations(self):
        return self.operation_set.all()

    def get_total_debit(self):
        ops = self.operation_set.filter(type_operation='DEBIT')
        tab = [op.solde for op in ops]
        return sum( tab )

    def get_total_credit(self):
        ops = self.operation_set.filter(type_operation='credit')
        tab = [op.solde for op in ops]
        return sum( tab )
    
    # return a list of tuple that composed by debit end credit 
    def get_debit_credit_both(self):
        deb = self.operation_set.filter(type_operation='DEBIT')
        debtab = [op.solde for op in deb]

        cre = self.operation_set.filter(type_operation='credit')
        cretab = [op.solde for op in cre]

        if len(debtab) < len(cretab):
            debtab.extend( [0 for _ in range(len(cretab)-len(debtab))] )
        else:
            cretab.extend( [0 for _ in range(len(debtab)-len(cretab))] )
        
        return list(zip(debtab,cretab)) 
    
    # return true if the account is debitor else false
    def is_debtor(self):
        
        return True if self.get_total_credit() - self.get_total_debit() <0 else False

    # return the difference between credit end debit
    def get_difference(self):

        return abs(self.get_total_credit() - self.get_total_debit())


    



class Operation(models.Model):
    label           = models.CharField(max_length=100)
    solde           = models.IntegerField()
    document        = models.FileField(upload_to='accounting/',blank=True, null=True)
    type_operation  = models.CharField(max_length=10, choices=[('DEBIT','débiter'), ('credit','crediter')])
    created_at      = models.DateTimeField(auto_now=True)
    
    account         = models.ForeignKey('Account' , on_delete=models.PROTECT, null=True)
    provider        = models.ForeignKey(Provider, on_delete=models.PROTECT, null=True, blank=True)
    customer        = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True, blank=True)

    def hasDocument(self):
        try:
            print(self.document.url)
            return True
        except:
            return False 

