import tastypie
from tastypie.authorization import Authorization
#from tastypie.utils import trailing_slash
from tastypie.resources import ModelResource
#from django.conf.urls import url, patterns, include
import models
from .pretty_json import PrettyJSONSerializer



class PropertyResource(ModelResource):
    #def get_detail(self, request, parent_id):
    #    return { 'parent_id': parent_id}

    class Meta:
        queryset = models.Property.objects.all()
        resource_name = 'property'
        serializer = PrettyJSONSerializer()


class ChemicalResource(ModelResource):
    #children = tastypie.fields.ToManyField(models.Property,'property')
    
    #def prepend_urls(self):
    #    return [
    #        url(r'^(P<resource_name>%s)/(?P<uuid>\w[\w/-]*)/property%s' % (self._meta.resource_name,trailing_slash()),
    #            self.wrap_view('get_properties'), name='api_chemical_properties'),
    #    ]
    #    
    #def get_property(self, request, **kwargs):
    #    bundle = self.build_bundle(data={'uuid': kwargs['uuid']}, request=request)
    #    obj = self.cached_obj_get(bundle=bundle, **self.remove_api_resource_names(kwargs))
    #    child_resource = PropertyResource()
    #    return child_resource.get_detail(request, parent_id=obj.pk)
    
    class Meta:
        queryset = models.Chemical.objects.all()
        resource_name = 'chemical'
        serializer = PrettyJSONSerializer()

    """
    haystack didn't work
    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/search%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('get_search'), name="api_get_search"),
        ]

    def get_search(self, request, **kwargs):
        self.method_check(request, allowed=['get'])
        self.is_authenticated(request)
        self.throttle_check(request)

        # Do the query.
        sqs = SearchQuerySet().models(models.Chemical).load_all().auto_query(request.GET.get('q', ''))
        paginator = Paginator(sqs, 20)

        try:
            page = paginator.page(int(request.GET.get('page', 1)))
        except InvalidPage:
            raise Http404("Sorry, no results on that page.")

        objects = []

        for result in page.object_list:
            bundle = self.build_bundle(obj=result.object, request=request)
            bundle = self.full_dehydrate(bundle)
            objects.append(bundle)

        object_list = {
            'objects': objects,
        }

        self.log_throttled_access(request)
        return self.create_response(request, object_list)
    """

class ApplicationResource(ModelResource):
    class Meta:
        queryset = models.Application.objects.all()
        resource_name = 'application'
        serializer = PrettyJSONSerializer()
        
class AnnotationResource(ModelResource):
    class Meta:
        queryset = models.Annotation.objects.all()
        resource_name = 'annotation'
        serializer = PrettyJSONSerializer()
        

class ProductResource(ModelResource):
    application = tastypie.fields.ForeignKey(ApplicationResource,'application')

    class Meta:
        queryset = models.Product.objects.all()
        resource_name = 'product'
        serializer = PrettyJSONSerializer()
        authorization= Authorization()
        
class ProductConstituent(ModelResource):
    product = tastypie.fields.ForeignKey(ProductResource,'product')
    chemical = tastypie.fields.ForeignKey(ChemicalResource,'chemical')
    
    class Meta:
        queryset = models.ProductChemical.objects.all()
        resource_name = 'constituent'
        serializer = PrettyJSONSerializer()
        authorization= Authorization()
