# Generated by Django 2.2.12 on 2020-04-16 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginapp', '0017_auto_20200416_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historia',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='historia/'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='texto',
            field=models.TextField(max_length=300, verbose_name='Texto'),
        ),
    ]