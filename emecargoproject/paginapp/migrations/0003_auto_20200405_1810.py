# Generated by Django 2.2.12 on 2020-04-05 22:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginapp', '0002_auto_20200405_0342'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='fechacontacto',
            field=models.DateField(default=datetime.datetime.today, verbose_name='Fecha de Envio'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='asunto',
            field=models.CharField(choices=[('CM', 'Comentario'), ('FT', 'Felicitaciones'), ('RC', 'Reclamo'), ('RS', 'Resera'), ('PD', 'Pedido')], max_length=20),
        ),
    ]
