"""Post models, for the users"""
# Django
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Models
from users.models import Profile

class Post(models.Model):
    """Post model."""

    user = models.ForeignKey(User, on_delete=CASCADE)
    profile = models.ForeignKey(Profile, on_delete=CASCADE)

    tittle = models.CharField(max_length=260)
    photo = models.ImageField(upload_to="posts/photos")

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.tittle} by @{self.user.username}"