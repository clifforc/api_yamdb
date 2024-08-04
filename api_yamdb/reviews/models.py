from datetime import date

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class User(AbstractUser):
    ROLES = (
        ('user', 'User'),
        ('moderator', 'Moderator'),
        ('admin', 'Admin')
    )

    email = models.EmailField(max_length=254, unique=True)
    role = models.CharField(max_length=20, choices=ROLES, default='user')
    bio = models.TextField(blank=True)
    confirmation_code = models.CharField(max_length=10, blank=True)

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
    year = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(date.today().year)
        ], help_text="Введите год произведения, не больше текущего."
    )
    description = models.TextField(null=True, blank=True)
    genre = models.ManyToManyField(Genre)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='titles'
    )


class ReviewCommentBaseModel(models.Model):
    text = models.TextField('Текст', help_text='Текст отзыва')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name='Автор')
    pub_date = models.DateTimeField('Дата и время публикации',
                                    auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ['-pub_date']


class Review(ReviewCommentBaseModel):
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, verbose_name='Произведение'
    )
    score = models.IntegerField('Оценка', validators=[
        MinValueValidator(1),
        MaxValueValidator(10)
    ], help_text="Введите целое число от 1 до 10.")

    class Meta(ReviewCommentBaseModel.Meta):
        default_related_name = 'reviews'
        verbose_name = 'отзыв'
        verbose_name_plural = 'Отзывы'
        constraints = [
            models.UniqueConstraint(fields=['title', 'author'],
                                    name='unique_for_title')
        ]


class Comment(ReviewCommentBaseModel):
    review = models.ForeignKey(Review, on_delete=models.CASCADE,
                               verbose_name='Отзыв')

    class Meta(ReviewCommentBaseModel.Meta):
        default_related_name = 'comments'
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'
