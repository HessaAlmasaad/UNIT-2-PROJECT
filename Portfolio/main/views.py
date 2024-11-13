from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse


# Create your views here
def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def projects(request):
    return render(request, 'main/projects.html')

def contact(request):
    return render(request, 'main/contact.html')


