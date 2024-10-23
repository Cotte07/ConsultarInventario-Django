from django.contrib import admin 
from django.urls import path, re_path
from .views import paginaPrincipal
from . import views


urlpatterns = [
    path('logout/', exit, name= 'exit'),                        #dirrecion para regresar al login 
    path('inventario/', views.lista_producto, name = 'producto') #dirrecion url para ver el inventario
]