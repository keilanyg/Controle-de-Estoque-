from django import forms
from django.contrib.auth import forms
from .models import Users

#Sobrescrever o User do django, adicionando o campo Cargo junto ao formulário do django
class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserCreationForm.Meta):
        model = Users
        
class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = Users