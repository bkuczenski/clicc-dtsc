from __future__ import unicode_literals

from django.db import models
import uuid 
####????from _curses import meta

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

"""
First we have the DTSC candidate chemical list that Sabina built.  It's not really used.
"""
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

"""
Now we begin to define the actual features.  First the base types, then the derived types.

Enums:
DataType - bool, int, float

base types:
  Chemical - a distinct chemical ID with (non-unique) CAS number and SMILES string
  Module - a computational unit.  Modules will need some kind of python wrapper and will return results.
  Property - something about a chemical. computed by a module.
    
"""
DATA_TYPES= (
    ('bool','Boolean'),
    ('int','Integer'),
    ('float','Real')
)

class Annotation(models.Model):
    uuid = models.UUIDField(blank=False, null=False, unique=False) # RDF subject
    relation = models.TextField(blank=False, null=False) # RDF predicate
    annotation = models.TextField(blank=True, null=True) # RDF object, or in this case documentary text

class Result(models.Model):
    uuid = models.UUIDField(blank=False, null=False, unique=True, default=uuid.uuid4)
    data_type = models.TextField(blank=False, null=False, choices=DATA_TYPES)
    unit = models.TextField(blank=True, null=False)

    class Meta:
        abstract = True

class RealResult(Result):
    mean_value = models.FloatField(blank=False, null=False)
    st_dev = models.FloatField(blank=True, null=True)
    confidence_interval_5 = models.FloatField(blank=True, null=True)
    confidence_interval_95 = models.FloatField(blank=True, null=True)
    
    class Meta:
        db_table = 'real_result'


class Module(models.Model):
    name = models.TextField(blank=False, null=False)
    
    def __unicode__(self):
        return self.name
    
class Property(models.Model):
    uuid = models.UUIDField(blank=False, null=False, unique=True, default=uuid.uuid4)
    name = models.TextField(blank=False, null=False)
    endpoint = models.TextField(blank=True, null=True)
    data_type = models.CharField(max_length=5,blank=False, null=False, choices=DATA_TYPES)
    module = models.ForeignKey(Module)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Properties'
    
class Chemical(models.Model):
    uuid = models.UUIDField(blank=False, null=False, unique=True, default=uuid.uuid4)
    name = models.TextField(blank=False, null=False)
    casrn = models.TextField(blank=True, null=False)
    smiles = models.TextField(blank=True, null=False)
    properties = models.ManyToManyField(Property, through='ChemicalProperty')
    
    def __unicode__(self):
        return self.name
    
class LciaMethod(models.Model):
    uuid = models.UUIDField(blank=False, null=False, unique=True, default=uuid.uuid4)
    name = models.TextField(blank=False, null=False)
    module = models.ForeignKey(Module)
    
    def __unicode__(self):
        return self.name

class Application(models.Model):
    uuid = models.UUIDField(blank=False, null=False, unique=True, default=uuid.uuid4)
    category = models.TextField(blank=False,null=False)
    subcategory = models.TextField(blank=True,null=False)
    
    def __unicode__(self):
        return self.category + " | " + self.subcategory

class Product(models.Model):
    uuid = models.UUIDField(blank=False, null=False, unique=True, default=uuid.uuid4)
    name = models.TextField(blank=False, null=False)
    owner = models.TextField(blank=True, null=False)
    constituents = models.ManyToManyField(Chemical, through='ProductChemical')
    geography = models.TextField(blank=True, null=False)
    production_volume = models.FloatField(blank=True, null=True)
    application = models.ForeignKey(Application)

    def __unicode__(self):
        return self.name
"""
Many-to-many tables
"""
    
class ProductChemical(models.Model):
    product = models.ForeignKey(Product)
    chemical = models.ForeignKey(Chemical)
    mass_fraction = models.FloatField(blank=False, null=False)
    custom_properties = models.ManyToManyField(Property, through='CustomProperty')
    
class ChemicalProperty(models.Model):
    chemical = models.ForeignKey(Chemical)
    property = models.ForeignKey(Property)
    """chemical properties can have a different data type, but it always gets stored as a RealResult"""
    result = models.ForeignKey(RealResult) 

class CustomProperty(models.Model):
    product_chemical = models.ForeignKey(ProductChemical)
    property = models.ForeignKey(Property)
    custom_value = models.ForeignKey(RealResult) # user can supply or omit the same uncertainty info
    
