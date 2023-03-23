from django.db import models
from django.contrib.auth.models import AbstractUser

#Autenticação do usuário
#Cria um novo campo, o cargo dentro da tabela Users
#Herdando ABSTRACTUSER do próprio django, sobrescrevendo essa classe
class Users(AbstractUser):
    choices_cargo = (('V', 'Vendedor'),
                     ('G', 'Gerente'))
    cargo = models.CharField(max_length=1, choices=choices_cargo)
    