from django.contrib import admin
from .models import Producto, Lote_Historial, Lote, Categoria, Historial

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class HistorialAdmin(admin.ModelAdmin):
    list_display = ('fecha_compra',)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Lote_Historial)
admin.site.register(Lote)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Historial, HistorialAdmin)