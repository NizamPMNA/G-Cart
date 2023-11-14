from django.shortcuts import render

# Create your views here.
def index(request):
    
    return render(request,'index.html')

def tour(request):

    return render(request,'tournaments/tour.html')

def football(request):

    return render(request,'tournaments/football/football.html')

def single_elimination(request):

    return render(request,'tournaments/football/single_elimination.html')