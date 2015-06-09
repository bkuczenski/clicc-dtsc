from __future__ import unicode_literals

from django.db import models

# Create your models here.

# first off, we have the already-existing table
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.

class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DtscCandidateChemical(models.Model):
    group_name = models.TextField(blank=True, null=True)
    casrn = models.TextField(blank=True, null=True)
    candidate_name = models.TextField(blank=True, null=True)
    hazard_traits = models.TextField(blank=True, null=True)
    authoritative_list_name = models.TextField(blank=True, null=True)
    initial_list = models.TextField(blank=True, null=True)

    class Meta:
        managed = False # don't manage this table
        db_table = 'dtsc_candidate_chemical'
