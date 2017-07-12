from django.shortcuts import render,redirect
from django.views.generic import TemplateView,DetailView,UpdateView,ListView
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import *
from .forms import *
from django.views.decorators.csrf import csrf_protect
from django.core.urlresolvers import reverse, reverse_lazy
from django.core.mail import EmailMessage
from django.template.defaulttags import register
from collections import defaultdict
from django.http import HttpResponseRedirect
@register.filter
def get_cart(dic,key,*args,**kwargs):
    print("DICT: "+str(dic))
    print(key)
    # print(request.session['count'])
    for i in dic:
        if str(key) in i:
            return i.get(str(key))




# Create your views here.

class HomeView(TemplateView):
    template_name='accounts/index.html'
    def get_context_data(self,*args,**kwargs):
        context=super(HomeView,self).get_context_data(*args,**kwargs)
        context['object_list']=Articulo.objects.all()
        if "count" not in self.request.session:
            print("ENTRE")
            self.request.session['count']=[]
            for i in context['object_list']:
                aux=self.request.session['count']
                a=dict([(str(i.pk),i.cantidad)])
                aux.append(a)
                self.request.session['count']=aux
        print("HOME COUNT: "+str(self.request.session['count']))
        self.request.session.modified = True
        self.request.session['search_product']=0
        return context

class ComprasView(ListView):
    template_name='accounts/compras.html'

    def get_queryset(self):
        return Compra.objects.all()

class CartView(TemplateView):
    template_name='accounts/cart.html'
    def get_context_data(self,*args,**kwargs):
        from collections import Counter
        context=super(CartView,self).get_context_data(*args,**kwargs)

        if 'product' in self.request.session:
            products=self.request.session['product']
            repeat=Counter(products)
            list_pk= [i for i in repeat if repeat[i]>1]
            list_pk= list_pk+[i for i in repeat if repeat[i]==1]
            context['object_list']=[]
            total=0
            for pk in list_pk:
                product=Articulo.objects.get(pk=pk)
                total=total+(product.precio*repeat[pk])
                context['object_list'].append({'nombre':product.nombre,'precio':product.precio,'cantidad':repeat[pk]})
            context['total']=total
        return context

def result(request):
    data=dict()
    typeProduct=request.GET['type']
    request.session['search_product']=typeProduct
    nameProduct=request.GET['name']
    if int(typeProduct) > 0:
        articles=Articulo.objects.filter(tipo=typeProduct)
    else:
        articles=Articulo.objects.all()
    context={
        'object_list':articles,
        'name':nameProduct,
    }
    data['html_result']=render_to_string('partials/html_result.html',context,request=request)
    return JsonResponse(data)

def sessionValues(request,idCompra):
    if 'product' in request.session:
        s=request.session['product']
        s.append(idCompra)
        request.session['product']=s
    else:
        request.session['product']=[idCompra]

def add_purchase(request):
    data=dict()
    idCompra=int(request.GET['idCompra'])
    temp=request.session['count']
    for i in temp:
        newId=str(idCompra)
        if newId in i:
            i[newId]=i.get(newId)-1
    print("REDUCE: "+str(temp))
    add=int(request.GET['add'])
    sessionValues(request,idCompra)
    context={'add':add}
    # print(context)
    data['cart']=render_to_string('partials/cart_count.html',context)

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
    def form_valid(self,form):
        super(ProductDetailView,self).form_valid(form)
        pk=form.instance.pk
        newCant=form.instance.cantidad
        temp=self.request.session['count']

        for i in temp:
            if str(pk) in i:
                i[str(pk)]=newCant
        self.request.session['count']=temp
        print("NEW CANTIDAD: "+str(self.request.session['count']))
        return HttpResponseRedirect(self.get_success_url())
def deleteSession(request):
    del request.session['product']
    del request.session['count']
    return JsonResponse({'done':'done'})

def finalizar(request):
    from collections import Counter
    data=dict()
    compra=Compra()
    compra.save()
    total=0
    repeat=dict(Counter(request.session['product']))
    for i in request.session['product']:
        p=Articulo.objects.get(pk=i)
        total=total+(p.precio)
        compra.productos.add(p)
    names=[]
    for pk,cant in repeat.items():
        p=Articulo.objects.get(pk=pk)
        names.append(str(cant)+"x"+str(p.nombre))
        p.cantidad=p.cantidad-cant
        p.save()
    # print(request.session['items'])
    compra.total=total
    compra.save()
    print(names)
    del request.session['product']
    email = EmailMessage('BodyMaster {}'.format(compra.fecha), 'Se ha relizado una compra de {1} con un total de ${0} \n '.format(total,"/".join(names)), to=['photoscastillo2017@gmail.com'])
    email.send()
    return JsonResponse(data)
