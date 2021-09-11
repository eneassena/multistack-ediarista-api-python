from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Usuario
from ..serializers.diaristas_localidade_serializer import DiaristasLocalidadeSerializer
from rest_framework import status as status_http
from ..services.cidade_atendimento_service import buscar_cidade_cep


class DiaristasLocalidade(APIView):
    def get(self, request, format=None):

        cep = self.request.query_params.get('cep', None)

        diaristas = Usuario.objects.filter(tipo_usuario=2)
        serialize_diarista_localidade = DiaristasLocalidadeSerializer(
            diaristas, many=True)
        return Response(buscar_cidade_cep(cep), status=status_http.HTTP_200_OK)
