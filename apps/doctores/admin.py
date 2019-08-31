from django.contrib import admin
from apps.doctores.models import Diagnostico, HistoriaClinica, Medico

admin.site.register(Diagnostico)
admin.site.register(HistoriaClinica)
admin.site.register(Medico)
