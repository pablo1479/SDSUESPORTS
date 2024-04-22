from django import forms
from .models import Registrant
from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'id': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'id': 'password'}))

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registrant
        fields = ['first_name', 'last_name', 'student_email', 'password', 'student_id', 'twitch']
