from django import forms
from .models import Supplier

class SupplierCreateForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name','phone','address']
class SupplierEditForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name','phone','address']


