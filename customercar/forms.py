from django import forms
from .models import CustomerCar,CarPart

class CustomerCar_Form(forms.ModelForm):
    class Meta :
        model = CustomerCar
        fields = '__all__'
        exclude = ('user',)

class CarPart_Form(forms.ModelForm):
    class Meta :
        model = CarPart
        fields = '__all__'
        exclude = ('user',)