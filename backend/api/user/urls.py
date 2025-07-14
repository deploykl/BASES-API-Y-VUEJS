from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from api.user.views import LoginView1, LoginView
from django.contrib.auth import views as auth_views  # Importa esto

router = DefaultRouter()

urlpatterns = [  
    #path('profile/', UserProfileView.as_view(), name='profile'),
    path('login/', LoginView.as_view(), name='login'),  # Esta es la ruta con nombre 'login'
    #path('register/', RegisterView.as_view(), name='register'),
    #path('logout/', LogoutView.as_view(), name='logout'),
    #path('password/reset/', PasswordResetRequestView.as_view(), name='password-reset'),
    #path('password/reset/confirm/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    
    # Añade estas rutas para el login tradicional
path('accounts/login/', auth_views.LoginView1.as_view(template_name='login.html'), name='login-api'),
] + router.urls


