from django import forms
from .models import AdminUser

class AdminUserForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=300)

    class Meta:
        model = AdminUser
        fields = '__all__'
