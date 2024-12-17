# Generated by Django 4.2.5 on 2024-11-09 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_productos_t_cambio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dir_ciudad',
            options={'verbose_name': 'Ciudad', 'verbose_name_plural': 'Ciudades'},
        ),
        migrations.AlterModelOptions(
            name='dir_colonia',
            options={'verbose_name': 'Colonia', 'verbose_name_plural': 'Colonias'},
        ),
        migrations.AlterModelOptions(
            name='dir_estado',
            options={'verbose_name': 'Estado', 'verbose_name_plural': 'Estados'},
        ),
        migrations.AlterField(
            model_name='dir_ciudad',
            name='id_dirEstado',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='dir_colonia',
            name='id_dirCiudad',
            field=models.CharField(max_length=100),
        ),
    ]