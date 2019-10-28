from django.db import models
from .enum import ServiceSet

class Endpoint(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
    service = models.CharField(max_length=50, choices=[(tag, tag.value) for tag in ServiceSet])
    url = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.url