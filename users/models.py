# Django
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    """Proflile model.
    
    This extend the user data, with the proxy way
    """
    nickname = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(max_length=250, blank=True, unique=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=21, blank=True,)
    picture = models.ImageField(upload_to="users/pictures", blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username"""
        return self.nickname.username

