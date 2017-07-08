from django.conf.urls import url
from .views import *
from django.contrib.auth.decorators import login_required
urlpatterns = [
    url(r'^$',HomeView.as_view(), name='home'),
    url(r'^result_type/$',result, name='result'),

]
