from django.contrib import admin 
from django.urls import path, include
from .views import vistaPrueba, listaProductos, listaLoteHistorial, ConsultaProductosViewSet
from . import views
from rest_framework.routers import DefaultRouter

Vista1 = vistaPrueba.as_view({'get': 'list'})
Vista2 = listaProductos.as_view({'get': 'list'})

router = DefaultRouter()
router.register(r'producto',listaProductos)
router.register(r'loteHistorial',listaLoteHistorial)
router.register(r'consulta-productos',ConsultaProductosViewSet, basename='consulta-productos')

urlpatterns = [
    path('vista1/', Vista1),
    path('vista2/', Vista2),
    path('producto/', include(router.urls))
]