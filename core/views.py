from django.shortcuts import render, redirect
from core.models import Ativos
from core.forms import AtivosForm

def lista_ativos(request):
    ativos = Ativos.objects.all()
    return render(request, 'lista_ativos.html', {'ativos': ativos})

def adicionar_ativo(request):
    if request.method == 'POST':
        form = AtivosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista-ativos')
    else:
        form = AtivosForm()
    return render(request, 'adicionar_ativo.html', {'form': form})

def editar_ativo(request, id):
    ativo = Ativos.objects.get(id=id)
    if request.method == 'POST':
        form = AtivosForm(request.POST, instance=ativo)
        if form.is_valid():
            form.save()
            return redirect('lista-ativos')
    else:
        form = AtivosForm(instance=ativo)
    return render(request, 'editar_ativo.html', {'form': form, 'ativo': ativo})

def excluir_ativo(request, id):
    ativo = Ativos.objects.get(id=id)
    if request.method == 'POST':
        ativo.delete()
        return redirect('lista-ativos')
    return render(request, 'excluir_ativo.html', {'ativo': ativo})
