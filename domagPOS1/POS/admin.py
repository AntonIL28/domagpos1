from django.contrib import admin
from main.models import Cliente, Productos
from POS.models import *
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('razon', 'telefono')
    search_fields = ['razon']
    readonly_fields = ('created', 'updated')
    filter_horizontal =()
    list_filter =()
    fieldsets =()

admin.site.register(Cliente, ClienteAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['description']
    search_fields = ['description']
    readonly_fields = ['created', 'updated']
    filter_horizontal =()
    list_filter =()
    fieldsets =()

admin.site.register(Productos, ProductoAdmin)

class ArticuloAdmin(admin.ModelAdmin):
    search_fields = ['description']
    readonly_fields = ['created', 'updated']

admin.site.register(Article, ArticuloAdmin) 


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    readonly_fields = ['created_at']

admin.site.register(Category, CategoryAdmin)

class VentaAdmin(admin.ModelAdmin):
    readonly_fields = ()

admin.site.register(Venta, VentaAdmin)

class AlmacenAdmin(admin.ModelAdmin):
    readonly_fields = ()

admin.site.register(Almacen, AlmacenAdmin)

class ExistenciaAdmin(admin.ModelAdmin):
    readonly_fields = ()

admin.site.register(Existencia, ExistenciaAdmin) 

