from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^policy$', views.policy),
    url(r'^term$', views.term)
    
]