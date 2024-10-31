from django.db.models.functions import Now, Concat, ExtractDay, ExtractMonth, ExtractYear, Extract
from django.db.models import F, Value, CharField, IntegerField, ExpressionWrapper, DurationField
from django.db.models.functions import Cast
from typing import List, Dict, Any
from .models import Lote_Historial

def obtener_inventario() -> List[Dict[Any, Any]]:
    
    inventario = (
        Lote_Historial.objects
        .select_related('id_lote', 'id_historial')
        .prefetch_related('id_lote__id_Producto__id_categoria')
        .annotate(
            dia=ExtractDay('id_historial__fecha_compra'),
            mes=ExtractMonth('id_historial__fecha_compra'),
            anio=ExtractYear('id_historial__fecha_compra'),
            fecha_formateada=Concat(
                F('dia'), Value('/'), F('mes'), Value('/'), F('anio'),
                output_field=CharField()
            ),
            tiempoBodega=ExpressionWrapper(
                Extract(Now() - F('id_historial__fecha_compra'), 'epoch') / 86400,  # 86400 segundos en un día
                output_field=IntegerField()
)
        )
        .values(
            'id_lote__id_Producto__nombre',
            'cantidad',
            'unidad_medida',
            'precio_compra',
            'fecha_formateada',
            'tiempoBodega',
            'id_lote__id_Producto__proveedor',
            'id_lote__numero_lote',
            'id_lote__estado',
            'id_lote__id_Producto__id_categoria__nombre'
        )
    )
    return list(inventario)