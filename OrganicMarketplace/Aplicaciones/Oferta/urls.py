from django.conf.urls import url

from . import views
urlpatterns = [
   # url(r'^$', views.index, name='index'),
    url(r'^producers/$', views.producers),
    url(r'^productos/$', views.products),
    url(r'^ofertas/$', views.offers),
    url(r'^create_offer/$', views.create_offer),
    url(r'^update_offer/$', views.update_offer),
    url(r'^request_offers/(?P<user_id>\d+)/$', views.request_offers),
    url(r'^request_offer/(?P<pk>\d+)/$', views.request_offer),
    url(r'^request_products/(?P<user_id>\d+)/$', views.request_products),
    url(r'^product_unit/(?P<product_id>\d+)/$', views.product_unit),
    url(r'^create_offer/$', views.create_offer),
    url(r'^delete_offer/$', views.delete_offer),
]
