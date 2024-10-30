# serializers.py
from rest_framework import serializers
from .models import Producto, Lote_Historial, ConsultaProductos

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__' #llamos todos los campos que queremos traer del modelo Producto


class LoteHistorialSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Lote_Historial
        fields = ['cantidad', 'unidad_medida', 'precio_compra'] #traemos los datos que necesitamos del modelo lote_historial

class ConsultaProductosSerializer(serializers.Serializer):      #serializamos los datos para pasarlos a formato JSON
    nombre_producto = serializers.CharField(max_length=30)
    cantidad = serializers.DecimalField(max_digits=9, decimal_places=2)
    unidad_medida = serializers.CharField(max_length=20)
    precio_compra = serializers.DecimalField(max_digits=9, decimal_places=2)
    fecha_rotacion = serializers.DateField(allow_null=True)
    estado = serializers.CharField(max_length=20)
    numero_lote = serializers.DecimalField(max_digits=10, decimal_places=0)
    fecha_compra = serializers.DateTimeField()
    nombre_categoria = serializers.CharField(max_length=20)
    proveedor = serializers.CharField(max_length=20)

    def to_representation(self, instance):

        data = super().to_representation(instance)
        
        if data['fecha_compra']:
            data['fecha_compra'] = data['fecha_compra'].strftime("%Y-%m-%d %H:%M:%S")
            
        if data['fecha_rotacion']:
            data['fecha_rotacion'] = data['fecha_rotacion'].strftime("%Y-%m-%d")
            
        data['cantidad'] = float(data['cantidad'])
        data['precio_compra'] = float(data['precio_compra'])
        
        return data

    class Meta:
        model = ConsultaProductos
        fields = ['nombre_producto','cantidad','unidad_medida','precio_compra','fecha_rotacion','estado','numero_lote','fecha_compra','nombre_categoria','proveedor']