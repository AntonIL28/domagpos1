# Generated by Django 4.2.5 on 2024-07-27 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_alter_cliente_lista_precios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='limite_credito',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]