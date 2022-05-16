from django import forms
from .models import Invoice

class Invoice_Form(forms.ModelForm):
    class Mete :
        model = Invoice
        fields = '__all__'
