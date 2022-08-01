from dataclasses import field
import email
from unicodedata import name
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Наименование',required=True, widget=forms.TextInput(attrs={'class':'container-input'}))
    password1 = forms.CharField(label='Пароль',required=True, widget=forms.PasswordInput(attrs={'class':'container-input'}))
    password2 = forms.CharField(label='Повторите пароль',required=True, widget=forms.PasswordInput(attrs={'class':'container-input'}))
    email = forms.EmailField(label='E-mail',required=True, widget=forms.TextInput(attrs={'class':'container-input'}))
    first_name = forms.CharField(label='Имя',required=True, widget=forms.TextInput(attrs={'class':'container-input'}))
    last_name = forms.CharField(label='Фамилия',required=True, widget=forms.TextInput(attrs={'class':'container-input'}))

    class Meta:
        model = User
        fields  = ('first_name', "last_name", 'email', 'username', 'password1', 'password2',)

    def save(self, commit=True):
        user = super().save(commit= False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
            return user