from django.contrib import admin 
from django.urls import path
from .views import paginaPrincipal
from . import views


urlpatterns = [
    path('logout/', exit, name= 'exit'),                        #dirrecion para regresar al login 
    path('inventario/', views.lista_producto, name='productos') #dirrecion url para ver el inventario
]