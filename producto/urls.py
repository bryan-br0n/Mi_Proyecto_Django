from django.urls import path
from producto import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('productos/', views.listadoProductos,name="productos"),
    path('productos/crear', views.crearProducto,name="crear_producto")
    path('productos/editar/<int:id>', views.editar_producto, name="editar_producto"),
    path('productos/eliminar/<int:id>', views.eliminar_producto, name="eliminar_producto")
]