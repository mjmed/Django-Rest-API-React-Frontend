from django.db import models


class Anestesia(models.Model):
    paciente = models.CharField(max_length=100)
    dia_cirugia = models.DateField()
    tipo_cirugia = models.CharField(max_length=200)
    cirujano = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.paciente

