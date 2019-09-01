from django.shortcuts import render
from django.urls import reverse_lazy

from apps.pacientes.forms import PacienteForm, TarjetaVisitaForm
from apps.pacientes.models import Paciente, TarjetaVisita
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, View

# Reportes PDF
from django.http import HttpResponse
from django.conf import settings
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.platypus import TableStyle, Table
from reportlab.lib.units import cm
from reportlab.lib import colors

class ReportePacientePdf(View):

    def cabecera(self, pdf):
        archivo_imagen = settings.STATIC_ROOT+'/images/project-1.jpg'
        pdf.drawImage(archivo_imagen, 35, 750, 100, 90, preserveAspectRatio=True)
        pdf.setFont('Helvetica', 16)
        pdf.drawString(230, 790, u"SENA MAS TRABAJO")
        pdf.setFont('Helvetica', 14)
        pdf.drawString(230, 750, u"REPORTE DE PACIENTES")

    def get(self, request):
        response = HttpResponse(content_type='application/pdf')
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        self.cabecera(pdf)
        y = 550
        self.tabla(pdf, y)
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

    def tabla(self, pdf, y):
        encabezado = ('No. Documento', 'Nombre', 'Apellidos', 'Direccion', 'F. Nacimiento', 'H. clinica')
        detalle = [(paciente.numero_documento, paciente.nombre, paciente.apellidos, paciente.direccion_recidencia, paciente.fecha_nacimiento, paciente.historia_clinica) for paciente in Paciente.objects.all()]
        detalle_orden = Table([encabezado] + detalle, colWidths=[4 * cm, 4 * cm, 4 * cm, 4 * cm])
        detalle_orden.setStyle(TableStyle(
            (
                ('ALIGN', (0, 0), (3, 0), 'CENTER'),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            )
        ))

        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 60, y)

class CreatePaciente(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'pacientes/paciente_form.html'
    success_url = reverse_lazy('paciente_listar')


class UpdatePaciente(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'pacientes/paciente_form.html'
    success_url = reverse_lazy('paciente_listar')


class DeletePaciente(DeleteView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'pacientes/paciente_delete.html'
    success_url = reverse_lazy('paciente_listar')


class ListPaciente(ListView):
    model = Paciente
    template_name = 'pacientes/paciente_list.html'


#------------------------------------Tarjeta Visita------------------------------

class ReporteTarjetaPdf(View):

    def cabecera(self, pdf):
        archivo_imagen = settings.STATIC_ROOT+'/images/project-1.jpg'
        pdf.drawImage(archivo_imagen, 35, 750, 100, 90, preserveAspectRatio=True)
        pdf.setFont('Helvetica', 16)
        pdf.drawString(230, 790, u"SENA MAS TRABAJO")
        pdf.setFont('Helvetica', 14)
        pdf.drawString(225, 750, u"REPORTE DE TARJETAS DE VISITA")

    def get(self, request):
        response = HttpResponse(content_type='application/pdf')
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        self.cabecera(pdf)
        y = 550
        self.tabla(pdf, y)
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

    def tabla(self, pdf, y):
        encabezado = ('ID', 'No. tarjeta', 'H. inicio')
        detalle = [(tarjeta.id_tarjeta, tarjeta.numero_tarjeta, tarjeta.hora_comienzo) for tarjeta in TarjetaVisita.objects.all()]
        detalle_orden = Table([encabezado] + detalle, colWidths=[4 * cm, 4 * cm, 4 * cm, 4 * cm])
        detalle_orden.setStyle(TableStyle(
            (
                ('ALIGN', (0, 0), (3, 0), 'CENTER'),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            )
        ))

        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 60, y)


class CreateTarjetaVisita(CreateView):
    model = TarjetaVisita
    form_class = TarjetaVisitaForm
    template_name = 'pacientes/tarjetavisita_form.html'
    success_url = reverse_lazy('tarjetavisita_listar')


class UpdateTarjetaVisita(UpdateView):
    model = TarjetaVisita
    form_class = TarjetaVisitaForm
    template_name = 'pacientes/tarjetavisita_form.html'
    success_url = reverse_lazy('tarjetavisita_listar')


class DeleteTarjetaVisita(DeleteView):
    model = TarjetaVisita
    form_class = TarjetaVisitaForm
    template_name = 'pacientes/tarjetavisita_delete.html'
    success_url = reverse_lazy('tarjetavisita_listar')


class ListTarjetaVisita(ListView):
    model = TarjetaVisita
    template_name = 'pacientes/tarjetavisita_list.html'



