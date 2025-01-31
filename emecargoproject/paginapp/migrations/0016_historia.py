# Generated by Django 2.2.12 on 2020-04-16 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginapp', '0015_auto_20200410_1516'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=300, verbose_name='Primer Texto:')),
                ('imagen', models.FileField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Historia',
                'verbose_name_plural': 'Historias',
            },
        ),
    ]
