# Generated by Django 4.2.2 on 2023-06-24 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_reserva_fecha_reserva'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='estado',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
