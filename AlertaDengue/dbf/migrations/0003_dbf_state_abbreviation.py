# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 20:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('dbf', '0002_dbfchunkedupload')]

    operations = [
        migrations.AddField(
            model_name='dbf',
            name='state_abbreviation',
            field=models.CharField(max_length=2, null=True),
        )
    ]
