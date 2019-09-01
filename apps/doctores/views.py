from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, View

from apps.doctores.forms import MedicoForm, DiagnosticoForm, HistoriaClinicaForm
from apps.doctores.models import Diagnostico, Medico, HistoriaClinica
from django.urls import reverse_lazy

# Reportes PDF
from django.http import HttpResponse
from django.conf import settings
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.platypus import TableStyle, Table
from reportlab.lib.units import cm
from reportlab.lib import colors

class ReporteMedicoPdf(View):

    def cabecera(self, pdf):
        archivo_imagen = settings.STATIC_ROOT+'/images/project-1.jpg'
        pdf.drawImage(archivo_imagen, 35, 750, 100, 90, preserveAspectRatio=True)
        pdf.setFont('Helvetica', 16)
        pdf.drawString(230, 790, u"SENA MAS TRABAJO")
        pdf.setFont('Helvetica', 14)
        pdf.drawString(230, 740, u"REPORTE DE MEDICOS")

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
        encabezado = ('ID', 'Nombre', 'Apellido', 'Diagnostico')
        detalle = [(medico.id_medico, medico.nombre, medico.apellidos, medico.diagnostico) for medico in Medico.objects.all()]
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

class ReporteDiagnosticoPdf(View):

    def cabecera(self, pdf):
        archivo_imagen = settings.STATIC_ROOT + '/images/project-1.jpg'
        pdf.drawImage(archivo_imagen, 35, 750, 100, 90, preserveAspectRatio=True)
        pdf.setFont('Helvetica', 16)
        pdf.drawString(230, 790, u"SENA MAS TRABAJO")
        pdf.setFont('Helvetica', 14)
        pdf.drawString(225, 740, u"REPORTE DE DIAGNOSTICOS MEDICOS")


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
        encabezado = ('ID', 'Descripcion')
        detalle = [(diagnostico.id_diagnostico, diagnostico.descripcion) for diagnostico in Diagnostico.objects.all()]
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

class ReporteHistoriaPdf(View):

    def cabecera(self, pdf):
        archivo_imagen = settings.STATIC_ROOT + '/images/project-1.jpg'
        pdf.drawImage(archivo_imagen, 35, 750, 100, 90, preserveAspectRatio=True)
        pdf.setFont('Helvetica', 16)
        pdf.drawString(230, 790, u"SENA MAS TRABAJO")
        pdf.setFont('Helvetica', 14)
        pdf.drawString(225, 740, u"REPORTE DE HISTORIAS CLINICAS")

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
        encabezado = ('ID', 'Descripcion')
        detalle = [(historia.id_historia, historia.descripcion) for historia in HistoriaClinica.objects.all()]
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
