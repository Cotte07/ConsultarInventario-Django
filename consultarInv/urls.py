from django.contrib import admin 
from django.urls import path
from .views import paginaPrincipal
from . import views


urlpatterns = [
    path('pag', paginaPrincipal, name='paginaPrincipal'),
    path('logout/', exit, name= 'exit'),
    path('inventario/', views.lista_producto, name='productos')
]