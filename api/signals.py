#imports
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import Usuario

"""
    @params sender, instance, created, **kwargs
    @return None
"""
def usuario_cadastrado(sender, instance, created, **kwargs):
    if created:
        assunto = 'Cadastro realizado com sucesso.'
        corpo_email = ''
        email_destino = [instance.email, ]
        email_remetente = 'desenvolvedoreneas2000@gmail.com'
        mensagem_html = render_to_string('05.03_email_cadastro.html', {
            'usuario': instance
        })
        send_mail(
            assunto, corpo_email, 
            email_remetente, email_destino, 
            mensagem_html,
            html_message=mensagem_html
        )


post_save.connect(usuario_cadastrado, sender=Usuario)
