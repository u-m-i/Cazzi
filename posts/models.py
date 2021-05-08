"""Post Models."""
from django.db import models

# Create your models here.

# imma creating the models here

class User(models.Model):
    """User Model"""
    #Login
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    #Personal data
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)

    bio = models.TextField(blank=True)

    birthday = models.DateField(blank=True, null=True)
    #Role
    is_admin = models.BooleanField(default=False)
    #Account Data
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
