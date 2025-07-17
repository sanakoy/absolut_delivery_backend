"""
URL configuration for delivery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.forms.widgets import static
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from delivery_absolute.views.login import login

urlpatterns = [
    path('admin/', admin.site.urls), # Эндпоинты для админки
    path('api/v1/', include('delivery_absolute.urls')), # Эндпоинты для доставок
    path('api/auth/login/', login, name='login'),  # эндпоинт для авторизации
    path('api/auth/token/', obtain_auth_token, name='api_token_auth'), # Эндпоинт для получения токена
]

