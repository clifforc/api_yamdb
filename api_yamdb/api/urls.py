from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthViewSet


router_v1 = DefaultRouter()
router_v1.register(r'auth', AuthViewSet, basename='auth')
urlpatterns = [
    path('v1/', include(router_v1.urls))
]
