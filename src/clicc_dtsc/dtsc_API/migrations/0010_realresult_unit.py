# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dtsc_API', '0009_annotation'),
    ]

    operations = [
        migrations.AddField(
            model_name='realresult',
            name='unit',
            field=models.TextField(blank=True),
        ),
    ]
