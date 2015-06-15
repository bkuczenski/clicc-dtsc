"""
Utility function to handle importing data from other dbs
"""
from __future__ import unicode_literals

from extras.models import Combinedtox, Combineduses
from dtsc_API.models import  Chemical, Property, Module, Application, DATA_TYPES, DtscCandidateChemical
import re

def ImportToxEndpoints():
    """
    Create a list of toxicity endpoints from the CombinedTox table "name" and "endpoint"
    We can query these results as a module until the endpoints are computed natively.
    """
    ECHA_TOX_MODULE=Module.objects.get(name='ECHA CombinedTox')
    Real=[item[0] for item in DATA_TYPES if "Real" in item][0]

    endpts = list(Combinedtox.objects.values_list('test','endpoint').distinct())
    for pp in endpts:
        # check to see if endpoint is already defined in properties
        if Property.objects.filter(name=pp[0],endpoint=pp[1]).count()==0:
            print("Adding new property for test %s with endpoint %s ") % pp
            P = Property(name=pp[0], endpoint=pp[1], module=ECHA_TOX_MODULE, data_type=Real)
            P.save()
        else:
            print("test %s with endpoint %s exists") % pp

def ImportApplications():
    """
    Create a list of applications from the CombinedUses table "Category" and "Subcategory"
    Later we can query all processes that match a given cat or subcat, and we can assign 
    a category and subcategory to each product
    """
    apps = list(Combineduses.objects.values_list('category','subcategory').distinct())
    # first create un-subcategorized applications
    ac = set([ app[0] for app in apps])
    for a in ac:
        # check to see if endpoint is already defined in properties
        if Application.objects.filter(category=a,subcategory='').count()==0:
            print("Adding new application category:  %s ") % a
            A = Application(category=a, subcategory='')
            A.save()
        else:
            print("Application %s exists") % a

    for ap in apps:
        # check to see if endpoint is already defined in properties
        if Application.objects.filter(category=ap[0],subcategory=ap[1]).count()==0:
            print("Adding new application:  %s | %s ") % ap
            A = Application(category=ap[0], subcategory=ap[1])
            A.save()
        else:
            print("Application %s | %s exists") % ap

def ImportChemicals():
    """
    Imports the chemicals listed in the dtsc_candidate_chemicals table, but only if they have CAS numbers
    """
    cand = list(DtscCandidateChemical.objects.filter(casrn__isnull=False))
    for ch in cand:
        # check to see if endpoint is already defined in properties
        ch.candidate_name=re.sub(u'\u2018|\u2019',"'",ch.candidate_name)
        ch.candidate_name=re.sub(u'\u2013',"-",ch.candidate_name)
        ch.candidate_name=ch.candidate_name.replace(u'\xad','-')
        if Chemical.objects.filter(casrn=ch.casrn).count()==0:
            print("Adding new chemical:  %s (CASRN: %s)") % (ch.candidate_name, ch.casrn)
            C = Chemical(name=ch.candidate_name, casrn = ch.casrn)
            C.save()
        else:
            print("Chemical with CASRN %s exists") % ch.casrn
        
        

def main():
    ImportToxEndpoints()
    ImportApplications()
    ImportChemicals()
            
        