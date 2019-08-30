from django.shortcuts import render
from django.contrib.auth.models import User
from apps.usuarios.forms import RegistroUsuarioForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class UsuarioCrear(CreateView):
    model = User
    form_class = RegistroUsuarioForm
    template_name = ('register.html')
    success_url = reverse_lazy('login')