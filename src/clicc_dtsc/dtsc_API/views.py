from django.shortcuts import render
import models, results
from django.forms.models import model_to_dict
from django.http.response import JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from uuid import UUID
from django.core import serializers

# Create your views here.

def modules(request):
    ms = models.Module.objects.all()
    return JsonResponse([model_to_dict(m) for m in ms] , safe=False)# 
 
def validate_uuid4(uuid_string):
    """
    Validate that a UUID string is in
    fact a valid uuid4.

    Happily, the uuid module does the actual
    checking for us.

    It is vital that the 'version' kwarg be passed
    to the UUID() call, otherwise any 32-character
    hex string is considered valid.
    """
    try:
        val = UUID(uuid_string, version=4)
    except ValueError:
        # If it's a value error, then the string 
        # is not a valid hex code for a UUID.
        return False
 
    # If the uuid_string is a valid hex code, 
    # but an invalid uuid4,
    # the UUID.__init__ will convert it to a 
    # valid uuid4. This is bad for validation purposes.
 
    return val.hex == uuid_string
     
def validate_int(int_string):
    try:
        int(int_string)
        return True
    except ValueError:
        return False

def moduleresults(request):
    """
    User requests result?chemical=x&proprty=y
    call the module dispatcher to generate a result-- returns a ChemicalProperty object (or None)
    """
    chem_id = request.GET.get('chemical','')
    prop_id = request.GET.get('property','')
    
    ####import pdb; pdb.set_trace()
    
    if chem_id == '':
        return HttpResponse("Please supply a chemical ID.")
    
    if prop_id == '':
        return HttpResponse("Please supply a property ID.")
    
    # decode the supplied id
    if validate_uuid4(chem_id):
        C = models.Chemical.objects.get(uuid=chem_id)
    elif validate_int(chem_id):
        try:
            C = models.Chemical.objects.get(id=int(chem_id))
        except ObjectDoesNotExist:
            return HttpResponse("Requested chemical ID does not exist.")
    else:
        return HttpResponse("Couldn't interpret chemical param value.")
    
    # decode the supplied id
    if validate_uuid4(prop_id):
        P = models.Property.objects.get(uuid=prop_id)
    elif validate_int(prop_id):
        try:
            P = models.Property.objects.get(id=int(prop_id))
        except ObjectDoesNotExist:
            return HttpResponse("Requested property ID does not exist.")
    else:
        return HttpResponse("Couldn't interpret property param value.")
    
    R_qs = models.ChemicalProperty.objects.filter(chemical=C, property=P)

    if R_qs.count() == 0:
        R = results.module_dispatcher(P,C)

        if isinstance(R,models.RealResult):
            CP = models.ChemicalProperty(chemical=C, property=P, result=R)
            CP.save()
        else:
            return JsonResponse({
                'chemical': C.name,
                'property': P.name,
                'result': R})
    else:
        R = R_qs[0].result
        
    return JsonResponse({
            'chemical': C.name,
            'property': P.name,
            'resultuuid': str(R.uuid),
            'result':   model_to_dict(R, ('unit','data_type','mean_value','st_dev'))
        }, safe=False)
        
    
def resultbyuuid(request, resultuuid):
    try:
        U = UUID(resultuuid, version=4)
    except ValueError:
        return HttpResponse("Not a valid UUID.")
    
    R = models.RealResult.objects.get(uuid=U)
    A = models.Annotation.objects.get(uuid=U)

    CP = models.ChemicalProperty.objects.get(result_id=R.id)

    
    return JsonResponse({
            'chemical': CP.chemical.name,
            'property': CP.property.name,
            'resultuuid': str(R.uuid),
            'result': model_to_dict(R,('unit','data_type','mean_value','st_dev')),
            'annotation': A.relation + " | " + A.annotation
                         })    
    
def lciaresults(request):
    """
    User requests lciaresult?product=x&lciamethod=y
    call the module dispatcher to generate a result-- returns a ChemicalProperty object (or None)
    """
    prod_id = request.GET.get('product','')
    lcia_id = request.GET.get('lciamethod','')
    
    ####import pdb; pdb.set_trace()
    
    if prod_id == '':
        return HttpResponse("Please supply a product ID.")
    
    if lcia_id == '':
        return HttpResponse("Please supply an LCIA Method ID.")
    
    # decode the supplied id
    if validate_uuid4(prod_id):
        P = models.Product.objects.get(uuid=prod_id)
    elif validate_int(prod_id):
        try:
            P = models.Product.objects.get(id=int(prod_id))
        except ObjectDoesNotExist:
            return HttpResponse("Requested product ID does not exist.")
    else:
        return HttpResponse("Couldn't interpret product param value.")
    
    # decode the supplied id
    if validate_uuid4(lcia_id):
        L = models.Property.objects.get(uuid=lcia_id)
    elif validate_int(lcia_id):
        try:
            L = models.LciaMethod.objects.get(id=int(lcia_id))
        except ObjectDoesNotExist:
            return HttpResponse("Requested LCIA Method ID does not exist.")
    else:
        return HttpResponse("Couldn't interpret LCIA Method param value.")
    
    R = results.lcia_dispatcher(P,L)

    if isinstance(R,models.RealResult):
        return JsonResponse({
            'product': P.name,
            'LciaMethod': L.name,
            'resultuuid': str(R.uuid),
            'result':   model_to_dict(R, ('unit','data_type','mean_value','st_dev'))
        }, safe=False)
    else:
        return JsonResponse({
            'product': P.name,
            'LciaMethod': L.name,
            'result':   R})
        
        
    
    
