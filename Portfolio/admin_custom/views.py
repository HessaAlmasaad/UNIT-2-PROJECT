from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render,redirect
from .models import Project
#from .forms import ProjectForm  # Assuming you have created a ProjectForm
from .models import Contact
#from .forms import ContactMessageForm  # Assuming you have created a ContactMessageForm

def is_superuser(user):
    return user.is_superuser  

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



# Create a new contact message
# def create_contact_message(request):
#     if request.method == 'POST':
#         form = ContactMessageForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('contact_message_list')  # Redirect to the contact message list
#     else:
#         form = ContactMessageForm()
#     return render(request, 'admin_custom/contact_form.html', {'form': form})

# Read (view) all contact messages
# def contact_message_list(request):
#     messages = Contact.objects.all()
#     return render(request, 'admin_custom/contact_message_list.html', {'messages': messages})

# Read (view) a single contact message
# def contact_message_detail(request, pk):
#     message = get_object_or_404(Contact, pk=pk)
#     return render(request, 'admin_custom/contact_message_detail.html', {'message': message})

# Delete a contact message
# def delete_contact_message(request, pk):
#     message = get_object_or_404(Contact, pk=pk)
#     if request.method == 'POST':
#         message.delete()
#         return redirect('contact_message_list')
#     return render(request, 'admin_custom/contact_message_confirm_delete.html', {'message': message})

