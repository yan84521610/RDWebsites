from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.about, name='about'),
    url(r'^$', views.news, name='news'),
    url(r'^$', views.products, name='products'),
    url(r'^$', views.hr, name='hr'),
    url(r'^$', views.contacts, name='contacts'),
]