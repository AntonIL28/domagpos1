from django.urls import path
from . import views
from .views import get_data

urlpatterns = [
    #path('punto-venta/', views.POS, name="Punto Venta"),
    path('punto-venta2/', views.POS, name="POS2"),
    path('clientes/', views.clientes_view, name="Clientes"),
    path('add_cliente/', views.add_cliente_view, name="AddCliente"),
    path('edit_cliente/', views.edit_cliente_view, name="EditCliente"),
    path('delete_cliente/<str:id>', views.delete_cliente_view, name="DeleteCliente"),
    path('productos/', views.productos_view, name="Productos"),
    path('add_producto/', views.add_producto_view, name="AddProducto"),
    path('delete_producto/<str:id>', views.delete_producto_view, name="DeleteProducto"),
    path('get_data/', get_data, name='get_data'),
    path('buscar/', views.buscar_cliente, name='buscar'),
    path('buscar_p/', views.buscar_producto, name='buscar_p'),
    path('seleccionar_elemento/<int:id>/', views.seleccionar, name='seleccionar_elemento'),
    path('venta/', views.venta, name='venta'),
    #path('export/', views.export_pdf_view, name="ExportPDF" ),
    #path('export/<id>/<iva>', views.export_pdf_view, name="ExportPDF" ),
]
