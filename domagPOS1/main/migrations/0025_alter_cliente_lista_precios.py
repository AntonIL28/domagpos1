# Generated by Django 4.2.5 on 2024-07-27 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_productos_codigo_barras'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='lista_precios',
            field=models.IntegerField(default=''),
        ),
    ]
