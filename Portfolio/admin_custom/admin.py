from django.contrib import admin
from .models import Contact, Project  # Import your models

from .models import Project, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1  # Number of empty image fields to display by default

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'date_created']
    inlines = [ProjectImageInline]
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('sender_name', 'sender_email', 'status', 'date_sent')
    list_filter = ('status', 'date_sent')
    search_fields = ('sender_name', 'sender_email', 'message_content')
