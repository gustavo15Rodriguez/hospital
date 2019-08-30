from django import forms
from apps.doctores.models import Medico, Diagnostico, HistoriaClinica


class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico

        fields = "__all__"

        labels = {
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'diagnostico': 'Diagnostico',
        }

    def __init__(self, *args, **kwargs):
        super(MedicoForm,self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})



class DiagnosticoForm(forms.ModelForm):
    class Meta:
        model = Diagnostico

        fields = "__all__"

        labels = {
            'descripcion': 'Descripcion',
        }

    def __init__(self, *args, **kwargs):
        super(DiagnosticoForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})




class HistoriaClinicaForm(forms.ModelForm):
    class Meta:
        model = HistoriaClinica

        fields = "__all__"

        labels = {
            'descripcion': 'Descripcion',
        }

    def __init__(self, *args, **kwargs):
        super(HistoriaClinicaForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})