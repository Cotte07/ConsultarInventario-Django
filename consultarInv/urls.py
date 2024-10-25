from django.contrib import admin 
from django.urls import path, re_path
from .views import paginaPrincipal, vistaPrueba
from . import views

Vista1 = vistaPrueba.as_view({'get': 'list'})

urlpatterns = [
    path('logout/', exit, name= 'exit'),                        #dirrecion para regresar al login 
    path('inventario/', views.lista_producto), #dirrecion url para ver el inventario
    path('vista1/', Vista1)
]