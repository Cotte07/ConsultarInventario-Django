from django.db.models import Prefetch 
from typing import List, Dict, Any
from django.db.models.functions import Concat
from django.db.models.functions import ExtractDay, ExtractMonth, ExtractYear
from django.db.models import Value, CharField, F

from .models import Producto, Lote, Historial, Lote_Historial, Categoria


def obtener_inventario() -> List[Dict[Any, Any]]:
    """
    Obtiene el inventario completo con información detallada y fecha formateada.
    
    Returns:
        List[Dict]: Lista de diccionarios con la información del inventario,
        incluyendo la fecha en formato 'DD/MM/YYYY'
    """
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
            )
        )
        .values(
            'id_lote__id_Producto__nombre',
            'cantidad',
            'unidad_medida',
            'precio_compra',
            'fecha_formateada',
            'id_lote__id_Producto__proveedor',
            'id_lote__numero_lote',
            'id_lote__estado',
            'id_lote__id_Producto__id_categoria__nombre'
        )
    )
    
    return list(inventario)