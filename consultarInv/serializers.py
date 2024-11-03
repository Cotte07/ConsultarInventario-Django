from rest_framework import serializers
from .models import Producto, Lote_Historial, Historial, Lote, Categoria
from datetime import datetime
from dateutil.relativedelta import relativedelta

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__' #llamamos todos los campos que queremos traer del modelo Producto

class LoteHistorialSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Lote_Historial
        fields = ['cantidad', 'unidad_medida', 'precio_compra'] #traemos los datos que necesitamos del modelo lote_historial

class HistorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historial
        fields = ['id', 'fecha_compra']  # Incluir el id y la fecha de compra en la serialización

class LoteSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Lote
        fields = ['id', 'fecha_Rotacion', 'estado', 'id_Producto', 'numero_lote']  # Campos que se incluirán

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fiels = ['id','nombre']
