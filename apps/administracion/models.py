from django.db import models

class Cama(models.Model):
    id_cama = models.AutoField(primary_key=True)

    def __str__(self):
        return '{}'.format(self.id_cama)

class Planta(models.Model):
    id_planta = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    numero_camas = models.IntegerField()
    cama = models.ForeignKey(Cama, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.nombre)

    class Meta:
        permissions = {
            ('is_administrador', _('Usuario Administrador')),
        }