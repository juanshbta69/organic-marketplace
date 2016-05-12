from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.productos, name='index'),
    url(r'^(?P<nombre>\w+)$', views.buscar_productos),
     url(r'^crear/$', views.createProduct),
         url(r'^productos/$', views.getProducts),
         url(r'^cargar/(\d+)$', views.getSingleProduct),


]
