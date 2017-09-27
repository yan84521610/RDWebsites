from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^news', views.news, name='news'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<news>[-\w]+)/$',
        views.news_detail,
        name='news_detail'),
    url(r'^products', views.products, name='products'),
    url(r'^hr', views.hr, name='hr'),
    url(r'^cooperation', views.cooperation, name='cooperation'),
    url(r'^contacts', views.contacts, name='contacts'),
]