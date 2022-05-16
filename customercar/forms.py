from django import forms
from .models import CustomerCar,CarPart

class CustomerCar_Form(forms.ModelForm):
    class Mete :
        model = CustomerCar
        fields = '__all__'

class CarPart_Form(forms.ModelForm):
    class Mete :
        model = CarPart
        fields = '__all__'