from django.shortcuts import render,redirect
from admin_custom.models import Project 
from admin_custom.models import Contact 
from .forms import ContactForm  

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'main/projects.html',{'projects': projects})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the data to the database
            return redirect('main:thank_you.html')  # Redirect after successful submission
    else:
        form = ContactForm()

    return render(request, 'main/contact_form.html', {'form': form})

