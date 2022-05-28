from django import forms
from .models import Employee

class Employee_Form(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ('user',)
