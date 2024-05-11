from django.contrib import messages
from django.shortcuts import redirect, render
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User,auth

from .forms import GeeksForm, LoginForm, RegisterForm,BasicForm
from . import views
from .models import GeeksModel, RegisterModel,BasicModel



def home(request):
    return render(request,"home.html")


def register(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}


    # add the dictionary during initialization
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        password =form.cleaned_data["password"]
        confirm_password =form.cleaned_data["confirmpassword"]
        if password == confirm_password:
            form.save()
            messages.info(request,'Registration Successfully Completed!')
            return redirect(register_view)
        else:
            messages.info(request,"password not matched!")
    context['form']= form
    return render(request, "register.html", context)

  


def basic(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = BasicForm(request.POST or None)
    if form.is_valid():
        password =form.cleaned_data["password"]
        confirm_password =form.cleaned_data["confirmpassword"]
        if password == confirm_password:
            form.save()
            messages.info(request,'Registration Successfully Completed!')
            return redirect(basic_view)
        else:
            messages.info(request,"password not matched!")
    context['form']= form
    return render(request, "basic.html", context)





def login(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
    dataset = RegisterModel.objects.all()
 
    # add the dictionary during initialization
    form = LoginForm(request.POST or None)
    if form.is_valid():
        email= form.cleaned_data["email"]
        password =form.cleaned_data["password"]
        for data in dataset:
            datatemp= data
            if email == datatemp.email :
                if password == datatemp.password:
                    messages.info(request,'Logged In Successfully!')
                    return redirect(basic)
                else:
                    messages.info(request,'Password is not valid!')
                    return redirect(register)
            else:
                messages.info(request,'Username or password is not valid!')
                return redirect(register)
        
    context['form']= form
    return render(request, "login.html", context)


def create_view(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = (request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "create_view.html", context)

def list_view(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = GeeksModel.objects.all()
         
    return render(request, "list_view.html", context)

def register_view(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = RegisterModel.objects.all()
         
    return render(request, "register_view.html", context)

 
 



def overview(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "overview.html", context)


def Variable(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "Variable.html", context)


def Loops(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "Loops.html", context)




def condition(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "condition.html", context)



def function(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "function.html", context)





def keywords(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "keywords.html", context)

    
def tuple(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "tuple.html", context)


def set(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "set.html", context)


def module(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "module.html", context)


def directory(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "directory.html", context)


def dictionary(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "dictionary.html", context)



def forget(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "forget.html", context)








