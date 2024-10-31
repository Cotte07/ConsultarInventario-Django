from rest_framework import viewsets, status
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Producto, Historial, Categoria, Lote, Lote_Historial
from django import views
from .serializers import ProductoSerializer, LoteHistorialSerialiazer
from .queries import obtener_inventario


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

def inventario_view(request):
    inventario = obtener_inventario()
    return JsonResponse(inventario, safe=False)