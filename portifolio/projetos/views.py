from django.shortcuts import render


def index(request):
    return render(request, 'projetos/index.html')

def projetos(request):
    projetos = {
        1 : 'Usando Selenium em Python 3',
        2 : 'Usando Dicionários em Python 3',
        3 : 'Usando Listas em Python 3',
        4 : 'API de clima/temperatura em Python 3'
    }

    dados = {
        'desc_projetos' : projetos
    }

    return render(request, 'projetos/projetos.html' dados)

def projeto_detalhes(request):
    return render(request, 'projetos/projeto_detalhes.html')
