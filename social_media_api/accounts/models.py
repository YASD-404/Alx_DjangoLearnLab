from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to="profile_pictures/", blank=True, null=True
    )

    followers = models.ManyToManyField(
        "self", symmetrical=False, related_name="followed_by", blank=True
    )
    following = models.ManyToManyField(
        "self", symmetrical=False, related_name="following_set", blank=True
    )

    def __str__(self):
        return self.username
