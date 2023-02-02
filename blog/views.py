from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def create(request):
    return render(request, 'create.html')

def home(request):
    context = {
        'home': '/static/home.css'
    }
    return render(request, 'home.html', context)