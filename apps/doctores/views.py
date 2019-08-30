from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from apps.doctores.models import Diagnostico, Medico, HistoriaClinica
from django.urls import reverse_lazy

class CreateMedico(CreateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'doctores/doctores_form.html'
    success_url = reverse_lazy('doctor_listar')


class UpdateMedico(UpdateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'doctores/doctores_form.html'
    success_url = reverse_lazy('doctor_listar')


class DeleteMedico(DeleteView):
    model = Medico
    form_class = MedicoForm
    template_name = 'doctores/doctores_delete.html'
    success_url = reverse_lazy('doctor_listar')


class ListMedico(ListView):
    model = Medico
    template_name = 'doctores/doctores_list.html'


#---------------------------------------Diagnostico-----------------------------------------

class CreateDiagnostico(CreateView):
    model = Diagnostico
    form_class = DiagnosticoForm
    template_name = 'doctores/diagnostico_form.html'
    success_url = reverse_lazy('diagnostico_listar')


class UpdateDiagnostico(UpdateView):
    model = Diagnostico
    form_class = DiagnosticoForm
    template_name = 'doctores/diagnostico_form.html'
    success_url = reverse_lazy('diagnostico_listar')


class DeleteDiagnostico(DeleteView):
    model = Diagnostico
    form_class = DiagnosticoForm
    template_name = 'doctores/diagnostico_delete.html'
    success_url = reverse_lazy('diagnostico_listar')


class ListDiagnostico(ListView):
    model = Diagnostico
    template_name = 'doctores/diagnostico_list.html'


#---------------------------------------HistoriaClinica-----------------------------------------

class CreateHistoriaClinica(CreateView):
    model = HistoriaClinica
    form_class = HistoriaClinicaForm
    template_name = 'doctores/historiaclinica_form.html'
    success_url = reverse_lazy('historiaclinica_listar')


class UpdateHistoriaClinica(UpdateView):
    model = HistoriaClinica
    form_class = HistoriaClinicaForm
    template_name = 'doctores/historiaclinica_form.html'
    success_url = reverse_lazy('historiaclinica_listar')


class DeleteHistoriaClinica(DeleteView):
    model = HistoriaClinica
    form_class = HistoriaClinicaForm
    template_name = 'doctores/historiaclinica_delete.html'
    success_url = reverse_lazy('historiaclinica_listar')


class ListHistoriaClinica(ListView):
    model = HistoriaClinica
    template_name = 'doctores/historiaclinica_list.html'
