from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import InvalidToken
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from django.utils import timezone
from django.utils.crypto import get_random_string
from datetime import timedelta
from django.core.mail import send_mail
from django.conf import settings
from api.user.serializers import *

User = get_user_model()

class LoginView(APIView):
    permission_classes = [AllowAny]  # Permitir acceso sin autenticación previa

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response(
                {'detail': 'Las credenciales de autenticación no se proveyeron.'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.filter(username=username).first()

        if user is None:
            return Response(
                {'detail': 'Usuario no encontrado'}, 
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        if not user.check_password(password):
            return Response(
                {'detail': 'Contraseña incorrecta'}, 
                status=status.HTTP_401_UNAUTHORIZED
            )

        # Verificar si el usuario está activo
        if not user.is_active:
            return Response(
                {'detail': 'Cuenta desactivada'}, 
                status=status.HTTP_403_FORBIDDEN
            )

        # Permitir acceso si es staff O superusuario
        if not user.is_staff and not user.is_superuser:
            return Response(
                {'detail': 'Acceso restringido a administradores'},
                status=status.HTTP_403_FORBIDDEN
            )

        # Generar tokens JWT
        refresh = RefreshToken.for_user(user)

        user_data = {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'is_superuser': user.is_superuser,
            'is_staff': user.is_staff,
        }

        return Response(user_data, status=status.HTTP_200_OK)
    
class LoginView1(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        # Para peticiones GET (cuando se accede desde el navegador)
        return render(request, 'login.html', {'next': request.GET.get('next', '')})

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is None:
            return Response({'detail': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

        # Si es una petición HTML
        if request.accepted_renderer.format == 'html':
            from django.contrib.auth import login
            login(request, user)  # Esto crea la sesión tradicional
            next_url = request.POST.get('next', '/api/schema/swagger/')
            return HttpResponseRedirect(next_url)
        
        # Si es API (devuelve JWT)
        refresh = RefreshToken.for_user(user)
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'is_superuser': user.is_superuser,
            'is_staff': user.is_staff,
        })