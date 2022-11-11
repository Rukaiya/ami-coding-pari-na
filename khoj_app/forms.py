from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Khoj



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

class KhojForm(ModelForm):
    search_value = forms.IntegerField(label = 'search_value', required = True)
    class Meta:
        model = Khoj
        fields = ['input_value', 'search_value']
