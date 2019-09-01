from django.db import models
from django.utils.translation import ugettext as _

class Planta(models.Model):
    id_planta = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    numero_camas = models.IntegerField()
    cama = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.nombre)

    class Meta:
        permissions = {
            ('is_administrador', _('Usuario Administrador')),
        }