# photos/models.py
from django.db import models
from django.utils import timezone

class Photo(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='photos/')
    published_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title