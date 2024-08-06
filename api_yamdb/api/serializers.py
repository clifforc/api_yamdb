from datetime import date

from django.contrib.auth import get_user_model
from django.contrib.auth.validators import UnicodeUsernameValidator
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api_yamdb import constants
from reviews.models import Category, Comment, Genre, Review, Title


User = get_user_model()


class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True,
        max_length=constants.USERNAME_MAX_LENGTH,
        validators=[UnicodeUsernameValidator()]
    )
    email = serializers.EmailField(
        required=True,
        max_length=constants.EMAIL_MAX_LENGTH
    )

    def validate(self, attr):
        username = attr['username']
        email = attr['email']

        if username == constants.NOT_ALLOWED_USERNAME:
            raise serializers.ValidationError(
                {"username": f"Использовать имя {username} "
                             "в качестве username запрещено."})
        elif (User.objects.filter(username=username).exists()
              and not User.objects.filter(email=email).exists()):
            raise serializers.ValidationError(
                {"username": "Пользователь "
                             f"с именем {username} уже существует"})
        if (User.objects.filter(email=email).exists()
                and not User.objects.filter(username=username).exists()):
            raise serializers.ValidationError(
                {"email": f"Пользователь с адресом {email} уже существует"}
            )
        return attr

    def create(self, validated_data):
        user, _ = User.objects.get_or_create(**validated_data)
        return user


class GetTokenSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True,
        max_length=constants.USERNAME_MAX_LENGTH,
    )
    confirmation_code = serializers.CharField(
        required=True,
        max_length=constants.CONFIRMATION_CODE_MAX_LENGTH
    )


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'bio', 'role')

    def validate_username(self, value):
        if value == constants.NOT_ALLOWED_USERNAME:
            raise serializers.ValidationError(
                {"username": f"Использовать имя '{value}' "
                             "в качестве username запрещено."})
        return value


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'slug')


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name', 'slug')


class TitleReadSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(required=True, many=True)
    category = CategorySerializer(required=True, many=False)
    rating = serializers.IntegerField(read_only=True, default=0)

    class Meta:
        model = Title
        fields = (
            'id', 'name', 'year', 'rating', 'description', 'genre', 'category'
        )


class TitleCreateSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        many=True,
        slug_field='slug',
        allow_empty=False,
        required=True,
        allow_null=False
    )
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug',
    )

    class Meta:
        model = Title
        fields = (
            'id', 'name', 'year', 'description', 'genre', 'category'
        )

    def validate_year(self, value):
        if value is not None and value > date.today().year:
            raise serializers.ValidationError(
                {value: ['Год произведения не может быть больше текущего!']}
            )
        return value


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date')

    def validate(self, data):
        if self.context.get('view').action == 'create':
            user = self.context.get('request').user
            title = self.context.get('view').kwargs.get('title_id')
            if user.reviews.filter(title=title).exists():
                raise ValidationError(
                    'Вы уже оставляли отзыв на это произведение.'
                )
        return data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')
