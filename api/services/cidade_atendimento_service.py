import requests
import json
from rest_framework import serializers
from ..models import CidadesAtendimento


def listar_diaristas_cidade(cep):
    codigo_ibge = buscar_cidade_cep(cep)['ibge']
    try:
        cidade = CidadesAtendimento.objects.get(codigo_ibge=codigo_ibge)
        return cidade.usuario.filter(tipo_usuario=2).order_by('-reputacao')
    except CidadesAtendimento.DoesNotExist:
        return []


def buscar_cidade_cep(cep: int):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    requisicao = requests.get(url)

    if requisicao.status_code == 400:
        raise serializers.ValidationError({"detail": "erro ao buscar o cep"})
    cidade_api = json.loads(requisicao.content)

    if 'erro' in cidade_api:
        raise serializers.ValidationError({
            'detail': 'o CEP informado não foi encontrado'
        })

    return cidade_api
