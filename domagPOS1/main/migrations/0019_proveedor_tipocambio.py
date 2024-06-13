# Generated by Django 4.2.5 on 2024-06-12 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_familia_marca_unidadmedida'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_proveedor', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
            },
        ),
        migrations.CreateModel(
            name='TipoCambio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('tc_venta', models.DecimalField(decimal_places=2, default='0.00', max_digits=8)),
                ('tc_compra', models.DecimalField(decimal_places=2, default='0.00', max_digits=8)),
                ('tc_dof', models.DecimalField(decimal_places=2, default='0.00', max_digits=8)),
            ],
            options={
                'verbose_name': 'Tipo de cambio',
            },
        ),
    ]