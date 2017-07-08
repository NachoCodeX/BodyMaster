from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import *
# Create your views here.

class HomeView(TemplateView):
    template_name='accounts/index.html'
    def get_context_data(self,*args,**kwargs):
        context=super(HomeView,self).get_context_data(*args,**kwargs)
        context['object_list']=Articulo.objects.all()
        return context

def result(request):
    data=dict()
    typeProduct=request.GET['type']
    nameProduct=request.GET['name']
    if int(typeProduct) > 0:
        articles=Articulo.objects.filter(tipo=typeProduct)
    else:
        articles=Articulo.objects.all()
    context={
        'object_list':articles,
        'name':nameProduct,
    }
    data['html_result']=render_to_string('partials/html_result.html',context)
    return JsonResponse(data)
