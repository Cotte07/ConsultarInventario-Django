from django.contrib import admin 
from django.urls import path, re_path
from .views import agregarProductoNuevo
from . import views


urlpatterns = [
    path('nuevo/', agregarProductoNuevo)
]