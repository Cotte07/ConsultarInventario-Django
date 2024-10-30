from django.db import models
from django.db.models import F
from django.db.models.functions import Coalesce

# Create your models here.

class Categoria(models.Model):  #tabla categoria de la bd
    nombre = models.CharField(max_length=20)

class Producto(models.Model):   #tabla productos de la bd
    nombre =    models.CharField(max_length=30)
    proveedor = models.CharField(max_length=20)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, null=True )

class Historial(models.Model):      #tabla historial de la bd
    fecha_compra = models.DateTimeField(auto_now_add=True)

class Lote(models.Model):   #tabla lote de la bd
    fecha_Rotacion = models.DateField(null = True, blank= True )
    estado = models.CharField(max_length=20, blank=True)
    id_Producto = models.ForeignKey(Producto, on_delete=models.PROTECT, null=True)
    numero_lote = models.DecimalField(max_digits=10, decimal_places=0)

class Lote_Historial(models.Model):     #tabla intermedia entre lote e historial
    id_lote = models.ForeignKey(Lote, on_delete=models.PROTECT, null=True)
    id_historial = models.ForeignKey(Historial, on_delete=models.PROTECT, null=True)
    cantidad = models.DecimalField(max_digits=9, decimal_places=2)
    unidad_medida = models.CharField(max_length=20)
    precio_compra = models.DecimalField(max_digits=9, decimal_places=2)


#consulta que trae todos los datos
class ConsultaProductos(models.Model):
    class Meta:
        managed = False  # No crear tabla en la base de datos
    
    @staticmethod
    def obtener_datos_productos_raw():
        """
        Obtiene los datos de productos usando SQL raw
        """
        return Lote_Historial.objects.raw("""
            SELECT 
                lh.id,
                p.nombre as nombre_producto,
                lh.cantidad,
                lh.unidad_medida,
                lh.precio_compra,
                l.fecha_Rotacion,
                l.estado,
                l.numero_lote,
                h.fecha_compra,
                c.nombre as nombre_categoria,
                p.proveedor
            FROM Lote_Historial lh
            INNER JOIN Lote l ON lh.id_lote_id = l.id
            INNER JOIN Producto p ON l.id_Producto_id = p.id
            INNER JOIN Categoria c ON p.id_categoria_id = c.id
            INNER JOIN Historial h ON lh.id_historial_id = h.id
        """)