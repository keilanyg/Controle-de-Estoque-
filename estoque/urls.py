from django.urls import path
from . import views

urlpatterns = [
    path('add_produto/', views.add_produto, name="add_produto"),
    path('ver_estoque/', views.ver_estoque, name="ver_estoque"),
    path('produto/<slug:slug>', views.produto, name="produto")
]
