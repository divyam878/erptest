from django import forms

class UsersForm(forms.Form):
    name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=15)
    registrationNo = forms.CharField(max_length=50)
    verified = forms.CharField(max_length=50)
    created = forms.CharField(max_length=50)
    status = forms.CharField(max_length=20)