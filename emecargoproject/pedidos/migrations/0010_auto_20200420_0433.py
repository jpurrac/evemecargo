# Generated by Django 2.2.12 on 2020-04-20 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0009_productos_cantidad'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Productos',
            new_name='Producto',
        ),
    ]