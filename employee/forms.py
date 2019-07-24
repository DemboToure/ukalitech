from django.utils import timezone
from django import forms
from .models import *

class  EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee 
        fields= '__all__'


class  PostForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields= '__all__'

class  ContractForm(forms.ModelForm):
    class Meta:
        model = Contract 
        fields= '__all__'

