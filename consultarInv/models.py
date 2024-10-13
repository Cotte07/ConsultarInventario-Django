from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre =    models.CharField(max_length=30)
    Proveedor = models.CharField(max_length=20)

    class Meta:
        db_table = 'producto'