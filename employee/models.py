from django.db import models
from django.utils import timezone

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

     
