from django.db import models

# Create your models here.

class Account(models.Model):
    label           = models.CharField(max_length=100)
    account_number  = models.IntegerField()
    created_at      = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.label 

    def get_operations(self):
        return self.operation_set.all()

    def get_total_debit(self):
        ops = self.operation_set.filter(type_operation='DEBIT')
        tab = [op.solde for op in ops]
        print(tab)
        return sum( tab )

    def get_total_credit(self):
        ops = self.operation_set.filter(type_operation='credit')
        tab = [op.solde for op in ops]
        print(tab)
        return sum( tab )
    
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
    
    def is_debtor(self):
        
        return True if self.get_total_credit() - self.get_total_debit() <0 else False

    def get_difference(self):

        return abs(self.get_total_credit() - self.get_total_debit())


    



class Operation(models.Model):
    label           = models.CharField(max_length=100)
    solde           = models.IntegerField()
    document        = models.FileField(upload_to='accounting/',blank=True, null=True)
    type_operation  = models.CharField(max_length=10, choices=[('DEBIT','débiter'), ('credit','crediter')])
    created_at      = models.DateTimeField(auto_now=True)
    
    account         = models.ForeignKey('Account', on_delete=models.PROTECT)

