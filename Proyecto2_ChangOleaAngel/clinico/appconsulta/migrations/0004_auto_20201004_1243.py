# Generated by Django 3.1.2 on 2020-10-04 17:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appconsulta', '0003_auto_20200920_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historia',
            name='fecha',
            field=models.DateField(blank=True, default=datetime.date(2020, 10, 4), null=True, verbose_name='Fecha de Historia'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='hora',
            field=models.TimeField(default=datetime.time(12, 43, 23, 579318), verbose_name='Hora'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='fecha',
            field=models.DateField(blank=True, default=datetime.date(2020, 10, 4), null=True, verbose_name='Fecha de Atencion'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='hora',
            field=models.TimeField(default=datetime.time(12, 43, 23, 577292), verbose_name='Hora'),
        ),
    ]