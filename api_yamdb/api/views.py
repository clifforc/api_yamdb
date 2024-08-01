from rest_framework import viewsets, filters
from reviews.models import Genre, Category, Title

from .serializers import (CategorySerializer, GenreSerializer,
                          TitleCreateSerializer, TitleReadSerializer)


class CommonInfo(viewsets.ModelViewSet):
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class GenreViewSet(CommonInfo):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class CategoryViewSet(CommonInfo):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleReadSerializer

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return TitleCreateSerializer
        return TitleReadSerializer
