from django.db import models

class Diagnostico(models.Model):
    id_diagnostico = models.CharField(primary_key=True, max_length=10)
    descripcion = models.CharField(max_length=40)


class Medico(models.Model):
    id_medico = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    diagnostico = models.ForeignKey(Diagnostico,on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return '{}{}'.format(self.nombre, self.apellidos)
