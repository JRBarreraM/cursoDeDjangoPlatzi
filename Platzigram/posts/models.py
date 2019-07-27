"""Posts models."""
# Django
from django.db import models

class User(models.Model):
    """User model."""
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    isAdmin = models.BooleanField(default=False)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank = True, null = True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

