from django import forms
from .models import Registrant

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registrant
        fields = ['first_name', 'last_name', 'student_email', 'password', 'student_id', 'twitch']
        widgets = {
            'password': forms.PasswordInput(),
        }
