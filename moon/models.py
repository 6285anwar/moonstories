from django.db import models

# Create your models here.

class Story(models.Model):
    storyname = models.CharField(max_length=240, null=True)
    storysrc = models.CharField(max_length=240, null=True)
    content = models.CharField(max_length=240, null=True)
    bookphoto = models.FileField(upload_to='images/', null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=60, null=True)

    latest = models.CharField(max_length=60, null=True)