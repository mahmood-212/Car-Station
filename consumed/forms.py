from django import forms
from .models import RequiremtsBranch,OutCome,InCome

class RequiremtsBranch_Form(forms.ModelForm):
    class Mete :
        model = RequiremtsBranch
        fields = '__all__'
        exclude = ('user',)

class OutCome(forms.ModelForm):
    class Mete :
        model = OutCome
        fields = '__all__'
        exclude = ('user',)