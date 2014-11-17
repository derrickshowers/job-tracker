# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connections', '0002_connection_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='id',
            field=models.CharField(max_length=10, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
