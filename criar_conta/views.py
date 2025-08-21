from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import Criar_contaForm
from django.contrib import messages


def criar_conta_view(request : HttpRequest):
    if request.method == 'POST':
        form = Criar_contaForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('login')
            messages.success(request, 'Usuário cadastrado com sucesso!')
        else:
            form = Criar_contaForm()
    else:
        form = Criar_contaForm()
        
    return render(
        request,
        'criar_conta.html',
        {'criar_conta': form}
    )