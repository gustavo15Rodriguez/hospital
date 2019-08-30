from django.shortcuts import render
from apps.pacientes.models import Paciente, TarjetaVisita
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

class CreatePaciente(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente/paciente_form.html'
    success_url = reverse_lazy('paciente_listar')


class UpdatePaciente(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente/paciente_form.html'
    success_url = reverse_lazy('paciente_listar')


class DeletePaciente(DeleteView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente/paciente_delete.html'
    success_url = reverse_lazy('paciente_listar')


class ListPaciente(ListView):
    model = Paciente
    template_name = 'paciente/paciente_list.html'


#------------------------------------Tarjeta Visita------------------------------

class CreateTarjetaVisita(CreateView):
    model = TarjetaVisita
    form_class = TarjetaVisitaForm
    template_name = 'paciente/tarjetavisita_form.html'
    success_url = reverse_lazy('tarjetavisita_listar')


class UpdateTarjetaVisita(UpdateView):
    model = TarjetaVisita
    form_class = TarjetaVisitaForm
    template_name = 'paciente/tarjetavisita_form.html'
    success_url = reverse_lazy('tarjetavisita_listar')


class DeleteTarjetaVisita(DeleteView):
    model = TarjetaVisita
    form_class = TarjetaVisitaForm
    template_name = 'paciente/tarjetavisita_delete.html'
    success_url = reverse_lazy('tarjetavisita_listar')


class ListTarjetaVisita(ListView):
    model = TarjetaVisita
    template_name = 'paciente/tarjetavisita_list.html'



