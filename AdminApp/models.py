from django.db import models
from django.contrib.auth.models import User
from pathlib import Path
from django.conf import settings

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


def upload_to_overwrite(instance, filename):
    file_path = Path(settings.MEDIA_ROOT) / 'uploads' /filename

    if file_path.exists():
        file_path.unlink()

    return Path('uploads') / filename

class FileUpload(models.Model):
    file = models.FileField(upload_to=upload_to_overwrite)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.file.name)
