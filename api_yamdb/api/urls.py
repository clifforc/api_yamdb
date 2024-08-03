from django.urls import path, include
from rest_framework import routers

from api.views import SignUpViewSet, CommentViewSet, ReviewViewSet, \
    GenreViewSet, CategoryViewSet, TitleViewSet, UserViewSet, GetTokenViewSet

app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register(r'auth/signup', SignUpViewSet, basename='signup')
router_v1.register(r'auth/token', GetTokenViewSet, basename='token')
router_v1.register(r'users', UserViewSet, basename='user')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, 'title-reviews')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, 'review-comments'
)
router_v1.register('genres', GenreViewSet)
router_v1.register('categories', CategoryViewSet)
router_v1.register('titles', TitleViewSet)

v1_endpoints = [
    path('', include(router_v1.urls)),
]
urlpatterns = [
    path('v1/', include(v1_endpoints)),
]
