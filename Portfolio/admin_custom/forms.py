from django import forms
from .models import Project , Contact , ProjectImage
        
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        # Remove 'date_created' from the fields
        fields = ['title', 'description', 'category', 'github_url', 'technologies_used', 'role_details',  'project_date']
        widgets = {
            'project_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class ProjectImageFormSet(forms.ModelForm):
    class Meta:
        model = ProjectImage
        fields = ['image']
    
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['sender_name', 'sender_email', 'message_content', 'status']