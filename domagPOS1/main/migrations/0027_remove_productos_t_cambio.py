# Generated by Django 4.2.5 on 2024-08-01 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_alter_cliente_limite_credito'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productos',
            name='t_cambio',
        ),
    ]
