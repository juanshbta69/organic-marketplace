from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^compras/$', views.compras),
    url(r'^(?P<pk>\d+)/compra_productos/$', views.detalle_compra),
]
