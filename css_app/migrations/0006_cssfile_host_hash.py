# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-06 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('css_app', '0005_auto_20161204_0354'),
    ]

    operations = [
        migrations.AddField(
            model_name='cssfile',
            name='host_hash',
            field=models.CharField(default='default', max_length=200),
            preserve_default=False,
        ),
    ]
