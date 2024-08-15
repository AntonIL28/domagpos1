# Generated by Django 4.2.5 on 2024-08-01 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_remove_productos_t_cambio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_Cambio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TC_VENTA', models.DecimalField(decimal_places=4, default='0.0000', max_digits=8)),
                ('TC_COMPRA', models.DecimalField(decimal_places=4, default='0.0000', max_digits=8)),
                ('TC_DOF', models.DecimalField(decimal_places=4, default='0.0000', max_digits=8)),
                ('FECHA', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Tipo de Cambio',
            },
        ),
    ]
