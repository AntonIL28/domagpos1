from django.db import models
from django.contrib.auth.models import User

# Create your models here.
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
    
class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='Titulo')
    content = models.CharField(max_length=250, verbose_name='Contenido')
    image = models.ImageField(default='null', verbose_name='Imagen', upload_to="products")
    public = models.BooleanField(verbose_name='Publicar')
    user = models.ForeignKey(User, verbose_name='Usuario', on_delete=models.CASCADE, null=True)
    categories = models.ManyToManyField(Category, verbose_name='Categorias') 
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado el')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.title
