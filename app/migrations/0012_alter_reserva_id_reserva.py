# Generated by Django 4.2.2 on 2023-06-23 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_reserva_asientos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='id_reserva',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]