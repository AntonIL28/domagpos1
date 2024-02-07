# Generated by Django 4.2.5 on 2024-02-07 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('POS', '0004_clientes_egreso_productosegreso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('description', models.CharField(max_length=255, verbose_name='Descripcion')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('image', models.ImageField(default='null', upload_to='categories', verbose_name='Imagen')),
            ],
            options={
                'verbose_name': 'Almace',
                'verbose_name_plural': 'Almacenes',
            },
        ),
        migrations.CreateModel(
            name='Existencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('id_Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='POS.article')),
                ('id_almacen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='POS.almacen')),
            ],
            options={
                'verbose_name': 'Inventario',
                'verbose_name_plural': 'Inventarios',
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=200, unique=True)),
                ('precio', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('iva', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('entregado', models.BooleanField(default=True)),
                ('devolucion', models.BooleanField(default=False)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='POS.article')),
                ('cantidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='POS.existencia')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
            },
        ),
        migrations.RemoveField(
            model_name='productosegreso',
            name='egreso',
        ),
        migrations.RemoveField(
            model_name='productosegreso',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='id_Producto',
        ),
        migrations.DeleteModel(
            name='Egreso',
        ),
        migrations.DeleteModel(
            name='ProductosEgreso',
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
    ]
