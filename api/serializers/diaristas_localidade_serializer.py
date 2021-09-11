from rest_framework import serializers
from ..models import Usuario


class DiaristasLocalidadeSerializer(serializers.ModelSerializer):
    cidade = serializers.SerializerMethodField()

    class Meta:
        model = Usuario
        fields = ('name_completo', 'reputacao', 'foto_usuario', 'cidade')

    def get_cidade(self, obj):
        return "Feira de Santana"
