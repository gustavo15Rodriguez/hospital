from django.conf.urls import url
from apps.pacientes.views import CreatePaciente, UpdatePaciente, DeletePaciente, ListPaciente
from apps.pacientes.views import CreateTarjetaVisita, UpdateTarjetaVisita, DeleteTarjetaVisita, ListTarjetaVisita

urlpatterns = [
    url(r'^paciente/crear$', CreatePaciente.as_view(), name='paciente_crear'),
    url(r'^paciente/listar$', ListPaciente.as_view(), name='paciente_listar'),
    url(r'^paciente/editar/(?P<pk>[\d]+)/$', UpdatePaciente.as_view(), name='paciente_editar'),
    url(r'^paciente/eliminar/(?P<pk>[\d]+)/$', DeletePaciente.as_view(), name='paciente_eliminar'),
    url(r'^tarjetavisita/crear$', CreateTarjetaVisita.as_view(), name='tarjetavisita_crear'),
    url(r'^tarjetavisita/listar$', ListTarjetaVisita.as_view(), name='tarjetavisita_listar'),
    url(r'^tarjetavisita/editar/(?P<pk>[\d]+)/$', UpdateTarjetaVisita.as_view(), name='tarjetavisita_editar'),
    url(r'^tarjetavisita/eliminar/(?P<pk>[\d]+)/$', DeleteTarjetaVisita.as_view(), name='tarjetavisita_eliminar'),
]