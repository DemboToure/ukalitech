from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Application(models.Model):

    name   = models.CharField(max_length=20)
    icon   = models.CharField(max_length=20, default="dashboard", null=True, blank=True)

    def __str__(self):
        return self.name 

    def getUrl(self):

        return "{}{}".format(self.name, 'Home')

    def isAuthorized(self, userId):
        user = User.objects.get(id=userId)
        for role in user.role_set.all():
            if role.application.id == self.id:
                return True
        
        return False
    

class Role(models.Model):

    user            = models.ForeignKey(User, on_delete=models.PROTECT)
    application        = models.ForeignKey("Application", on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return "{}--{}".format(self.user.username, self.application.name)

        