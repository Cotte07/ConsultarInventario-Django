from rest_framework import viewsets 
from django.http import JsonResponse
from .models import Producto, Categoria, Lote, Historial, Lote_Historial
from .serializers import ProductoSerializer
from .queries import obtener_inventario
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from django.db import transaction
from django.views.decorators.http import require_POST
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.views.decorators.csrf import csrf_exempt


class listaProductos(viewsets.ReadOnlyModelViewSet):    #lista de los productos que necesito de los modelos
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

def inventario_view(request):               #me trae todos los datos del inventario
    inventario = obtener_inventario()
    return JsonResponse(inventario, safe=False)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
@require_POST
def guardar_datos(request):
    try:
        with transaction.atomic():
            # Verificar que el usuario está autenticado
            if not request.user.is_authenticated:
                return Response({'error': 'Usuario no autenticado'}, status=401)
            
            categoria = Categoria.objects.create(
                nombre=request.data.get('nombreCategoria')
            )
            
            producto = Producto.objects.create(
                nombre=request.data.get('nombre'),
                proveedor=request.data.get('proveedor'),
                estado=request.data.get('estadoProducto'),
                id_categoria=categoria
            )
            
            lote = Lote.objects.create(
                fecha_Rotacion=request.data.get('fecha_Rotacion'),
                estado=request.data.get('estado'),
                numero_lote=request.data.get('numero_lote'),
                id_Producto=producto
            )
            
            historial = Historial.objects.create()
            
            lote_Historial = Lote_Historial.objects.create(
                id_lote=lote,
                id_historial=historial,
                cantidad=request.data.get('cantidad'),
                unidad_medida=request.data.get('unidad_medida'),
                precio_compra=request.data.get('precio_compra')
            )
            
            return Response({
                'mensaje': 'Datos guardados correctamente',
                'producto_id': producto.id,
                'lote_id': lote.id,
                'historial_id': historial.id
            })
    except Exception as e:
        return Response({'error': str(e)}, status=400)

@csrf_exempt  # Deshabilita la verificación CSRF en esta vista
@require_POST
@permission_classes([IsAuthenticated])  # Asegura que el usuario esté autenticado
@authentication_classes([TokenAuthentication])

def eliminar_producto(request, producto_id):        #funcion para desahibilitar la visibilidad del producto en el inventario como forma de 'eliminar'
    try:
        producto = Producto.objects.get(id=producto_id)
        producto.eliminar_del_inventario()  #cambia el estado del producto
        return JsonResponse({'success': True})
    except Producto.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Producto no encontrado'}, status=404)