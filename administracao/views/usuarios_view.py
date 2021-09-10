from administracao.forms.usuarios_form import CadastroUsuarioForm, EditarUsuarioForm
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required


@login_required
def cadastrar_usuario(request):
    if request.method == "POST":
        cadastro_form_usuario = CadastroUsuarioForm(request.POST)
        if cadastro_form_usuario.is_valid():
            cadastro_form_usuario.save()
            return redirect('listar_usuario')
    else:
        cadastro_form_usuario = CadastroUsuarioForm()
    return render(request, 'usuarios/form_usuarios.html', {'cadastro_usuario_form': cadastro_form_usuario})


@login_required
def listar_usuario(request):
    User = get_user_model()
    usuarios = User.objects.filter(is_superuser=True)
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})


@login_required
def editar_usuarios(request, usuario_id):
    User = get_user_model()
    usuario = User.objects.get(id=usuario_id)
    editar_usuario_form = EditarUsuarioForm(request.POST or None, instance=usuario)
    if editar_usuario_form.is_valid():
        editar_usuario_form.save()
        return redirect('listar_usuario')
    return render(request, 'usuarios/form_usuarios.html', {'cadastro_usuario_form': editar_usuario_form})


@login_required
def alterar_senha_done(request):
    return render(request, 'registration/password_change_done.html')
