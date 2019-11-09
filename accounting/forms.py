from django.utils import timezone
from django import forms
from .models import *


class  AccountForm(forms.ModelForm):
    class Meta:
        model = Account 
        fields= '__all__'


class  OperationForm(forms.ModelForm):
    class Meta:
        model = Operation 
        fields= '__all__'

