import imp
from django.contrib import admin
from .models import Users
from django.contrib.auth import admin as admin_auth_django
from .forms import UserChangeForm, UserCreationForm


#Faz aparecer o formulário antigo, junto do campo Cargo, que foi adicionado

@admin.register(Users) #Registrar a model criada
class UsersAdmin(admin_auth_django.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    models = Users
    #Pra usar os campos que já existem e adicionar o campo no admin
    fieldsets = admin_auth_django.UserAdmin.fieldsets + (
        ('Cargo', {'fields': ('cargo',)}),
    )