from rest_framework import viewsets, status 
from django.http import JsonResponse
from .models import Producto, Categoria, Lote, Historial, Lote_Historial
from .serializers import ProductoSerializer
from .queries import obtener_inventario
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import transaction

class listaProductos(viewsets.ReadOnlyModelViewSet):    #lista de los productos que necesito de los modelos
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

def inventario_view(request):               #me trae todos los datos del inventario
    inventario = obtener_inventario()
    return JsonResponse(inventario, safe=False)

@api_view(['POST']) 
def guardar_datos(request):
    try:
        with transaction.atomic():      #crear las instancias en orden de dependencia de llaves foraneas
            
            categoria = Categoria.objects.create(       #crear instancia de categoria
                nombre=request.data.get('nombreCategoria'))
            
            producto = Producto.objects.create(       #crear instancia de producto
                nombre=request.data.get('nombre'),
                proveedor=request.data.get('proveedor'),
                id_categoria=categoria)
            
            lote = Lote.objects.create(       #crear instancia de lote
                fecha_Rotacion=request.data.get('fecha_Rotacion'),
                estado=request.data.get('estado'),
                numero_lote=request.data.get('numero_lote'),
                id_Producto=producto)
            
            historial = Historial.objects.create()       #crear instancia de historial
            
            lote_Historial = Lote_Historial.objects.create(     #crear instancia de lote_historial
                id_lote=lote,
                id_historial=historial,
                cantidad = request.data.get('cantidad'),
                unidad_medida = request.data.get('unidad_medida'),
                precio_compra = request.data.get('precio_compra')
            )
        return Response({
            'mensaje': 'Datos guardados correctamente',
            'producto_id': producto.id,
            'lote_id': lote.id,
            'historial_id': historial.id
        })
    except Exception as e:return Response({'error': str(e)}, status=400)