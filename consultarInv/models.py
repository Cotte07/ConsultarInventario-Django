from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('gerente', 'Gerente'),
        ('tendero', 'Tendero'),
        ('ayudante', 'Ayudante'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='ayudante')

class Categoria(models.Model):  #tabla categoria de la bd
    nombre = models.CharField(max_length=20)

class Producto(models.Model):   #tabla productos de la bd
    nombre =    models.CharField(max_length=30)
    proveedor = models.CharField(max_length=20)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, null=True )
    estado = models.BooleanField(default=True)  #True significa activo, False inactivo en inventario.

    def eliminar_del_inventario(self):  #funcion para cambiar el estado de los productos
        self.estado = False
        self.save()

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
    cantidad = models.DecimalField(max_digits=9, decimal_places=0)
    unidad_medida = models.CharField(max_length=20)
    precio_compra = models.DecimalField(max_digits=9, decimal_places=2)


