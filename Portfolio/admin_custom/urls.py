from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

app_name = 'admin_custom'

urlpatterns = [
    #login 
    path('login/', auth_views.LoginView.as_view(), name='login'),
    
    # Dashboard Home
    path('dashboard/', views.dashboard_home, name='dashboard_home'),

    # CRUD for Projects
    path('projects/', views.project_list, name='project_list'),
    path('projects/create/', views.project_create, name='project_create'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('projects/<int:pk>/edit/', views.project_update, name='project_update'),
    path('projects/<int:pk>/delete/', views.project_delete, name='project_delete'),

    # CRUD for Contacts
    path('contact-messages/', views.contact_list, name='contact_list'),
    path('contact-messages/<int:pk>/', views.contact_detail, name='contact_detail'),
    path('contact-messages/<int:pk>/mark-as-read/', views.mark_message_as_read, name='mark_message_as_read'),
    path('contact-messages/<int:pk>/archive/', views.archive_message, name='archive_message'),
    path('contact-messages/<int:pk>/delete/', views.delete_message, name='delete_message'),
    
    # Logout
    path('logout/', views.logout_view, name='logout_view'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)