# Generated by Django 2.2.12 on 2020-04-20 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0006_remove_productos_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='categoriaproducto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pedidos.Categoria'),
            preserve_default=False,
        ),
    ]
