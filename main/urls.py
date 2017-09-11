from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'about', views.about, name='about'),
    url(r'news', views.news, name='news'),
    url(r'products', views.products, name='products'),
    url(r'hr', views.hr, name='hr'),
    url(r'contacts', views.contacts, name='contacts'),
]