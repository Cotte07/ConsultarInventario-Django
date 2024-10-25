from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth import logout
from .models import Producto, Historial, Categoria, Lote, Lote_Historial
from django.http.response import JsonResponse
from django import views
from .serializers import ProductoSerializer


# Create your views here.
class vistaPrueba(viewsets.ViewSet):
    def list(self, request):
        return Response({"info": "oscar"})

class listaProductos(viewsets.ViewSet):
    def list(self, request):
        productos = Producto.objects.all()  # Obtener todos los productos
        serializer = ProductoSerializer(productos, many=True)  # Serializar los productos
        return Response(serializer.data)  # Devolver los datos serializados en la respuesta

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