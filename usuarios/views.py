from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, get_user_model, login, logout
from app import views

# Create your views here.
from app.models import Pessoa
from usuarios.forms import RegistrarUsuarioForm


class RegistrarUsuarioView(View):

    template_name = 'registrar.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = RegistrarUsuarioForm(request.POST)

        if form.is_valid():
            dados_form = form.cleaned_data
            usuario = User.objects.create(username=dados_form['nome'], email=dados_form['email'], password=dados_form['senha'])
            pessoa = Pessoa(nome=dados_form['nome'],telefone=dados_form['telefone'],usuario=usuario)

            pessoa.save()
            return redirect('index')

        return render(request, self.template_name, {'form': form})

def logout(request):
    # Session is modified.
    del request.session['user']
    messages.success(request, 'Logout realizado com sucesso!')
    return HttpResponseRedirect('/login')

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        views.listagem()
    else:
        view.erro()
