from django.contrib import admin
from main.models import dir_Ciudad, dir_Colonia, dir_Estado, Productos, Cliente
from main.models import Familia, Marca, UnidadMedida, Proveedor, TipoCambio

"""class ClienteAdmin(admin.ModelAdmin):
    list_display = ('razon', 'telefono')
    search_fields = ['razon']
    readonly_fields = ('created', 'updated')
    filter_horizontal =()
    list_filter =()
    fieldsets =()
admin.site.register(Cliente, ClienteAdmin)

class ProductosAdmin(admin.ModelAdmin):
    list_display = ('description')
    search_fields = ['description']
    readonly_fields = ('created', 'updated')
    filter_horizontal =()
    list_filter =()
    fieldsets =()
admin.site.register(Productos, ProductosAdmin)

class EstadoAdmin(admin.ModelAdmin):
    list_display = ['nombre','codigo']
    search_fields = ['nombre']
    readonly_fields = ()
    filter_horizontal =()
    list_filter =()
    fieldsets =()
admin.site.register(dir_Estado, EstadoAdmin) 

class CiudadAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']
    readonly_fields = ()
    filter_horizontal =()
    list_filter =()
    fieldsets =()
admin.site.register(dir_Ciudad, CiudadAdmin) 

class ColoniaAdmin(admin.ModelAdmin):
    list_display = ['nombre','cod_postal']
    search_fields = ['nombre']
    readonly_fields = ()
    filter_horizontal =()
    list_filter =()
    fieldsets =()
admin.site.register(dir_Colonia, ColoniaAdmin)"""

class FamiliaAdmin(admin.ModelAdmin):
    list_display = ['description']
    search_fields = ['description']
admin.site.register(Familia, FamiliaAdmin)

class MarcaAdmin(admin.ModelAdmin):
    list_display = ['description']
    search_fields = ['description']
admin.site.register(Marca, MarcaAdmin)

class UnidadMedidaAdmin(admin.ModelAdmin):
    list_display = ['description']
    search_fields = ['description']
admin.site.register(UnidadMedida, UnidadMedidaAdmin)

class TipoCambioAdmin(admin.ModelAdmin):
    list_display = ['tc_dof']
    search_fields = ['tc_dof']
admin.site.register(TipoCambio, TipoCambioAdmin)

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['description']
    search_fields = ['description']
admin.site.register(Proveedor, ProveedorAdmin)