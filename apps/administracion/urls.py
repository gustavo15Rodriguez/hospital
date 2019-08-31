from django.conf.urls import url
from apps.administracion.views import CreatePlanta, UpdatePlanta, DeletePlanta, ListPlanta

urlpatterns = [
    url(r'^planta/nueva$', CreatePlanta.as_view(), name='planta_crear'),
    url(r'^planta/listar$', ListPlanta.as_view(), name='planta_listar'),
    url(r'^planta/editar/(?P<pk>[\d]+)/$', UpdatePlanta.as_view(), name='planta_editar'),
    url(r'^planta/eliminar/(?P<pk>[\d]+)/$', DeletePlanta.as_view(), name='planta_eliminar'),
]
