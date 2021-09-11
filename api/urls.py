from django.urls import path
from .views import diaristas_localidade_view

urlpatterns = [
    path('diaristas/localidade',
         diaristas_localidade_view.DiaristasLocalidade.as_view(), name='diaristas-localidade-list')
]
