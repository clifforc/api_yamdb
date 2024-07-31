from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLES = (
        ('user', 'User'),
        ('moderator', 'Moderator'),
        ('admin', 'Admin')
    )

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLES, default='user')
    confirmation_code = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.username


class Categories(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name


class Genres(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name


class Titles(models.Model):
    name = models.CharField(max_length=256)
    year = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    genre = models.ForeignKey(
        Genres, on_delete=models.CASCADE, related_name='titles'
    )

    def __str__(self):
        return self.name
