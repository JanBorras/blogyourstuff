from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import UserProfile

class UserProfileCreationForm(UserCreationForm):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        validators=[]
    )
    first_name = forms.CharField(
        label='First Name',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    last_name = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        validators=[]
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        validators=[]
    )

    class Meta:
        model = UserProfile
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        # Add email validation logic here if needed
        return email

