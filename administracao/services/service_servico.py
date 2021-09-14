from ..models import Service


def listar_servicos():
    return Service.objects.all().order_by('posicao')
