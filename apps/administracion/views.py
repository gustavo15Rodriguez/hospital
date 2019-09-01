from io import BytesIO

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle

from apps.administracion.forms import PlantaForm
from apps.administracion.models import Planta
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy

class ReportePlataPdf(View):

    def cabecera(self, pdf):
        archivo_imagen = settings.STATIC_ROOT+'/images/project-1.jpg'
        pdf.drawImage(archivo_imagen, 35, 750, 100, 90, preserveAspectRatio=True)
        pdf.setFont('Helvetica', 16)
        pdf.drawString(230, 790, u"SENA MAS TRABAJO")
        pdf.setFont('Helvetica', 14)
        pdf.drawString(230, 750, u"REPORTE DE PLANTAS")

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
        encabezado = ('ID', 'Nombre', 'No. camas', 'cama')
        detalle = [( planta.id_planta, planta.nombre, planta.numero_camas, planta.cama) for planta in Planta.objects.all()]
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
