from rest_framework.views import APIView
from rest_framework.response import Response
from administracao.services import service_servico
from ..serializers import service_serializer
from rest_framework import status as status_http


class Servico(APIView):
    def get(self, request, format=None):
        service = service_servico.listar_servicos()
        serializer_servico = service_serializer.ServiceSerializer(
            service, many=True
        )
        return Response(
            serializer_servico.data,
            status=status_http.HTTP_200_OK
        )
