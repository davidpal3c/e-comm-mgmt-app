from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User
from django.forms import TextInput

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=TextInput(attrs={"placeholder": "Username"}))

    class Meta:             
        model = User        # model userReg will be interacting with (abstractUser in /admin app)
        fields = ['username', 'email']         # passes the field that are going to show up

