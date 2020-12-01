from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):

    email = forms.EmailField()
    phone_number = forms.IntegerField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email','phone_number', 'password1', 'password2')

        