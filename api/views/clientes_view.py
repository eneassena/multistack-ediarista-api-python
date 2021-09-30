from rest_framework.views import APIView
from rest_framework.response import Response


class ClientesView(APIView):
    def get(self, request, format=None):
        return Response("Cheguei aqui", status=200)

    def post(self, request, format=None):
        data = request.data
        if data:
            return Response(data, status=200)
        return Response("Not Found", status=404)

    def delete(self, request, format=None):
        return Response("Dados deletado com sucesso", status=200)

    def put(self, request, format=None):
        return Response("Dados atualizados com sucesso")
