"""ProvaFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from usuarios.views import RegistrarUsuarioView
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('listagem/',views.listagem,name='listagem'),
    path('erro',views.erro,name='erro'),
    path('verpessoa/<int:pessoa_id>',views.exibirPessoa,name='exibirpessoa'),
    path('registrar/',RegistrarUsuarioView.as_view(),name="registrar"),
    path(r'^login/$',views.LoginView.as_view(template_name='login.html'),name = "login"),
    path(r'^logout/$',views.LogoutView.as_view(template_name='login.html'),name="logout"),
]