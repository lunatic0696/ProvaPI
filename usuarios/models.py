from django.db import models
from django.contrib.auth.models import User
# Create your models here.


nivelpermissao=((1,"user"),(2,"admin"))

class Usuario(models.Model):
    pessoa = models.OneToOneField(User,related_name="usuário",on_delete=models.CASCADE)
    permissao = models.IntegerField(choices=nivelpermissao, default=1)

    @property
    def email(self):
        return self.user.email

    def __str__(self):
        return self.user.username