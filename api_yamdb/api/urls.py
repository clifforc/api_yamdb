from django.urls import path, include
from rest_framework import routers
from api.views import AuthViewSet, CommentViewSet, ReviewViewSet

app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register(r'auth', AuthViewSet, basename='auth')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, 'title-reviews')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, 'review-comments'
)

v1_endpoints = [
    path('', include(router_v1.urls)),
]
urlpatterns = [
    path('v1/', include(v1_endpoints)),
]
