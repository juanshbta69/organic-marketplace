"""OrganicMarketplace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from OrganicMarketplace.Aplicaciones.Productor import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^proveedor/$', views.proveedor, name='proveedor'),
    url(r'^dashboard/$', views.dashboardAdmin, name='dashboardAdmin'),
    url(r'^admin/$', views.administracion, name='admin'),
    url(r'^dashboardProvider/$', views.dashboardProvider, name='dashboardProvider'),
    url(r'^createOffer/$', views.createOffer, name='createOffer'),
    url(r'^login/', include(admin.site.urls)),
    url(r'^productor/', include('OrganicMarketplace.Aplicaciones.Productor.urls')),
    url(r'^producto/', include('OrganicMarketplace.Aplicaciones.Producto.urls')),
    url(r'^unidadmedida/', include('OrganicMarketplace.Aplicaciones.UnidadMedida.urls')),
    url(r'^oferta/', include('OrganicMarketplace.Aplicaciones.Oferta.urls')),
    url(r'^categoria/', include('OrganicMarketplace.Aplicaciones.Categoria.urls')),
    url(r'^compra/', include('OrganicMarketplace.Aplicaciones.Compra.urls')),
    url(r'^consumidor/', include('OrganicMarketplace.Aplicaciones.Consumidor.urls')),
    url(r'^diaentrega/', include('OrganicMarketplace.Aplicaciones.DiaEntrega.urls')),
    url(r'^mercadotipo/', include('OrganicMarketplace.Aplicaciones.MercadoTipo.urls')),
    url(r'^movil/', include('OrganicMarketplace.Aplicaciones.Movil.urls'))
]
urlpatterns += staticfiles_urlpatterns()
