from django.urls import path
from . import views

app_name = "admin_custom"

urlpatterns = [
    path('project-details/', views.project_details, name='project_details'),  # Admin Project Details page
    path('contact-messages/', views.contact_messages, name='contact_messages'),  # Admin Contact Messages page
]
