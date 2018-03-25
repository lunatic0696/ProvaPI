from django.shortcuts import render
from app.models import *
from django.contrib.auth import authenticate, get_user_model, login, logout



# Create your views here.

def index(request):
    return render(request, 'index.html')

def exibirPessoa(request, pessoa_id):
    pessoa = Pessoa.objects.get(id=pessoa_id)
    return render(request, 'pessoa.html',{'app' : pessoa})

def listagem(request):
    return render(request, 'listagem.html', {'pessoas': Pessoa.objects.all()})

def LoginView(request):
    return render(request, 'formulario.html')

def adicionar(request, pessoa):
    pessoa.save()

def deletar(request, pessoa):
    pessoa.delete()

def erro(request):
    return render(request, 'erro.html')