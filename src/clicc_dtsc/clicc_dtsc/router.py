'''
Created on Jun 10, 2015

@author: Brandon
'''
class CliccRouter(object):
    """
    A router to control access to all databases in the clicc_dtsc project
    """
    def db_for_read(self, model, **hints):
        ""
        if model._meta.app_label == 'dtsc_API':
            return 'default'
        elif hasattr(model._meta,'in_db'):
            return model._meta.in_db
        else:
            return None
        
    def db_for_write(self, model, **hints):
        
        if model._meta.app_label == 'dtsc_API':
            return 'default'
        else:
            return None
        
    def allow_relation(self, obj1, obj2, **hints):
        return None
    
    def allow_migrate(self, db, app_label, model=None, **hints):
        if db == 'default':
            return True
        else:
            return False
        

                
            
        