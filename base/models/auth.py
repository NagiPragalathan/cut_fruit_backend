# auth_app/models.py
from django.contrib.auth.models import User
from django.db import models

class Role(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
