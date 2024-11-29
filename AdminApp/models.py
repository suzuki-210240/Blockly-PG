from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    CATEGORY_CHOICES = [
        ('basic', '基本'),
        ('advanced', '応用'),
    ]
    
    title = models.CharField(max_length=200)
    file_content = models.TextField()
    file_type = models.CharField(max_length=10, choices=[('html', 'HTML'), ('py', 'Python')])
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
# Create your models here.
