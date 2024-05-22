from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.forms import ModelForm
from .models import CustomUser


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username',)


class LogInForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')
