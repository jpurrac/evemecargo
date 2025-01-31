# Generated by Django 2.2.12 on 2020-04-22 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0011_auto_20200420_2126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orden',
            old_name='fechacontacto',
            new_name='fechapedido',
        ),
        migrations.AddField(
            model_name='orden',
            name='total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='orden',
            name='comentario',
            field=models.TextField(max_length=100, verbose_name='Comentario'),
        ),
    ]
