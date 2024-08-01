from django.contrib.auth import get_user_model
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination

from .serializers import UserSerializer
from .permissions import IsAdmin

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdmin,)
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['$username']
