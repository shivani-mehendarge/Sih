from django import forms
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignuForm(UserCreationForm):
    mobile_number = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','mobile_number','password1','password2']
