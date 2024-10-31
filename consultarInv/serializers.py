from rest_framework import serializers
from .models import Producto, Lote_Historial

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__' #llamamos todos los campos que queremos traer del modelo Producto


class LoteHistorialSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Lote_Historial
        fields = ['cantidad', 'unidad_medida', 'precio_compra'] #traemos los datos que necesitamos del modelo lote_historial
