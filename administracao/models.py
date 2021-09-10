from django.db import models

# Create your models here.


class Service(models.Model):

    ICONE_CHOICES = (
        ('twf-cleaning-1', 'twf-cleaning-1'),
        ('twf-cleaning-2', 'twf-cleaning-2'),
        ('twf-cleaning-3', 'twf-cleaning-3')
    )

    nome = models.CharField(
        max_length=50, null=False, blank=False
    )
    valor_minimo = models.DecimalField(
        max_digits=5, decimal_places=2, null=False, blank=False
    )
    qtd_horas = models.IntegerField(
        null=False, blank=False
    )
    porcentagem_comissao = models.DecimalField(
        max_digits=5, decimal_places=2,  null=False, blank=False
    )
    horas_quarto = models.IntegerField(
        null=False, blank=False
    )
    valor_quarto = models.DecimalField(
        max_digits=5, decimal_places=2,  null=False, blank=False
    )
    horas_sala = models.IntegerField(
        null=False, blank=False
    )
    valor_sala = models.DecimalField(
        max_digits=5, decimal_places=2,  null=False, blank=False
    )
    horas_banheiro = models.IntegerField(
        null=False, blank=False
    )
    valor_banheiro = models.DecimalField(
        max_digits=5, decimal_places=2,  null=False, blank=False
    )
    horas_quintal = models.IntegerField(
        null=False, blank=False
    )
    valor_quintal = models.DecimalField(
        max_digits=5, decimal_places=2,  null=False, blank=False
    )
    horas_outros = models.IntegerField(
        null=False, blank=False
    )
    valor_outros = models.DecimalField(
        max_digits=5, decimal_places=2,  null=False, blank=False
    )
    icone = models.CharField(
        null=False, blank=False, choices=ICONE_CHOICES,  max_length=14
    )
    posicao = models.IntegerField(
        null=False
    )

    @staticmethod
    def all_service():
        return Service.objects.all()
