from django.db import models
from datetime import datetime

# Create your models here.
class Post_blog_form(models.Model):
    Title = models.CharField(max_length=200)
    Description = models.TextField()
    Pic = models.FileField(upload_to='images/')
    Author = models.CharField(max_length=50)
    Date_time = models.DateTimeField(default=datetime.now)
