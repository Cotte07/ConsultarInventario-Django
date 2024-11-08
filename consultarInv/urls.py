from django.contrib import admin 
from django.urls import path, include
from .views import  listaProductos, inventario_view, eliminar_producto
from rest_framework.routers import DefaultRouter
from .import views
from rest_framework.authtoken import views as auth_views

router = DefaultRouter()
router.register(r'producto',listaProductos)

urlpatterns = [
    path('inventario/', inventario_view, name='inventario'),
    path('producto/', include(router.urls)),
    path('guardarDatos/', views.guardar_datos, name='guardar_datos'),
    path('eliminar_producto/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('api-token-auth/', auth_views.obtain_auth_token),
]