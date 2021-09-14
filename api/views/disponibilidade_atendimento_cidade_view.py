from rest_framework.views import APIView
from rest_framework.response import Response
from ..services import cidade_atendimento_service


class DisponibilidadeAtendimentoCidade(APIView):
    def get(self, request, format=None):
        cep = self.request.query_params.get('cep')
        disponibilidade = cidade_atendimento_service.verificar_disponibilidade_cidade(
            cep
        )
        return Response({'disponibilidade': disponibilidade})
