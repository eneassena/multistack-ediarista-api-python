from django.urls import path
from .views import (
    diaristas_localidade_view,
    endereco_cep_view,
    disponibilidade_atendimento_cidade_view as disponibilidade_cidade_view,
    servico_view,
    inicio_view
)

# urls padrão da api
urlpatterns = [
    path('diaristas/localidades',
         diaristas_localidade_view.DiaristasLocalidade.as_view(),
         name='diaristas-localidades-list'
         ),
    path('diaristas/enderecos/',
         endereco_cep_view.EnderecoCep.as_view(),
         name='endereco-cep-list'
         ),
    path('diaristas/disponibilidade',
         disponibilidade_cidade_view.DisponibilidadeAtendimentoCidade.as_view(),
         name='disponibilidade-atendimento-cidade-list'
         ),
    path('diaristas/servicos/',
         servico_view.Servico.as_view(),
         name='servico-list'
         ),
    path('', inicio_view.Inicio.as_view(), name='inicio')
]
