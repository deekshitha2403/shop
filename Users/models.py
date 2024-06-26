from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile = models.ImageField(upload_to="profile_pictures")
