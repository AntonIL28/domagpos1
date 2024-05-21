from django.urls import path
from . import views

urlpatterns = [
    #path('punto-venta/', views.POS, name="Punto Venta"),
    path('punto-venta2/', views.POS, name="POS2"),
    path('clientes/', views.clientes_view, name="Clientes"),
    path('add_cliente/', views.add_cliente_view, name="AddCliente"),
    path('edit_cliente/', views.edit_cliente_view, name="EditCliente"),
    path('delete_cliente/<str:id>', views.delete_cliente_view, name="DeleteCliente"),
    path('productos/', views.productos_view, name="Productos"),
    path('delete_producto/<int:id>', views.delete_producto_view, name="DeleteProducto"),
    path('add_producto/', views.add_producto_view, name="AddProducto"),
    path('editar_producto/<int:producto_id>', views.add_producto_view, name="EditarProducto"),
    
    #path('actualizar_producto/<int:id>', views.actualizar_producto, name="ActualizarProducto"),
    #path('export/', views.export_pdf_view, name="ExportPDF" ),
    #path('export/<id>/<iva>', views.export_pdf_view, name="ExportPDF" ),
]
