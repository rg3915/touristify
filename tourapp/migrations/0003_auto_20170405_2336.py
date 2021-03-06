# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-05 23:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourapp', '0002_auto_20170405_2127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tourpoint',
            old_name='type',
            new_name='point_type',
        ),
        migrations.AlterField(
            model_name='tourpoint',
            name='latitude',
            field=models.DecimalField(decimal_places=3, max_digits=8),
        ),
        migrations.AlterField(
            model_name='tourpoint',
            name='longitude',
            field=models.DecimalField(decimal_places=3, max_digits=8),
        ),
    ]
