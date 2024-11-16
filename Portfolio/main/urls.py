from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name= "main"

urlpatterns = [
    path('home/', views.home, name='home'),  # Home page
    path('about/', views.about, name='about'),  # About page
    path('projects/', views.projects, name='projects'),  # Projects page
    path('projects-views/<int:pk>', views.project_view, name='project_view'),  # Projects views page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('thank-you/', views.thank_you_view, name='thank_you'),  # Thank_you Page
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)