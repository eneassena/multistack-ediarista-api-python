from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Usuario
from ..serializers.diaristas_localidade_serializer import DiaristasLocalidadeSerializer
from rest_framework import status as status_http
from ..services import cidade_atendimento_service as service_cidades
from ..pagination.diaristas_localidade_pagination import DiaristasLocalidadePagination


class DiaristasLocalidade(APIView, DiaristasLocalidadePagination):
    def get(self, request, format=None):
        cep = self.request.query_params.get('cep', None)
        diaristas = service_cidades.listar_diaristas_cidade(cep)
        resultado = self.paginate_queryset(diaristas, request)
        serialize_diarista_localidade = DiaristasLocalidadeSerializer(
            resultado, many=True, context={'request': request}
        )
        return self.get_paginated_response(serialize_diarista_localidade.data)
