from .models import EmployeeModel
from django import forms


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = '__all__'
        
        labels={
            'f_name': 'First Name',
            'l_name': 'Last Name'
        }

