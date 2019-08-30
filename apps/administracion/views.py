from django.shortcuts import render
from apps.administracion.models import Cama, Planta
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy

class CreateCama(CreateView):
    model = Cama
    form_class = CamaForm
    template_name = 'administracion/cama_form.html'
    success_url = reverse_lazy('cama_listar')


class UpdateCama(UpdateView):
    model = Cama
    form_class = CamaForm
    template_name = 'administracion/cama_form.html'
    success_url = reverse_lazy('cama_listar')


class DeleteCama(DeleteView):
    model = Cama
    form_class = CamaForm
    template_name = 'administracion/cama_delete.html'
    success_url = reverse_lazy('cama_listar')


class ListCama(ListView):
    model = Cama
    template_name = 'administracion/cama_list.html'


#------------------------------Planta------------------------------------


class CreatePlanta(CreateView):
    model = Planta
    form_class = PlantaForm
    template_name = 'administracion/planta_form.html'
    success_url = reverse_lazy('planta_listar')


class UpdatePlanta(UpdateView):
    model = Planta
    form_class = PlantaForm
    template_name = 'administracion/planta_form.html'
    success_url = reverse_lazy('planta_listar')


class DeletePlanta(DeleteView):
    model = Planta
    form_class = PlantaForm
    template_name = 'administracion/planta_delete.html'
    success_url = reverse_lazy('planta_listar')


class ListPlanta(ListView):
    model = Planta
    template_name = 'administracion/planta_list.html'
