# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dtsc_API', '0007_auto_20150612_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='application',
            field=models.ForeignKey(to='dtsc_API.Application'),
        ),
    ]
