from django import forms
from . models import Account, Vet
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=200)

    class Meta:
        model = Account
        fields = ['fullName', 'email', 'phoneNumber', 'role','county']


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password',)

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")


class VetRegistrationForm(forms.ModelForm):
    class Meta:
        model = Vet
        fields = ['account', 'vetNo','county']
