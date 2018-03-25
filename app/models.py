from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=255, null=False)

    email = models.CharField(max_length=255, null=False)

    telefone = models.CharField(max_length=255, null=True)

    usuario = models.OneToOneField(User, related_name="pessoa", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome