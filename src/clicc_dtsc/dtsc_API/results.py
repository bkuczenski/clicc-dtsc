"""
This section handles all the result generation

Every result-generating function should return a uresult
"""
import random
from extras.models import Combinedtox 
from models import RealResult, Annotation
import re

class uResult:
    def __init__(self,unitname,value=0,stdev=0):
        self.unit=unitname
        self.value=value
        self.stdev=stdev
        
    def set(self, value, stdev=0):
        self.value=value
        self.stdev=stdev
        
    def conf5(self):
        return self.value-2*self.stdev
    
    def conf95(self):
        return self.value+2*self.stdev

def random_result(data_type):
    
    u = uResult('kg-eq',random.random()*100,random.random()*20)
    return (u, "Randomly generated result")

def echa_tox_lookup(prop,chemical):
    try:
        L = Combinedtox.objects.get(test=prop.name, endpoint=prop.endpoint, cas=chemical.casrn)
        score = re.match('^[0-9\.]+',L.effectconc)
        unit = L.effectconc[score.end()+1:]

        return (uResult(unit,float(score.group(0))),"ECHA Tox lookup")
    except:
        return (None, "ECHA Tox Lookup: No result found")

def module_dispatcher(prop, chemical, product=None):
    """
    first argument is the property to be computed-- should be an instance of models.Property
    second argument is the chemical the property is computed about-- instance of models.Chemica
    third argument is the product system in scope-- instance of models.Product. not implemented.
    
    This function is only called when a new result is required.  Invoke the appropriate module
    and return the result!  make a random one for now.
    """
    
    M = prop.module
    # these should all return a uresult and an annotation
    uR, annot = {
            'ECHA CombinedTox': echa_tox_lookup(prop, chemical)
            }.get(M.name,random_result(prop.data_type))
    
    if uR is None:
        return annot
    
    # save the result  
    R = RealResult(data_type = prop.data_type,
                   unit = uR.unit,
                   mean_value = uR.value,
                   st_dev = uR.stdev,
                   confidence_interval_5 = uR.conf5(),
                   confidence_interval_95 = uR.conf95())

    R.save()
    A=Annotation(uuid=R.uuid,relation='result',annotation=annot)
    A.save()

    return R

def lcia_dispatcher(product, method):
    """
    same again
    """
    uR, annot = random_result("float")
    
    # save the result  
    R = RealResult(data_type = "float",
                   unit = uR.unit,
                   mean_value = uR.value,
                   st_dev = uR.stdev,
                   confidence_interval_5 = uR.conf5(),
                   confidence_interval_95 = uR.conf95())

    R.save()
    A=Annotation(uuid=R.uuid,relation=method.name,annotation=product.name + " | " + annot)
    A.save()

    return R