# Generated by Django 2.2.9 on 2020-04-05 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paginapp', '0009_auto_20200405_1928'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacto',
            old_name='asunto',
            new_name='asunto_id',
        ),
    ]