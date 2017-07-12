from django.conf.urls import url
from .views import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login,logout
from .forms import MyLoginForm
urlpatterns = [
    url(r'^$',login,{'template_name':'accounts/login.html','form_class':MyLoginForm,'redirect_authenticated_user':True},name='login'),
    url(r'^logout$',logout,{'next_page':'/'},name='logout'),

    url(r'^home$',login_required(HomeView.as_view()), name='home'),
    url(r'^product/delete/(?P<pk>\d+)$', login_required(product_delete), name='product_delete'),
    url(r'^compra/delete/(?P<pk>\d+)$', login_required(compra_delete.as_view()), name='compra_delete'),

    url(r'^result_type/$',login_required(result), name='result'),
    url(r'^cart/$',login_required(CartView.as_view()), name='cart'),
    url(r'^comprar/$',login_required(add_purchase), name='comprar'),
    url(r'^compras$',login_required(ComprasView.as_view()), name='compras'),
    url(r'^add/product$',login_required(add_product), name='addProduct'),
    url(r'^detail/product/(?P<pk>\d+)$',login_required(ProductDetailView.as_view()), name='detail'),
    url(r'^deleteSession/$',login_required(deleteSession), name='deleteSession'),
    url(r'^finalizar/$',login_required(finalizar), name='finalizar'),
]
