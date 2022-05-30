from django import forms
from .models import RequiremtsBranch,OutCome,InCome

class RequiremtsBranch_Form(forms.ModelForm):
    class Meta:
        model = RequiremtsBranch
        fields = '__all__'
        exclude = ('user',)

class OutComeForm(forms.ModelForm):
    class Meta:
        model = OutCome
        fields = '__all__'
        exclude = ('user',)