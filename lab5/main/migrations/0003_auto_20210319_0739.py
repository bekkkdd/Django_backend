# Generated by Django 3.1.7 on 2021-03-19 07:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210319_0516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_on',
            field=models.DateField(default=datetime.datetime(2021, 3, 21, 7, 39, 35, 979850), verbose_name='Due on'),
        ),
        migrations.AlterField(
            model_name='task',
            name='owner',
            field=models.CharField(default='Admin', max_length=255),
        ),
    ]