from django.urls import path
from . import views

app_name= "main"

urlpatterns = [
    path("", views.home, name='home'),  # Home page
    path('about/', views.about, name='about'),  # About page
    path('projects/', views.projects, name='projects'),  # Projects page
    path('contact/', views.contact, name='contact'),  # Contact page
]