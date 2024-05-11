from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator


# my_string_validator= RegexValidator(r"", "Value should be string format!")
# Create your models here.
# def contact_no(value):
#     if value < 10:
#         raise ValidationError("%")

# declare a new model with a name "GeeksModel"
class GeeksModel(models.Model):
 
    # fields of the model
    title = models.CharField(max_length = 200)
    description = models.TextField()
 
    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title
    
    
class RegisterModel(models.Model):
 
    # fields of the model
    firstname = models.CharField(
        max_length =30,
        validators=[
            RegexValidator(
                regex=r'^[A-Z,a-z]',
                message="First Name Should Be String !!",
                code= "invalid_registration"
            )])
    lastname = models.CharField(
        max_length =30,
        validators=[
            RegexValidator(
                regex=r'^[A-Z,a-z]',
                message="Last Name Should Be String !!",
                code= "invalid_registration"
            )])
    email = models.CharField(
        max_length = 200,
        validators=[
            RegexValidator(
                regex= r',*\@gmail.com$',
                # regex=r'/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;',
                message="Email ID Should Be Proper Format!!",
                code= "invalid_registration"
            )])
    contactnumber = models.CharField(
        max_length = 12,
        validators=[
            RegexValidator(
                regex=r'^[0-9]{10}$',
                message="Contact Number Should Be 10 Digit !!",
                code= "invalid_registration"
            )])
    password = models.CharField(max_length = 10)
    confirmpassword = models.CharField(max_length = 10)
    description = models.CharField(null= True,max_length = 200)
    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.firstname #, self.lastname, self.email, self.contactnumber, self.password, self.confirmpassword



    

class BasicModel(models.Model):
 
    # fields of the model
    title = models.CharField(max_length = 200)
    description = models.TextField()
 
    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title
    

