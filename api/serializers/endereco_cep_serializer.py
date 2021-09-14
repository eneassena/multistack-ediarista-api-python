from rest_framework.serializers import BaseSerializer


class EnderecoCepSerializer(BaseSerializer):
    def to_representation(self, instance):
        return {
            "cep": instance['cep'],
            "localidade": instance['localidade'],
            "bairro": instance['bairro'],
            "logradouro": instance['logradouro'],
            "uf": instance['uf'],
            "complemento": instance['complemento'],
            "ibge": instance['ibge']
        }
