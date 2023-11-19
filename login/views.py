from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Register
from django.contrib.auth import authenticate,login
# Create your views here.

def register(request):
    user = None
    error_msg = None
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        try:
            user = User.objects.create_user(username=username,password=password,email=email)
        except Exception:
            error_msg = username
        if user:
            return redirect('login')
            
    
    return render(request,'register.html',{'user':user,'error_msg':error_msg})

def login(request):
    error_msg = None
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('index')
        else:
            error_msg = 'invalid credencials'

    return render(request,'login.html',{'error_msg':error_msg})