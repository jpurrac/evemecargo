# Generated by Django 2.2.12 on 2020-04-22 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0014_auto_20200421_2153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carrito',
            old_name='item',
            new_name='producto',
        ),
    ]
