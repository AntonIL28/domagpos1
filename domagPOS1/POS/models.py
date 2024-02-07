from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.CharField(max_length=255, verbose_name='Descripcion')
    created_at = models. DateTimeField(auto_now_add=True, verbose_name='Creado el')
    image = models.ImageField(default='null', verbose_name='Imagen', upload_to="categories")
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name
    
class Almacen(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.CharField(max_length=255, verbose_name='Descripcion')
    created_at = models. DateTimeField(auto_now_add=True, verbose_name='Creado el')
    image = models.ImageField(default='null', verbose_name='Imagen', upload_to="categories")
    class Meta:
        verbose_name = 'Almace'
        verbose_name_plural = 'Almacenes'

    def __str__(self):
        return self.name

class Article(models.Model):
    codigo = models.CharField(max_length=200, unique=True, null=False)
    description = models.CharField(max_length=255, null=False)
    image = models.ImageField(upload_to='productos', null=True, blank=True)
    costo = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    precio_unitario = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    importe = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    lista_precios = models.IntegerField(default=0)
    porcentaje_iva = models.DecimalField(default=0, decimal_places=2, max_digits=8)
    iva = models.DecimalField(max_digits=15, decimal_places=2)
    id_Categoria = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'

    def __str__(self):
        return self.description
    
class Existencia(models.Model):
    id_Producto = models.ForeignKey(Article, on_delete=models.CASCADE)
    id_almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    class Meta:
        verbose_name = 'Existencia'
        verbose_name_plural = 'Existencias'

class Clientes(models.Model):
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


class Venta(models.Model):
    codigo = models.CharField(max_length=200, unique=True, null=False)
    articulo = models.ForeignKey(Article, on_delete=models.CASCADE)
    cantidad = models.ForeignKey(Existencia, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    subtotal = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    iva = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    total = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    created = models.DateTimeField(auto_now_add=True)
    entregado = models.BooleanField(default=True)
    devolucion = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'

    def __str__(self):
        return self.codigo