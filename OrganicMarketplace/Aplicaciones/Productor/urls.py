from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.productores),
    url(r'^loginAdmin/$', views.loginAdmin),
    url(r'^loginProvider/$', views.loginProvider),
    url(r'^(?P<nombre>\w+)$', views.buscar_productores),
    url(r'^productor_producto/(?P<productor_id>\d+)/(?P<nombre>\w+)$', views.buscar_productos_productores),
    url(r'^productor_producto/(?P<productor_id>\d+)$', views.lista_productos_productores),
    url(r'^productor_producto_faltantes/(?P<productor_id>\d+)/(?P<nombre>\w+)$', views.buscar_productos_productores_faltantes),
    url(r'^productor_producto_faltantes/(?P<productor_id>\d+)$', views.lista_productos_productores_faltantes),
    url(r'^gestion_productor_producto/$', views.gestionar_producto_productor),
    url(r'^registro/$', views.registerProducer),

]
