from django.shortcuts import render
from admin_custom.models import Project  
from .forms import ContactForm  

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'main/projects.html',{'projects': projects})

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'main/contact.html', {'form': form})
