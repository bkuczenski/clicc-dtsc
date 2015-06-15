# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('dtsc_API', '0004_property_endpoint'),
    ]

    operations = [
#        migrations.CreateModel(
#            name='Application',
#            fields=[
#                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
#                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
#                ('category', models.TextField()),
#                ('subcategory', models.TextField(blank=True)),
#            ],
#        ),
#        migrations.AddField(
#            model_name='chemical',
#            name='uuid',
#            field=models.UUIDField(default=uuid.uuid4, unique=True),
#        ),
#        migrations.AddField(
#            model_name='lciamethod',
#            name='uuid',
#            field=models.UUIDField(default=uuid.uuid4, unique=True),
#        ),
#        migrations.AddField(
#            model_name='product',
#            name='uuid',
#            field=models.UUIDField(default=uuid.uuid4, unique=True),
#        ),
        migrations.AddField(
            model_name='property',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
        migrations.AddField(
            model_name='realresult',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
