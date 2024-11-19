from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(
        max_length=100,
        choices=[
            ('All', 'All'),
            ('Web Development', 'Web'),
            ('Full Stack Development', 'Full Stack'),
            ('Game Development', 'Game'), 
            ('Agile and Project Management', 'Project Management'), 
            ('Hackathon Projects', 'Hackathon'),
        ],
        default='All'
    )
    technologies_used = models.TextField()
    role_details = models.TextField()
    github_url = models.URLField(blank=True, null=True)
    project_date = models.DateField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"Image for {self.project.title}"

class Contact(models.Model):
    sender_name = models.CharField(max_length=100)
    sender_email = models.EmailField()
    message_content = models.TextField()
    status = models.CharField(max_length=50, choices=[
        ('unread', 'Unread'),
        ('read', 'Read'),
        ('archived', 'Archived')
    ], default='unread')
    date_sent = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def mark_as_read(self):
        self.status = 'read'
        self.save()

    def archive_message(self):
        self.status = 'archived'
        self.save()

    def delete_message(self):
        self.delete()

    def __str__(self):
        return f'Message from {self.sender_name} - {self.sender_email}'

