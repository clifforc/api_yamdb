from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views
from .views import GenreViewSet, CategoryViewSet


router = routers.DefaultRouter()
router.register('genres', GenreViewSet)
router.register('categories', CategoryViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
