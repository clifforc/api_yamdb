from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLES = (
        ('user', 'User'),
        ('moderator', 'Moderator'),
        ('admin', 'Admin')
    )

    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    role = models.CharField(max_length=20, choices=ROLES, default='user')
    confirmation_code = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.username


class CommonInfo(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ['name']


class Category(CommonInfo):
    slug = models.SlugField(max_length=50, unique=True)


class Genre(CommonInfo):
    slug = models.SlugField(max_length=50, unique=True)


class Title(CommonInfo):
    year = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    genres = models.ManyToManyField(Genre)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='titles'
    )
