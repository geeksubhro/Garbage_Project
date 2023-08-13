from django import forms
from .models import *

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'  
