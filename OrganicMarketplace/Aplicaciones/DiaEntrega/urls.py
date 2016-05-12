from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.dias_entrega),
    url(r'^diasEntrega/$', views.definir_dias_entrega),
]
