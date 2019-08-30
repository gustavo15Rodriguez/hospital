from apps.pacientes.models import Paciente, TarjetaVisita
from django import forms

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente

        fields = "__all__"

        labels = {
            'numero_documento': 'Numero Documento',
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'direccion_recidencia': 'Direccion Recidencia',
            'telefono_recidencia': 'Telefono Recidencia',
            'fecha_nacimiento': 'Fecha Nacimiento',
            'tarjeta_paciente': 'Tarjeta Paciente',
            'doctor': 'Doctor',
            'diagnostico': 'Diagnostico',
            'historia_clinica': 'Historia Clinica',
        }

    def __init__(self, *args, **kwargs):
        super(PacienteForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})



class TarjetaVisitaForm(forms.ModelForm):
    class Meta:
        model = TarjetaVisita

        fields = "__all__"

        labels = {
            'numero_tarjeta': 'Numero Tarjeta',
            'hora_comienzo': 'Hora Comienzo',
        }

    def __init__(self, *args, **kwargs):
        super(TarjetaVisitaForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

