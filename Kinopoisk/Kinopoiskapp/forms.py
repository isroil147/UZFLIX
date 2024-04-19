from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'prompt srch_explore'}), max_length=50, required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'prompt srch_explore'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'class': 'prompt srch_explore'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'prompt srch_explore'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SearchForm(forms.Form):
    query = forms.CharField(label='Search')

class AgeFilterForm(forms.Form):
    age_choices = [
        ('all', 'All Ages'),
        ('6', '6'),
        ('16', '16'),
        ('18', '18')
    ]
    age = forms.ChoiceField(choices=age_choices, label='Select your age')
