from django import forms
from .models import Employee

class Employee_Form(forms.ModelForm):
    class Mete :
        model = Employee
        fields = '__all__'
