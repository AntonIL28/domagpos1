from django.db import models
from django.contrib.auth.models import User
from django.forms import model_to_dict #Tranformar en tipo Json un modelo

# Create your models here.
class dir_Estado(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=3)

    def __str__(self):
        return self.nombre
    
class dir_Ciudad(models.Model):
    nombre = models.CharField(max_length=100)
    id_dirEstado = models.ForeignKey(dir_Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
class dir_Colonia(models.Model):
    nombre = models.CharField(max_length=100)
    cod_postal = models.IntegerField(default='', blank=True)
    id_dirCiudad = models.ForeignKey(dir_Ciudad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    razon = models.CharField(max_length=200, null=False)
    rfc = models.CharField(max_length=13, null= False)
    credito = models.BooleanField(default=False)
    limite_credito = models.DecimalField(default=0, decimal_places=2, max_digits=8)
    dias_credito = models.IntegerField(default=0)
    lista_precios = models.IntegerField(default=1)
    nombre_comercial = models.CharField(max_length=200, null=True)
    dirEstado = models.CharField(max_length=200, null=True)
    dirCiudad = models.CharField(max_length=200, null=True)
    dirColonia = models.CharField(max_length=200, null=True)
    dircalle = models.CharField(max_length=200, null=True)
    dirnumext = models.CharField(max_length=10)
    dirnumint = models.CharField(max_length=10)
    telefono = models.CharField(max_length=15, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.razon

class Productos(models.Model):
    codigo = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=255, null=False)
    image = models.ImageField(upload_to='productos', null=True, blank=True) #original
    Unidad_Compras = models.CharField(max_length=200, null=False, default="")
    Unidad_Ventas = models.CharField(max_length=200, null=False, default="")
    Unidad_Inventario = models.CharField(max_length=200, null=False, default="")
    cantidad_Unidad_Compras = models.IntegerField(default=1)
    Cto_Unidad_Compras = models.DecimalField(max_digits=15, decimal_places=4, null=False)
    Cto_Factura = models.DecimalField(max_digits=15, decimal_places=4, null=False)
    Porc_GastosVarios = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    Porc_impuestos = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    Cto_Integrado = models.DecimalField(max_digits=15, decimal_places=4, null=False)
    moneda = models.CharField(max_length=50, null=False, default="")
    precio1 = models.DecimalField(max_digits=15, decimal_places=4, null=False, default="0.0000")
    precio2 = models.DecimalField(max_digits=15, decimal_places=4, null=False, default="0.0000")
    precio3 = models.DecimalField(max_digits=15, decimal_places=4, null=False, default="0.0000")
    precio4 = models.DecimalField(max_digits=15, decimal_places=4, null=False, default="0.0000")
    precio5 = models.DecimalField(max_digits=15, decimal_places=4, null=False, default="0.0000")
    porc_util_1 = models.DecimalField(max_digits=15, decimal_places=4, null=False, default="0.0000")
    porc_util_2 = models.DecimalField(max_digits=15, decimal_places=4, null=False, default="0.0000")
    porc_util_3 = models.DecimalField(max_digits=15, decimal_places=4, null=False, default="0.0000")
    porc_util_4 = models.DecimalField(max_digits=15, decimal_places=4, null=False, default="0.0000")
    porc_util_5 = models.DecimalField(max_digits=15, decimal_places=4, null=False, default="0.0000")
    codigo_bar_1 = models.CharField(max_length=200, default="")
    codigo_bar_2 = models.CharField(max_length=200, default="")
    codigo_bar_3 = models.CharField(max_length=200, default="")
    codigo_bar_4 = models.CharField(max_length=200, default="")
    codigo_bar_5 = models.CharField(max_length=200, default="")
    codigo_prov = models.CharField(max_length=200, null=False, default="")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        factor_gastosvarios = 1+(float(self.Porc_GastosVarios)/100)
        factor_impuestos = 1+(float(self.Porc_impuestos)/100)
        self.Cto_Factura = float(self.Cto_Unidad_Compras)/int(self.cantidad_Unidad_Compras)
        ctoInt = float(self.Cto_Factura) * float(factor_gastosvarios)
        ctoInt = ctoInt * factor_impuestos
        
        self.Cto_Integrado = ctoInt
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.description
