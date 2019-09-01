from django import forms
from apps.administracion.models import Planta

class PlantaForm(forms.ModelForm):
    class Meta:
        model = Planta

        fields = "__all__"

        labels = {
            'nombre': 'Nombre',
            'numero_camas': 'Numero Camas',
            'cama': 'Cama',
        }

    def __init__(self, *args, **kwargs):
        super(PlantaForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

