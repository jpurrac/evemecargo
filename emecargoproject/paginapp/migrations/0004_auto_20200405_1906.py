# Generated by Django 2.2.9 on 2020-04-05 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paginapp', '0003_auto_20200405_1810'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asuntos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asuntos', models.CharField(choices=[('CM', 'Comentario'), ('FT', 'Felicitaciones'), ('RC', 'Reclamo'), ('RS', 'Reserva'), ('PD', 'Pedido')], max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='contacto',
            name='asunto',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='paginapp.Asuntos'),
        ),
    ]
