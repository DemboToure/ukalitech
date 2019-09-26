from django.db import models
from django.utils import timezone
from decimal import Decimal 

# Create your models here. 

class  Employee(models.Model):

    first_name  = models.CharField(max_length=20)
    last_name   = models.CharField(max_length=20)
    sexe        = models.CharField(max_length=5, choices=[('M', 'HOMME'), ('W', 'FEMME')], blank=True)
    email       = models.EmailField(max_length=50, blank=True)
    tel         = models.CharField(max_length=30, blank=True)
    fix         = models.CharField(max_length=30, blank=True)
    adress      = models.CharField(max_length=100, blank=True)
    profil_img  = models.ImageField(upload_to='employee/', default='employee/default.png', blank=True)
    birth_date  = models.DateField()
    birth_to    = models.CharField(max_length=50)
    regis_number= models.CharField(max_length=20)
    cni         = models.CharField(max_length=20)
    created_at  = models.DateTimeField(auto_now=True)

    marital_status = models.CharField(max_length=10, choices=[('married', 'married'), ('single', 'single')],blank=True)
    number_children= models.IntegerField(default=0, blank=True)
    social_security_number = models.CharField(max_length=20, blank=True)


    def __str__(self):
        return self.first_name+" | "+self.email 



class Contract(models.Model):

    contract_type   = models.CharField(max_length=10, choices=[('CDD','CDD'), ('CDI','CDI'), ('STAGE','STAGE')])
    begin           = models.DateField()
    end             = models.DateField()
    salary          = models.IntegerField()
    location        = models.CharField(max_length=20)
    contract_doc    = models.FileField(upload_to='employee/',null=True)
    created_at      = models.DateTimeField(auto_now=True)
    
    post            = models.ForeignKey('Post', on_delete=models.PROTECT)
    employees       = models.ForeignKey('Employee', on_delete=models.PROTECT)


class Post(models.Model):

    label       = models.CharField(max_length=100)
    desc        = models.CharField(max_length=100)
    created_at  = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.label

class Diploma(models.Model):
    
    label   = models.CharField(max_length=100)
    school  = models.CharField(max_length=100)
    year    = models.IntegerField()

    employee   = models.ForeignKey('Employee', on_delete=models.PROTECT)

    def __str__(self):
        return self.label



class ProfessionalExperience(models.Model):

    structure = models.CharField(max_length=100)
    begin     = models.DateField()
    end       = models.DateField()
    post      = models.CharField(max_length=100)
    desc      = models.CharField(max_length=100)

    employee  = models.ForeignKey('Employee', on_delete=models.PROTECT)
    
    def __str__(self):
        return self.structure
    

class SalaryDesignation(models.Model):
    
    code                = models.IntegerField() 
    label               = models.CharField(max_length=100)
    nbr_hour            = models.IntegerField(null=True, blank=True)
    base                = models.DecimalField(max_digits=15, decimal_places=3, null=True, blank=True)
    salary_rate         = models.DecimalField(max_digits=5,  decimal_places=3, null=True, blank=True)
    salary_gain         = models.DecimalField(max_digits=15, decimal_places=3, null=True, blank=True)
    salary_deduction    = models.DecimalField(max_digits=15, decimal_places=3, null=True, blank=True)
    patronal_rate       = models.DecimalField(max_digits=5,  decimal_places=3, null=True, blank=True)
    patronal_deduction  = models.DecimalField(max_digits=15, decimal_places=3, null=True, blank=True)
    
    
    def __str__(self):
        return self.label
    
class Salary(models.Model):

    employee  = models.ForeignKey('Employee', on_delete=models.PROTECT)
    salary_period = models.DateField()
    created_at  = models.DateTimeField(auto_now=True)
    closed      = models.BooleanField(default=False)

    def __str__(self):
        return self.employee.first_name
    
    def duplicate(self):
        s = Salary() 
        s.employee = self.employee
        s.salary_period = self.salary_period
        s.closed = False
        s.save()

        for sdg in self.salaryitems_set.all():
            si = sdg.duplicate(s)
            si.save()

        return s 


class SalaryItems(models.Model):
    
    code                = models.IntegerField() 
    label               = models.CharField(max_length=100)
    nbr_hour            = models.IntegerField(null=True, blank=True)
    base                = models.DecimalField(max_digits=15, decimal_places=3, null=True, blank=True)
    salary_rate         = models.DecimalField(max_digits=5,  decimal_places=3, null=True, blank=True)
    salary_gain         = models.DecimalField(max_digits=15, decimal_places=3, null=True, blank=True)
    salary_deduction    = models.DecimalField(max_digits=15, decimal_places=3, null=True, blank=True)
    patronal_rate       = models.DecimalField(max_digits=5,  decimal_places=3, null=True, blank=True)
    patronal_deduction  = models.DecimalField(max_digits=15, decimal_places=3, null=True, blank=True)
    
    salary  = models.ForeignKey('Salary', on_delete=models.PROTECT)

    def __str__(self):
        return "{}-{}".format(self.label, self.salary.employee.first_name)

    def duplicate(self, salary):
        si = SalaryItems()
        si.code = self.code
        si.label = self.label
        si.nbr_hour = self.nbr_hour 
        si.base = self.base 
        si.salary_rate = self.salary_rate 
        si.salary_gain = self.salary_gain 
        si.salary_deduction = self.salary_deduction
        si.patronal_rate = self.patronal_rate 
        si.patronal_deduction = self.patronal_deduction
        si.salary = salary

        si.save()
        
        return si 

    def setAttr(self, key, value):
        value = value.replace(',', '.', 1) 
        value = value.replace(' ', '' , 4) 
        print("{} = {}".format(key, None if value=='' else value))
        if key == "code":
            self.code = value
        elif key == "label":
            self.label = value
        elif key == "nbr_hour":
            self.nbr_hour = None if value=='' else value
        elif key == "base":
            self.base = None if value=='' else Decimal(value)
        elif key == "salary_rate":
            self.salary_rate = None if value=='' else Decimal(value)
        elif key == "salary_gain":
            self.salary_gain = None if value=='' else Decimal(value)
        elif key == "salary_deduction":
            self.salary_deduction = None if value=='' else Decimal(value)
        elif key == "patronal_rate":
            self.patronal_rate = None if value=='' else Decimal(value) 
        elif key == "patronal_deduction":
            self.patronal_deduction = None if value=='' else Decimal(value)

