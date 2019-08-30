from django.db import models

class Diagnostico(models.Model):
    id_diagnostico = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=4 0)

    def __str__(self):
        return '{}'.format(self.descripcion)


class HistoriaClinica(models.Model):
    id_historia = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=40)

    def __str__(self):
        return '{}'.format(self.descripcion)


class Medico(models.Model):
    id_medico = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    diagnostico = models.ForeignKey(Diagnostico,on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return '{}{}'.format(self.nombre, self.apellidos)
