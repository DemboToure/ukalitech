from django.utils import timezone
from django import forms
from .models import *

class  InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields= '__all__'


class  InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields= '__all__'

class  InvoicePayForm(forms.ModelForm):
    class Meta:
        model = InvoicePay
        fields= '__all__'
