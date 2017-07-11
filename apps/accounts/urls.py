from django.conf.urls import url
from .views import *
from django.contrib.auth.decorators import login_required
urlpatterns = [
    url(r'^$',HomeView.as_view(), name='home'),
    url(r'^result_type/$',result, name='result'),
    url(r'^cart/$',CartView.as_view(), name='cart'),
    url(r'^comprar/$',add_purchase, name='comprar'),
    url(r'^compras$',ComprasView.as_view(), name='compras'),
    url(r'^add/product$',add_product, name='addProduct'),
    url(r'^detail/product/(?P<pk>\d+)$',ProductDetailView.as_view(), name='detail'),
    url(r'^deleteSession/$',deleteSession, name='deleteSession'),
    url(r'^finalizar/$',finalizar, name='finalizar'),
]
