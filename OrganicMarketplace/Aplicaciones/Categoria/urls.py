from django.conf.urls import url

from . import views

urlpatterns = [
   url(r'^$', views.gestionCategoria),
   url(r'^(?P<categoria_id>\d+)/$', views.getCategoria),
]
