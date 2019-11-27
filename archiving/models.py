from django.db import models

# Create your models here. 
class ArchivingFolder(models.Model):
    label           = models.CharField(max_length=100)
    created_at      = models.DateTimeField(auto_now=True)

    folder          = models.ForeignKey('ArchivingFolder', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.label

    def getPath(self):
        return self.label+"-"+str(self.id)+"/"+self.folder.getPath() if self.folder is not None else self.label+"-"+str(self.id)


class ArchivingFile(models.Model):
    label           = models.CharField(max_length=100)
    created_at      = models.DateTimeField(auto_now=True)
    description     = models.CharField(max_length=500)
    code            = models.CharField(max_length=10, null=True, blank=True )
    
    document        = models.FileField(upload_to='archiving/')
    
    parentFolder    = models.ForeignKey('ArchivingFolder', on_delete=models.PROTECT)

    def __str__(self):
        return self.label

    def getIconPath(self):
        return 'images/'+self.document.url.split('.')[-1]+'.png'

