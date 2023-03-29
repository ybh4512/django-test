from django import forms

class AdminUserForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=300)
    created_at = forms.DateTimeField()
    updated_at = forms.DateTimeField()
