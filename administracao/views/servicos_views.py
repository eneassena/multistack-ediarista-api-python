from django.shortcuts import redirect, render
from administracao.forms.servico_forms import ServicoForm
from administracao.models import Service
from django.contrib.auth.decorators import login_required


# cadrastando serviços
@login_required
def cadastrar_servico(request):
    if request.method == 'POST':  # verifica o método da requisição
        # se for post cria um formulário e passa os dados do formulário enviado em request.POST
        service_form = ServicoForm(request.POST)
        if service_form.is_valid():     # verifica se o formulário é valido para persistir-lo no bd
            service_form.save()  # se tudo tiver correto então salvamos no banco de dados
            # e por ultimo redireciona para uma pagina seguinte
            return redirect('listagem_services')
    else:
        service_form = ServicoForm()
    return render(request, 'services/service_form.html', {
        'service_form': service_form
    })


# listando serviços
@login_required
def listagem_services(request):
    list_services = Service.all_service()
    return render(request, 'services/service_list.html', {
        'list_services': list_services
    })


# editando serviço
@login_required
def editar_servico(request, service_id):
    servico = Service.objects.get(pk=service_id)
    service_form = ServicoForm(request.POST or None, instance=servico)
    if service_form.is_valid():
        service_form.save()
        return redirect('listagem_services')
    return render(request, 'services/service_form.html', {
        'service_form': service_form
    })
