from django import forms
from .models import Place


#  Django's Forms work of brevity, used to build a form specifically for the model Place, dealing with (only!) the attributes of 'name' and 'visited'.
class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('name', 'visited')
