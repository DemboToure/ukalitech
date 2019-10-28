from django.utils import timezone
from django import forms
from .models import *

class  ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider 
        fields= '__all__'

class  CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer 
        fields= '__all__'

class  ArticleForm(forms.ModelForm):
    class Meta:
        model = Article 
        fields= '__all__'

class  CategoryForm(forms.ModelForm):
    class Meta:
        model = Category 
        fields= '__all__'

class  ProcurementForm(forms.ModelForm):
    class Meta:
        model = Procurement 
        fields= '__all__'

class  ProcurementItemForm(forms.ModelForm):
    class Meta:
        model = ProcurementItem 
        fields= '__all__'

class  DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery 
        fields= '__all__'
    

class  DeliveryItemForm(forms.ModelForm):
    class Meta:
        model = DeliveryItem 
        fields= '__all__'