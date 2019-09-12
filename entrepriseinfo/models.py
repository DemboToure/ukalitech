from django.db import models
from django.utils import timezone

# Create your models here. 

class  EntrepriseInfo(models.Model):

    name            = models.CharField(max_length=100)
    entreprise_type = models.CharField(max_length=20, choices=[('personnal', 'personnel'), ('GIE', 'GIE'), ('SA', 'SA'), ('SARL', 'SARL')], blank=True)
    adress          = models.CharField(max_length=100)
    contact         = models.CharField(max_length=50)
    contact_2       = models.CharField(max_length=50, blank=True)
    ninea_number    = models.CharField(max_length=50)
    img             = models.ImageField(upload_to='entreprise/', default='entreprise/default.png', blank=True)
    

    def __str__(self):
        return self.name

"""
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
"""
