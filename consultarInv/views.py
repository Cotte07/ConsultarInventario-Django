from django.shortcuts import render, redirect
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth import logout
from .models import Producto, Historial, Categoria, Lote, Lote_Historial, ConsultaProductos
from django.http.response import JsonResponse
from django import views
from .serializers import ProductoSerializer, LoteHistorialSerialiazer, ConsultaProductosSerializer


# Create your views here.
class vistaPrueba(viewsets.ViewSet):
    def list(self, request):
        return Response({"info": "oscar"}) #prueba para confirmar el funcionamiento del get 

class listaProductos(viewsets.ReadOnlyModelViewSet):    #lista de los productos que necesito de los modelos
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class listaLoteHistorial(viewsets.ReadOnlyModelViewSet): #lista para campos de loteHistorial
    queryset = Lote_Historial.objects.all()
    serializer_class = LoteHistorialSerialiazer

class ConsultaProductosViewSet(viewsets.ViewSet):      #lista de los campos de la consulta de productos
    
    def list(self, request):
        try:  

            productos = ConsultaProductos.obtener_datos_productos_raw()
            serializer = ConsultaProductosSerializer(productos, many=True)
            return Response(serializer.data)
        except Exception as e: 
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )