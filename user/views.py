from django.shortcuts import render
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.shortcuts import render,redirect

# Create your views here.

def register(request):
    if request.method=="POST":
        form=forms.RegisterForm(request.POST or None)
        if form.is_valid():                                     #verifie si clean method est True
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")

            newUser=User(username=username)
            newUser.set_password(password)

            newUser.save()
            login(request,newUser)
            message=messages.success(request,"Registered with success")
            return redirect("index",message)
        context={
        "form":form
        }
        return render(request,"register.html",context)
    else:
        form=forms.RegisterForm
        context={
        "form":form
        }
        return render(request,"register.html",context)


def loginUser(request):
    form = forms.LoginForm(request.POST or None)
    context={
        "form":form
    }
    if form.is_valid():  # verifie si clean method est True
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user=authenticate(username=username,password=password)
        if user is None:
            messages.info(request,"Username or Password error")
            return render(request,"login.html",context)
        messages.success(request,"You'are logged in")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)


def logoutUser(request):
    logout(request)
    messages.success(request,"You are logged out")
    return render(request,"index.html")

