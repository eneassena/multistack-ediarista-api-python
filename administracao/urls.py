from django.urls import path, reverse_lazy
from administracao.views.servicos_views import *
from administracao.views.usuarios_view import (
    cadastrar_usuario,
    listar_usuario,
    editar_usuarios,
    alterar_senha_done
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('service/cadastrar/', cadastrar_servico, name='cadastrar_servico'),
    path('service/list/', listagem_services, name='listagem_services'),
    path('service/editar/<int:service_id>/',
         editar_servico, name='editar_servico'),
    path('usuarios/cadastrar/', cadastrar_usuario, name='cadastrar_usuarios'),
    path('usuarios/listar/', listar_usuario, name='listar_usuario'),
    path('usuarios/editar/<int:usuario_id>/',
         editar_usuarios, name='editar_usuarios'),
    path('authenticacao/login/',
         auth_views.LoginView.as_view(), name='login_usuario'),
    path('authenticacao/logout/',
         auth_views.LogoutView.as_view(), name="usuario_logout"),

    # resetar senha
    path('alterar_senha/', auth_views.PasswordChangeView.as_view(
        success_url=reverse_lazy('alterar_senha_done')
    ), name="alterar_senha"),
    path('alterar_senha_done/', alterar_senha_done, name='alterar_senha_done'),
    path('resetar_senha/', auth_views.PasswordResetView.as_view(),
         name='resetar_senha'),
    path('resetar_senha/sucesso/', auth_views.PasswordResetDoneView.as_view(),
         name='resetar_senha_sucesso'),
    path('resetar_senha/<str:uidb64>/<str:token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='resetar_senha_confirmar'),
    path('resetar_senha/feito/', auth_views.PasswordChangeDoneView.as_view(),
         name='resetar_senha_feito'),
]
