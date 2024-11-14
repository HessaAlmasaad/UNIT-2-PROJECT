from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render,redirect
from .models import Project
#from .forms import ProjectForm  # Assuming you have created a ProjectForm
from .models import Contact
#from .forms import ContactForm  # Assuming you have created a ContactMessageForm

def is_superuser(user):
    return user.is_superuser  

@login_required
@user_passes_test(is_superuser)
def dashboard(request):
    return render(request, 'admin_custom/admin_dashboard.html')

@user_passes_test(is_superuser)
def project_details(request):
    return render(request, 'admin_custom/project_details.html')

@user_passes_test(is_superuser)
def contact_messages(request):
    return render(request, 'admin_custom/contact_messages.html')

#Create a new project
# def create_project(request):
#     if request.method == 'POST':
#         form = ProjectForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('project_list')  # Redirect to the list of projects
#     else:
#         form = ProjectForm()
#     return render(request, 'admin_custom/project_form.html', {'form': form})

# Read (view) all projects
# def project_list(request):
#     projects = Project.objects.all()
#     return render(request, 'admin_custom/project_list.html', {'projects': projects})

# Read (view) a single project
# def project_detail(request, pk):
#     project = get_object_or_404(Project, pk=pk)
#     return render(request, 'admin_custom/project_detail.html', {'project': project})

# Update a project
# def update_project(request, pk):
#     project = get_object_or_404(Project, pk=pk)
#     if request.method == 'POST':
#         form = ProjectForm(request.POST, instance=project)
#         if form.is_valid():
#             form.save()
#             return redirect('project_detail', pk=project.pk)
#     else:
#         form = ProjectForm(instance=project)
#     return render(request, 'admin_custom/project_form.html', {'form': form})

# Delete a project
# def delete_project(request, pk):
#     project = get_object_or_404(Project, pk=pk)
#     if request.method == 'POST':
#         project.delete()
#         return redirect('project_list')
#     return render(request, 'admin_custom/project_confirm_delete.html', {'project': project})

# @user_passes_test(lambda u: u.is_staff)  
# def contact_messages_view(request):
#     contacts = Contact.objects.all().order_by('-date_sent')  # Sort by most recent
#     return render(request, 'admin_custom/contact_messages.html', {'contacts': contacts})