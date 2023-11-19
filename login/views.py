from django.shortcuts import render
from .models import Register
# Create your views here.
def login(request):
    
    return render(request,'login.html')

def register(request):
    if request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')
        reg_obj = Register(email=email,password=password)
        reg_obj.save()
    
    return render(request,'register.html')