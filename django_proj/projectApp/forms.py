from typing import Any
from django import forms
from .models import BasicModel, GeeksModel, RegisterModel
from django_password_eye.fields import PasswordEye
from django.core.validators import RegexValidator


my_string_validator= RegexValidator(r"", "Value should be string format!")

class GeeksForm(forms.ModelForm):
 
    # create meta class 
    class Meta:
        # specify model to be used
        model = GeeksModel
 
        # specify fields to be used
        fields = [
            "title",
            "description",
        ]



# creating a register form
class RegisterForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = RegisterModel
 
        # specify fields to be used
        fields = [
            "firstname",
            "lastname",
            "email",
            "contactnumber",
            "password",
            "confirmpassword",
            "description",
        ]
        widgets = {
            "firstname" : forms.TextInput(attrs={'placeholder':'Enter Your First Name','autocomplete':'off'}),
            "lastname" : forms.TextInput(attrs={'placeholder':'Enter Your Last Name','autocomplete':'off'}),
            "email" : forms.TextInput(attrs={'placeholder':'abc@gmail.com','autocomplete':'off'}),
            "contactnumber" : forms.TextInput(attrs={'placeholder':'9881587896','autocomplete':'off'}),
            "password" : forms.PasswordInput(attrs={'placeholder':'******','autocomplete':'off','data-toggle':'password'}),
            "confirmpassword" : forms.PasswordInput(attrs={'placeholder':'******','autocomplete':'off','data-toggle':'password'}),
            "description" : forms.TextInput(attrs={'placeholder':'This is new user .....','autocomplete':'off'})
        }


# creating a login form
class LoginForm(forms.ModelForm):

    # password = forms.CharField(widget=forms.PasswordInput)
    # password : PasswordEye(label='')
    # create meta class
    class Meta:
        # specify model to be used
        model = RegisterModel
 
        # specify fields to be used
        fields = [
           "email",
           "password",
       ]
        labels = {
            "email" : "Username",
            "password" : "Password"
        }
        widgets = {
            "email" : forms.TextInput(attrs={'placeholder':'karan@gmail.com','autocomplete':'off'}),
            "password" : forms.PasswordInput(attrs={'placeholder':'******','autocomplete':'off','data-toggle':'password'})
             
        }

        

        
# creating a form
class BasicForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = BasicModel
 
        # specify fields to be used
        fields = [
            "title",
            "description",
        ]
