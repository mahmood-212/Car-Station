from django import forms
from .models import Company,CompanyBranch

class Company_Form(forms.ModelForm):
    class Meta :
        model = Company
        fields = '__all__'
        exclude = ('user',)

class CompanyBranch_Form(forms.ModelForm):
    class Meta :
        model = CompanyBranch
        fields = '__all__'
        exclude = ('user',)