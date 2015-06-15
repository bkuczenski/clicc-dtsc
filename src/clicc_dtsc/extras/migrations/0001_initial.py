# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Combinedtox',
            fields=[
                ('chemical', models.CharField(max_length=10000, null=True, db_column='Chemical', blank=True)),
                ('cas', models.CharField(max_length=63, null=True, db_column='CAS', blank=True)),
                ('test', models.CharField(max_length=255, null=True, db_column='Test', blank=True)),
                ('species', models.CharField(max_length=63, null=True, db_column='Species', blank=True)),
                ('duration', models.CharField(max_length=63, null=True, db_column='Duration', blank=True)),
                ('endpoint', models.CharField(max_length=127, null=True, db_column='Endpoint', blank=True)),
                ('effectconc', models.CharField(max_length=63, null=True, db_column='EffectConc', blank=True)),
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='ID')),
            ],
            options={
                'db_table': 'CombinedTox',
                'managed': False,
                'in_db': 'cliccTriple',
            },
        ),
        migrations.CreateModel(
            name='Combineduses',
            fields=[
                ('chemical', models.CharField(max_length=10000, null=True, db_column='Chemical', blank=True)),
                ('cas', models.CharField(max_length=63, null=True, db_column='CAS', blank=True)),
                ('process', models.CharField(max_length=10000, null=True, db_column='Process', blank=True)),
                ('category', models.CharField(max_length=127, null=True, db_column='Category', blank=True)),
                ('subcategory', models.CharField(max_length=255, null=True, db_column='Subcategory', blank=True)),
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='ID')),
            ],
            options={
                'db_table': 'CombinedUses',
                'managed': False,
                'in_db': 'cliccTriple',
            },
        ),
    ]
