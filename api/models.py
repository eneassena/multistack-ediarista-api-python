import uuid
import os

from django.db import models
from django.contrib.auth.models import AbstractUser
from localflavor.br.models import BRCPFField
from django.core.validators import validate_image_file_extension
from .managers import diarista_managers
from django.contrib.auth.models import UserManager

def nome_arquivo_foto(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)

    return os.path.join('usuarios', filename)


def nome_arquivo_documento(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)

    return os.path.join('documentos', filename)

class ExempleTable(models.Model):
    nome_field = models.CharField(max_length=150, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False)



class Usuario(AbstractUser):
    TIPO_USUARIO_CHOICES = (
        (1, "Cliente"),
        (2, "Diarista")
    )

    username = None
    name_completo = models.CharField(max_length=255, null=True, blank=False)
    cpf = BRCPFField(null=True, unique=True, blank=False)
    nascimento = models.DateField(null=True, blank=False)
    email = models.EmailField(null=True, blank=False, unique=True)
    telefone = models.CharField(max_length=11, null=True, blank=False)
    tipo_usuario = models.IntegerField(
        choices=TIPO_USUARIO_CHOICES, null=True, blank=False)
    reputacao = models.FloatField(null=True, blank=False, default=5)
    chave_pix = models.CharField(null=True, blank=True, max_length=255)
    foto_usuario = models.ImageField(null=True, upload_to=nome_arquivo_foto,
                                     validators=[validate_image_file_extension, ])
    foto_documento = models.ImageField(null=True, upload_to=nome_arquivo_documento,
                                       validators=[validate_image_file_extension, ])
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        'nome_completo', 'cpf',
        'telefone', 'tipo_usuario',
        'reputacao', 'chave_pix',
        'foto_usuario', 'foto_documento'
    ]

    objects = UserManager()
    diarista_object = diarista_managers.DiaristaManager()


class CidadesAtendimento(models.Model):
    codigo_ibge = models.IntegerField(null=False, blank=False)
    cidade = models.CharField(max_length=100, null=False, blank=False)
    estado = models.CharField(max_length=2, null=False, blank=False)
    usuario = models.ManyToManyField(Usuario, related_name='cidades_atendidas')
