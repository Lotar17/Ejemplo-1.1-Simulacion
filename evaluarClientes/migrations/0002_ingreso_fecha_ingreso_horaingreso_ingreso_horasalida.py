# Generated by Django 5.0.3 on 2024-03-21 02:55

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluarClientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingreso',
            name='fecha',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingreso',
            name='horaIngreso',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingreso',
            name='horaSalida',
            field=models.TimeField(null=True),
        ),
    ]