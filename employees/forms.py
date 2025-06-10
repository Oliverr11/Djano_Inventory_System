from django import forms
from .models import Employee

class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'age', 'phone', 'address', 'username', 'password']
class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'age', 'phone', 'address', 'username', 'password']
       