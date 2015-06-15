# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DtscCandidateChemical',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_name', models.TextField(null=True, blank=True)),
                ('casrn', models.TextField(null=True, blank=True)),
                ('candidate_name', models.TextField(null=True, blank=True)),
                ('hazard_traits', models.TextField(null=True, blank=True)),
                ('authoritative_list_name', models.TextField(null=True, blank=True)),
                ('initial_list', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'dtsc_candidate_chemical',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Chemical',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('casrn', models.TextField(blank=True)),
                ('smiles', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChemicalProperty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chemical', models.ForeignKey(to='dtsc_API.Chemical')),
            ],
        ),
        migrations.CreateModel(
            name='CustomProperty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='LciaMethod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('owner', models.TextField(blank=True)),
                ('geography', models.TextField(blank=True)),
                ('production_volume', models.FloatField(null=True, blank=True)),
                ('application', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductChemical',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mass_fraction', models.FloatField()),
                ('chemical', models.ForeignKey(to='dtsc_API.Chemical')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('data_type', models.TextField(choices=[('bool', 'Boolean'), ('int', 'Integer'), ('float', 'Real')])),
                ('module', models.ForeignKey(to='dtsc_API.Module')),
            ],
        ),
        migrations.CreateModel(
            name='RealResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_type', models.TextField(choices=[('bool', 'Boolean'), ('int', 'Integer'), ('float', 'Real')])),
                ('mean_value', models.FloatField()),
                ('st_dev', models.FloatField(null=True, blank=True)),
                ('confidence_interval_5', models.FloatField(null=True, blank=True)),
                ('confidence_interval_95', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'real_result',
            },
        ),
        migrations.AddField(
            model_name='productchemical',
            name='custom_properties',
            field=models.ManyToManyField(to='dtsc_API.Property', through='dtsc_API.CustomProperty'),
        ),
        migrations.AddField(
            model_name='productchemical',
            name='product',
            field=models.ForeignKey(to='dtsc_API.Product'),
        ),
        migrations.AddField(
            model_name='product',
            name='constituents',
            field=models.ManyToManyField(to='dtsc_API.Chemical', through='dtsc_API.ProductChemical'),
        ),
        migrations.AddField(
            model_name='lciamethod',
            name='module',
            field=models.ForeignKey(to='dtsc_API.Module'),
        ),
        migrations.AddField(
            model_name='customproperty',
            name='custom_value',
            field=models.ForeignKey(to='dtsc_API.RealResult'),
        ),
        migrations.AddField(
            model_name='customproperty',
            name='product_chemical',
            field=models.ForeignKey(to='dtsc_API.ProductChemical'),
        ),
        migrations.AddField(
            model_name='customproperty',
            name='property',
            field=models.ForeignKey(to='dtsc_API.Property'),
        ),
        migrations.AddField(
            model_name='chemicalproperty',
            name='property',
            field=models.ForeignKey(to='dtsc_API.Property'),
        ),
        migrations.AddField(
            model_name='chemicalproperty',
            name='result',
            field=models.ForeignKey(to='dtsc_API.RealResult'),
        ),
        migrations.AddField(
            model_name='chemical',
            name='properties',
            field=models.ManyToManyField(to='dtsc_API.Property', through='dtsc_API.ChemicalProperty'),
        ),
    ]
