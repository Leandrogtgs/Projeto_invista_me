from django.shortcuts import render, HttpResponse, redirect

from .forms import InvestimentoForm

from .models import Investimento

from django.contrib.auth.decorators import login_required



def pagina_inicial(request):

    investimentos = {'investimentos': Investimento.objects.all()}

    return render(request, 'investimentos/investimentos.html', context=investimentos)

@login_required
def novo_investimento(request):
    

    if request.method == 'POST':

        formulario = InvestimentoForm(request.POST)

        if formulario.is_valid():

            formulario.save()

        return redirect('pagina_inicial')

    else:

        formulario_v = InvestimentoForm()

        formulario = {'formulario': formulario_v}

        return render(request, 'investimentos/novo_investimento.html', context=formulario)
    

@login_required
def exibir_detalhes(request, id_investimento):

    investimento = Investimento.objects.get(pk=id_investimento)

    return render(request, 'investimentos/detalhes_investimento.html', {'investimento': investimento})


@login_required
def editar_investimento(request, id_investimento):

    investimento = Investimento.objects.get(pk=id_investimento)

    if request.method == 'POST':

        formulario = InvestimentoForm(request.POST, instance=investimento)

        if formulario.is_valid():

            formulario.save()

        return redirect('pagina_inicial')
    else:

        formulario = InvestimentoForm(instance=investimento)

    return render(request, 'investimentos/novo_investimento.html', {'formulario': formulario})

@login_required
def excluir_investimento(request, id_investimento):

    investimento = Investimento.objects.get(pk=id_investimento)

    if request.method == 'POST':

        investimento.delete()

        return redirect('pagina_inicial')

    return render(request, 'investimentos/excluir_investimento.html', {'investimento': investimento})

