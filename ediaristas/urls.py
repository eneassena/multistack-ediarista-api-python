from django.contrib import admin
from django.urls import path, include
from .views import index
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('administracao/', include('administracao.urls')),
    path('api/', include('api.urls')),

    # authentication JWT
    path('auth/token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
