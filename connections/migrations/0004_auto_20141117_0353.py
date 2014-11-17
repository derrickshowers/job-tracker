# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connections', '0003_auto_20141117_0315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='id',
            field=models.CharField(serialize=False, max_length=10, primary_key=True),
            preserve_default=True,
        ),
    ]
