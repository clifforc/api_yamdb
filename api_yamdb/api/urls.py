from django.urls import path, include
from rest_framework import routers
from .views import GenreViewSet, CategoryViewSet, TitleViewSet


router = routers.DefaultRouter()
router.register('genres', GenreViewSet)
router.register('categories', CategoryViewSet)
router.register('titles', TitleViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
