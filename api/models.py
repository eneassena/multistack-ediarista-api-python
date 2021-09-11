import uuid
import os
from django.core import validators
from django.db import models
from django.contrib.auth.models import AbstractUser
from localflavor.br.models import BRCPFField
from django.core.validators import validate_image_file_extension


def nome_arquivo_foto(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid(), ext)
    return os.path.join('usuarios', filename)


def nome_arquivo_documento(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid(), ext)
    return os.path.join('documentos', filename)


class Usuario(AbstractUser):
    TIPO_USUARIO_CHOICES = (
        (1, "Cliente"),
        (2, "Diarista")
    )

    nome_completo = models.CharField(max_length=255, null=False, blank=False)
    cpf = BRCPFField(null=True, unique=True)
    nascimento = models.DateField(null=False, blank=False)
    email = models.EmailField(null=True, blank=False, unique=True)
    telefone = models.CharField(max_length=11, null=False, blank=False)
    tipo_usuario = models.IntegerField(
        choices=TIPO_USUARIO_CHOICES, null=False, blank=False)
    reputacao = models.FloatField(null=False, blank=False, default=5)
    chave_pix = models.CharField(null=True, blank=True, max_length=255)
    foto_usuario = models.ImageField(null=False, upload_to=nome_arquivo_foto,
                                     validators=[validate_image_file_extension, ])
    foto_documento = models.ImageField(null=False, upload_to=nome_arquivo_documento,
                                       validators=[validate_image_file_extension, ])


class CidadesAtendimento(models.Model):
    codigo_bge = models.IntegerField(null=False, blank=False)
    cidade = models.CharField(max_length=100, null=False, blank=False)
    estado = models.CharField(max_length=2, null=False, blank=False)
    usuario = models.ManyToManyField(Usuario, related_name='cidades_atendidas')
