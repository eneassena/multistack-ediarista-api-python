from django.contrib import admin
from django.urls import path, include
from .views import index


urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('administracao/', include('administracao.urls')),
    path('api/', include('api.urls')),
]
