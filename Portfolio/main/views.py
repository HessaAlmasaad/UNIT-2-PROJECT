from django.shortcuts import render,redirect
from admin_custom.models import Project 
from admin_custom.models import Contact 
from .forms import ContactForm  

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def projects(request):
    category = request.GET.get('category', 'all')
    if category == 'all':
        projects = Project.objects.all()
    else:
        projects = Project.objects.filter(category__iexact=category)  # Case-insensitive match
    return render(request, 'main/projects.html', {'projects': projects})


def project_view(request):
    return render(request, 'main/project_view.html')
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the data to the database
            return redirect('main:thank_you')  # Redirect after successful submission
    else:
        form = ContactForm()

    return render(request, 'main/contact_form.html', {'form': form})

def thank_you_view(request):
    return render(request, 'main/thank_you.html')

