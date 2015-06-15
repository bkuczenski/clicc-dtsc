# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dtsc_API', '0003_auto_20150611_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='endpoint',
            field=models.TextField(null=True, blank=True),
        ),
    ]
