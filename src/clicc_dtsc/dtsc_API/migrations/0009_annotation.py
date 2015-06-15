# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dtsc_API', '0008_auto_20150612_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', models.UUIDField()),
                ('relation', models.TextField()),
                ('annotation', models.TextField(null=True, blank=True)),
            ],
        ),
    ]
