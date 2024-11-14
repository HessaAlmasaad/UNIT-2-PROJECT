from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['sender_name', 'sender_email', 'message_content']
        widgets = {
            'sender_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'sender_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'message_content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message'}),
        } 
