# Generated by Django 3.1.2 on 2020-10-06 03:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appconsulta', '0009_auto_20201005_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historia',
            name='hora',
            field=models.TimeField(default=datetime.time(22, 15, 44, 139020), verbose_name='Hora'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='hora',
            field=models.TimeField(default=datetime.time(22, 15, 44, 130816), verbose_name='Hora'),
        ),
    ]