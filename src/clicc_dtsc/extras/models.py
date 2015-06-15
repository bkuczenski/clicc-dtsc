# Create your models here.

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals
from django.db import models


import django.db.models.options as options
options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('in_db',)

class Combinedtox(models.Model):
    chemical = models.CharField(db_column='Chemical', max_length=10000, blank=True, null=True)  # Field name made lowercase.
    cas = models.CharField(db_column='CAS', max_length=63, blank=True, null=True)  # Field name made lowercase.
    test = models.CharField(db_column='Test', max_length=255, blank=True, null=True)  # Field name made lowercase.
    species = models.CharField(db_column='Species', max_length=63, blank=True, null=True)  # Field name made lowercase.
    duration = models.CharField(db_column='Duration', max_length=63, blank=True, null=True)  # Field name made lowercase.
    endpoint = models.CharField(db_column='Endpoint', max_length=127, blank=True, null=True)  # Field name made lowercase.
    effectconc = models.CharField(db_column='EffectConc', max_length=63, blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CombinedTox'
        in_db = 'cliccTriple'


class Combineduses(models.Model):
    chemical = models.CharField(db_column='Chemical', max_length=10000, blank=True, null=True)  # Field name made lowercase.
    cas = models.CharField(db_column='CAS', max_length=63, blank=True, null=True)  # Field name made lowercase.
    process = models.CharField(db_column='Process', max_length=10000, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=127, blank=True, null=True)  # Field name made lowercase.
    subcategory = models.CharField(db_column='Subcategory', max_length=255, blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CombinedUses'
        in_db = 'cliccTriple'
