from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login', views.iniciar_sesion),
    url(r'^logout', views.cerrar_sesion),
    url(r'^products/$', views.productos),
    url(r'^products/page=(?P<page>\d+)/$', views.productos_por_pagina),
    url(r'^cart/add', views.agregar_producto_carrito),
    url(r'^cart/checkout', views.confirmar_compra),
    url(r'^order', views.productos_comprados),
]
