from django.conf.urls import url

from . import views

urlpatterns = [
   url(r'^request/$', views.request),
   url(r'^request_products/(?P<market_id>\d+)/$', views.request_products),
   url(r'^request_products_available/(?P<market_id>\d+)/$', views.request_products_available),
   url(r'^create/$', views.create),
   url(r'^add_product/$', views.add_product),
   url(r'^delete_product/$', views.delete_product)
]
