from django.contrib.auth import get_user_model
from rest_framework import status, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import SignUpSerializer, GetTokenSerializer
from .utils import send_confirmation_code

User = get_user_model()


class AuthViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['post'], url_path='signup')
    def signup(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            send_confirmation_code(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    from rest_framework.exceptions import NotFound

    @action(detail=False, methods=['post'], url_path='token')
    def token(self, request):
        serializer = GetTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.filter(
            username=serializer.validated_data['username']).first()
        if not user:
            raise NotFound("Пользователь не найден")
        if user.confirmation_code == serializer.validated_data[
            'confirmation_code']:
            refresh = RefreshToken.for_user(user)
            return Response({
                'token': str(refresh.access_token),
            })
        return Response({'error': 'Неверный код подтверждения'},
                        status=status.HTTP_400_BAD_REQUEST)
