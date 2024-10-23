from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Producto, Historial, Categoria, Lote, Lote_Historial
from django.http.response import JsonResponse
from django import views


# Create your views here.

def paginaPrincipal(request):       #vista para mostrar la pagina principal
    return render(request, 'PaginaPrincipal.html')

def lista_producto(request):        #vista para mostrar el contenido de las tablas del inventario
    productos = Producto.objects.all()
    historial = Historial.objects.all()
    categoria = Categoria.objects.all()
    lote = Lote.objects.all()
    loteHistorial = Lote_Historial.objects.all()

    context = {
        'productos': productos,
        'historial': historial,
        'categoria': categoria,
        'lote': lote,
        'loteHistorial': loteHistorial,
        }
    return render(request, 'PaginaPrincipal.html', context)

def exit(request):      #vista para salir y cerrar sesion 
    logout(request)
    return redirect('paginaPrincipal')