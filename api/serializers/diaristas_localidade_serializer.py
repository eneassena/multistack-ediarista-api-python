from rest_framework import serializers
from ..models import Usuario


class DiaristasLocalidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('nome_completo', 'cpf', 'reputacao', 'foto_usuario')
