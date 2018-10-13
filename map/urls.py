from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^calculate', views.map_calculate, name='index'),
    url(r'^bad_request', views.map_bad_request, name='index')
]