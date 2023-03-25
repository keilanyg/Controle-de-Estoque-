from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields =  "__all__"
        widgets = {
            "nome":forms.TextInput(attrs={"class": "form-control"}),
            "categoria":forms.Select(attrs={"class": "form-control"}),
            "quantidade":forms.Select(attrs={"class": "form-control"}),
            "preco_compra":forms.TextInput(attrs={"class": "form-control"}),
            "preco_venda":forms.TextInput(attrs={"class": "form-control"}),
            "slug":forms.TextInput(attrs={"class": "form-control"}),
        }
        