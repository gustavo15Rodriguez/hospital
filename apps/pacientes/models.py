from django.db import models
from apps.doctores.models import Medico, Diagnostico

class TarjetaVisita(models.Model):
    id_tarjeta = models.AutoField(primary_key=True)
    numero_tarjeta = models.CharField(max_length=40)
    hora_comienzo = models.CharField(max_length=40)

    def __str__(self):
        return '{}'.format(self.numero_tarjeta)


class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    numero_documento = models.CharField(max_length=40)
    historia_clinica = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    direccion_recidencia = models.CharField(max_length=40)
    telefono_recidencia = models.IntegerField()
    fecha_nacimiento = models.CharField(max_length=40)
    tarjeta_paciente = models.ForeignKey(TarjetaVisita,on_delete=models.CASCADE, blank=True, null=True)
    doctor = models.ForeignKey(Medico, on_delete=models.CASCADE, blank=True, null=True)
    diagnostico = models.ForeignKey(Diagnostico, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return '{}{}'.format(self.nombre, self.apellidos)