# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-02 21:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20161202_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='individual_ticket',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]