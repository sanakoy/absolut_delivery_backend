from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    # авторизация пользователя
    username = request.data.get('username')
    password = request.data.get('password')

    # проверка пользователя
    user = authenticate(username=username, password=password)
    if user:
        # создание токена
        token, _ = Token.objects.get_or_create(user=user)
        # возвращение токена
        return Response({
            'token': token.key,
            'user_id': user.id,
            'username': user.username
        })
    return Response({'error': 'Invalid credentials'}, status=400)