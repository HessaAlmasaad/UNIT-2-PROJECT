from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect 
from .models import Project, Contact  , ProjectImage
from .forms import ProjectForm, ContactForm , ProjectImageForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth import logout
from django.forms import modelformset_factory

# Dashboard Home View
@login_required
@user_passes_test(lambda u: u.is_superuser)  # Restrict access to superusers only
def dashboard_home(request):
    # Handle Project filtering, ordering, and pagination
    search_query_projects = request.GET.get('search_projects', '')
    ordering_projects = request.GET.get('ordering_projects', 'title')  # Default order by 'title'

    projects = Project.objects.all().order_by(ordering_projects)
    if search_query_projects:
        projects = projects.filter(title__icontains=search_query_projects)

    paginator_projects = Paginator(projects, 10)
    page_number_projects = request.GET.get('page_projects')
    page_obj_projects = paginator_projects.get_page(page_number_projects)

    # Handle Contact filtering, ordering, and pagination
    search_query_contacts = request.GET.get('search_contacts', '')
    ordering_contacts = request.GET.get('ordering_contacts', 'sender_name')  # Default order by 'sender_name'

    contacts = Contact.objects.all().order_by(ordering_contacts)
    if search_query_contacts:
        contacts = contacts.filter(sender_name__icontains=search_query_contacts)

    paginator_contacts = Paginator(contacts, 10)
    page_number_contacts = request.GET.get('page_contacts')
    page_obj_contacts = paginator_contacts.get_page(page_number_contacts)

    context = {
        'projects': page_obj_projects,
        'contacts': page_obj_contacts,
        'search_query_projects': search_query_projects,
        'ordering_projects': ordering_projects,
        'search_query_contacts': search_query_contacts,
        'ordering_contacts': ordering_contacts,
    }

    return render(request, 'admin_custom/dashboard_home.html', context)

# CRUD Views for Projects
@login_required
@user_passes_test(lambda u: u.is_superuser)
def project_list(request):
    search_query = request.GET.get('search', '')
    ordering = request.GET.get('ordering', 'title')
    category_filter = request.GET.get('category', '')

    projects = Project.objects.all().order_by(ordering)

    if search_query:
        projects = projects.filter(Q(title__icontains=search_query) | Q(category__icontains=search_query))
    
    if category_filter:
        projects = projects.filter(category=category_filter)

    paginator = Paginator(projects, 10)  # 10 projects per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'admin_custom/project_list.html', {
        'projects': page_obj,
        'search_query': search_query,
        'ordering': ordering,
        'category_filter': category_filter,
        'categories': Project._meta.get_field('category').choices
    })

@login_required
@user_passes_test(lambda u: u.is_superuser)
def project_create(request):
    # Using modelformset_factory to create a formset for ProjectImage model
    ProjectImageFormSet = modelformset_factory(ProjectImage, fields=('image',), extra=3)

    if request.method == "POST":
        form = ProjectForm(request.POST)
        formset = ProjectImageFormSet(request.POST, request.FILES, prefix='images')
        if form.is_valid() and formset.is_valid():
            project = form.save()
            for form in formset:
                if form.cleaned_data:
                    image = form.save(commit=False)
                    image.project = project
                    image.save()
            return redirect('admin_custom:project_list')
    else:
        form = ProjectForm()
        formset = ProjectImageFormSet(queryset=ProjectImage.objects.none(), prefix='images')

    return render(request, 'admin_custom/project_form.html', {'form': form, 'formset': formset})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'admin_custom/project_detail.html', {'project': project})

@login_required 
@user_passes_test(lambda u: u.is_superuser)
def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    ProjectImageFormSet = modelformset_factory(ProjectImage, form=ProjectImageForm, extra=0)  # Set extra to 0 to avoid redundancy

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        formset = ProjectImageFormSet(request.POST, request.FILES, queryset=ProjectImage.objects.filter(project=project), prefix='images')
        
        if form.is_valid() and formset.is_valid():
            project_instance = form.save()
            images = formset.save(commit=False)
            
            # Save images and associate them with the project
            for image in images:
                image.project = project_instance
                image.save()
            
            # Handle deletion of removed images
            for obj in formset.deleted_objects:
                obj.delete()
            
            return redirect('admin_custom:project_list')
    else:
        form = ProjectForm(instance=project)
        formset = ProjectImageFormSet(queryset=ProjectImage.objects.filter(project=project), prefix='images')

    return render(request, 'admin_custom/project_form.html', {'form': form, 'formset': formset})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        project.delete()
        return redirect('admin_custom:project_list')
    return render(request, 'admin_custom/project_confirm_delete.html', {'project': project})

# CRUD Views for Contacts
@login_required
@user_passes_test(lambda u: u.is_superuser)
def contact_list(request):
    search_query = request.GET.get('search', '')
    ordering = request.GET.get('ordering', 'sender_name')
    status_filter = request.GET.get('status', '')

    # Retrieve all contacts
    contacts = Contact.objects.all().order_by(ordering)

    # Apply search filter if a query is provided
    if search_query:
        contacts = contacts.filter(sender_name__icontains=search_query)
    
    # Apply status filter if a status is selected
    if status_filter:
        contacts = contacts.filter(status=status_filter)

    return render(request, 'admin_custom/contact_list.html', {
        'contacts': contacts,
        'search_query': search_query,
        'ordering': ordering,
        'status_filter': status_filter,
        'statuses': Contact._meta.get_field('status').choices  # Pass status choices to the template
    })


@login_required
@user_passes_test(lambda u: u.is_superuser)
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_custom:contact_list')
    else:
        form = ContactForm()
    return render(request, 'admin_custom/contact_form.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'admin_custom/contact_detail.html', {'contact': contact})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('admin_custom:contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'admin_custom/contact_form.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('admin_custom:contact_list')
    return render(request, 'admin_custom/contact_confirm_delete.html', {'contact': contact})

# Logout
def logout_view(request):
    logout(request)
    return redirect('main:home')
