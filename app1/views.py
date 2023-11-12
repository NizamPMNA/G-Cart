from django.shortcuts import render

# Create your views here.
def index(request):
    
    return render(request,'index.html')

def tour(request):

    return render(request,'tournaments/tour.html')