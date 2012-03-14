from django import forms

from offices.models import Office

class OfficeForm (forms.ModelForm):

    class Meta: 
        model = Office
        fields = ['name', 'url', 'photo',]
