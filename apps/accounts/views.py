from django.shortcuts import render,redirect
from django.views.generic import TemplateView,DetailView,UpdateView
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import *
from .forms import *
from django.views.decorators.csrf import csrf_protect
from django.core.urlresolvers import reverse, reverse_lazy
from django.core.mail import EmailMessage


# Create your views here.

class HomeView(TemplateView):
    template_name='accounts/index.html'
    def get_context_data(self,*args,**kwargs):
        context=super(HomeView,self).get_context_data(*args,**kwargs)
        context['object_list']=Articulo.objects.all()
        self.request.session['search_product']=0
        return context

class ComprasView(TemplateView):
    template_name='accounts/compras.html'

def result(request):
    data=dict()
    typeProduct=request.GET['type']
    request.session['search_product']=typeProduct
    nameProduct=request.GET['name']
    print(request.session['search_product'])
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


def add_purchase(request):
    data=dict()
    add=int(request.GET['add'])
    context={'add':add}
    print(context)
    data['cart']=render_to_string('partials/cart_count.html',context)
    # email = EmailMessage('COMPRA', 'SE HIZO UNA COMPRA', to=['photoscastillo2017@gmail.com'])
    # email.send()
    return JsonResponse(data)

# @csrf_protect
def save_form(request,form,template_name):
    data=dict()
    if request.method =='POST':
        if form.is_valid():
            form.save()
            # print(form)
            data['form_is_valid']=True
            products=Articulo.objects.filter(tipo=request.session['search_product'])
            data['product']=request.session['search_product']
            data['html_list']=render_to_string('partials/html_result.html',{'object_list':products})
        else:
            data['form_is_valid']=False
    context={'form':form}
    data['html']=render_to_string(template_name,context,request=request)
    return JsonResponse(data)

@csrf_protect
def add_product(request):
    if request.method=='POST':
        form=ProductForm(data=request.POST,files=request.FILES)
        print(request.FILES)
    else:
        form=ProductForm()
    return save_form(request,form,'partials/create_article.html')


class ProductDetailView(UpdateView):
    model = Articulo
    success_url = reverse_lazy('accounts:home')
    template_name = 'accounts/detail_product.html'
    form_class=ProductUpdateForm

    # def get_success_url(self):
    #     pass
        # return reverse_lazy('accounts:home')
