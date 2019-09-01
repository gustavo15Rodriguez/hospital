from apps.doctores.views import CreateMedico, UpdateMedico, ListMedico, DeleteMedico, CreateDiagnostico, DeleteDiagnostico, UpdateDiagnostico, ListDiagnostico, ReporteDiagnosticoPdf, ReporteMedicoPdf
from apps.doctores.views import CreateHistoriaClinica, DeleteHistoriaClinica, UpdateHistoriaClinica, ListHistoriaClinica, ReporteHistoriaPdf
from django.conf.urls import url

urlpatterns = [
    url(r'^medico/listar$', ListMedico.as_view(), name='medico_listar'),
    url(r'^medico/crear$', CreateMedico.as_view(), name='medico_crear'),
    url(r'^medico/editar/(?P<pk>[\d]+)/$', UpdateMedico.as_view(), name='medico_editar'),
    url(r'^medico/eliminar/(?P<pk>[\d]+)/$', DeleteMedico.as_view(), name='medico_eliminar'),
    url(r'^medico/reporte_medico_pdf', ReporteMedicoPdf.as_view(), name='reporte_medico_pdf'),

    url(r'^diagnostico/listar$', ListDiagnostico.as_view(), name='diagnostico_listar'),
    url(r'^diagnostico/crear$', CreateDiagnostico.as_view(), name='diagnostico_crear'),
    url(r'^diagnostico/editar/(?P<pk>[\d]+)/$', UpdateDiagnostico.as_view(), name='diagnostico_editar'),
    url(r'^diagnostico/eliminar/(?P<pk>[\d]+)/$', DeleteDiagnostico.as_view(), name='diagnostico_eliminar'),
    url(r'^diagnostico/reporte_diagnostico_pdf', ReporteDiagnosticoPdf.as_view(), name='reporte_diagnostico_pdf'),

    url(r'^historia/listar$', ListHistoriaClinica.as_view(), name='historiaclinica_listar'),
    url(r'^historia/crear$', CreateHistoriaClinica.as_view(), name='historiaclinica_crear'),
    url(r'^historia/editar/(?P<pk>[\d]+)/$', UpdateHistoriaClinica.as_view(), name='historiaclinica_editar'),
    url(r'^historia/eliminar/(?P<pk>[\d]+)/$', DeleteHistoriaClinica.as_view(), name='historiaclinica_eliminar'),
    url(r'^historia/reporte_historiaclinica_pdf', ReporteHistoriaPdf.as_view(), name='reporte_historiaclinica_pdf'),
]