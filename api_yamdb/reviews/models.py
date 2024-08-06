from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from api_yamdb import constants
from api_yamdb.validators import validate_username_not_me, validate_max_year


class User(AbstractUser):
    username = models.CharField(
        max_length=constants.USERNAME_MAX_LENGTH,
        unique=True,
        validators=[UnicodeUsernameValidator(), validate_username_not_me],
    )
    email = models.EmailField(
        max_length=constants.EMAIL_MAX_LENGTH,
        unique=True)
    role = models.CharField(
        max_length=constants.MAX_ROLE_LENGTH,
        choices=constants.ROLES,
        default=constants.USER)
    bio = models.TextField(blank=True)

    @property
    def is_admin(self):
        return (self.role == constants.ADMIN
                or self.is_superuser or self.is_staff)

    class Meta(AbstractUser.Meta):
        verbose_name = 'пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class CommonInfo(models.Model):
    name = models.CharField(
        max_length=constants.NAME_MAX_LENGTH, verbose_name='Название'
    )

    class Meta:
        abstract = True
        ordering = ['name']

    def __str__(self):
        return self.name


class CommonInfoCategoryGenre(models.Model):
    slug = models.SlugField(unique=True, verbose_name='Слаг')

    class Meta:
        abstract = True


class Category(CommonInfo, CommonInfoCategoryGenre):

    class Meta(CommonInfo.Meta):
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


class Genre(CommonInfo, CommonInfoCategoryGenre):

    class Meta(CommonInfo.Meta):
        verbose_name = 'жанр'
        verbose_name_plural = 'Жанры'


class Title(CommonInfo):
    year = models.SmallIntegerField(
        validators=[validate_max_year], verbose_name='Год'
    )
    description = models.TextField(
        null=True, blank=True, verbose_name='Описание'
    )
    genre = models.ManyToManyField(
        Genre, through='TitleGenre', verbose_name='Жанр'
    )
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT,
        related_name='titles', verbose_name='Категория'
    )

    class Meta(CommonInfo.Meta):
        verbose_name = 'произведение'
        verbose_name_plural = 'Произведения'


class TitleGenre(models.Model):
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE
    )
    genre = models.ForeignKey(
        Genre, on_delete=models.PROTECT
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'жанр произведения'
        verbose_name_plural = 'Жанры произведения'


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
    score = models.PositiveSmallIntegerField(
        'Оценка', validators=[
            MinValueValidator(constants.MIN_REVIEW_SCORE),
            MaxValueValidator(constants.MAX_REVIEW_SCORE)
        ], help_text=(f'Введите целое число от {constants.MIN_REVIEW_SCORE} '
                      f'до {constants.MAX_REVIEW_SCORE}.')
    )

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
