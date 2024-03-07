from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User
from django.forms import TextInput

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"}))

    class Meta:             
        model = User        # model userReg will be interacting with (abstractUser in /admin app)
        fields = ['username', 'email']         # passes the field that are going to show up

