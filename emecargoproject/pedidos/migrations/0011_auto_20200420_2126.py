# Generated by Django 2.2.12 on 2020-04-21 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0010_auto_20200420_0433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='categoriaproducto',
        ),
        migrations.AlterField(
            model_name='productosorden',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Producto'),
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]
