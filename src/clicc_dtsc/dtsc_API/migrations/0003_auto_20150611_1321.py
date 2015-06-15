# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dtsc_API', '0002_auto_20150611_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='data_type',
            field=models.CharField(max_length=5, choices=[('bool', 'Boolean'), ('int', 'Integer'), ('float', 'Real')]),
        ),
    ]
