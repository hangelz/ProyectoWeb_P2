# Generated by Django 3.1.2 on 2020-10-05 01:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appbase', '0004_auto_20201004_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='hora',
            field=models.TimeField(default=datetime.time(20, 45, 48, 985046), verbose_name='Hora'),
        ),
    ]