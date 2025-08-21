from django import forms
from django.contrib.auth.models import AbstractUser


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta():
        model = AbstractUser
        fields = ('username', 'password')
