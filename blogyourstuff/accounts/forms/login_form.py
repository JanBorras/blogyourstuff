from django import forms
from django.contrib.auth.forms import AuthenticationForm
from accounts.models import UserProfile

class LoginForm(AuthenticationForm):
    
    username = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'InputEmail', 'aria-describedby': 'emailHelp'}),
        required=True
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'InputPassword'}),
        required=True
    )

    class Meta:
        model = UserProfile
        fields = ['email', 'password']
        
