from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    notification_token = models.CharField(max_length=255)

    def __str__(self):
        return self.username