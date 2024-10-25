# serializers.py
from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'  #  especifica los campos que quieras, por ejemplo: ['id', 'nombre', 'precio', 'descripcion']
