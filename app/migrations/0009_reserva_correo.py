# Generated by Django 4.2.2 on 2023-06-23 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_conductor_asientosdisponibles_reserva_destino_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='correo',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
    ]
