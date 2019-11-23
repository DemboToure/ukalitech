from django.utils import timezone
from django import forms
from .models import *


class  FileForm(forms.ModelForm):
    class Meta:
        model = ArchivingFile 
        fields= '__all__'

