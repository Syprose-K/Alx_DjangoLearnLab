from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    following = models.ManyToManyField(
        'self',
        symmetrical=False, #if A follows B, B does NOT follow A automatically
        related_name='followers',
        blank=True
    )
    def __str__(self):
        return self.username
