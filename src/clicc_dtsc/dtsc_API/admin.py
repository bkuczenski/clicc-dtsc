from django.contrib import admin

# Register your models here.

from .models import *

class PropertyAdmin(admin.ModelAdmin):
    # plural is properties
    pass

class ConstituentInline(admin.StackedInline):
    model = ProductChemical
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ConstituentInline]    

admin.site.register(Module)
admin.site.register(LciaMethod)
admin.site.register(Chemical)
admin.site.register(Property,PropertyAdmin)
admin.site.register(Product,ProductAdmin)
