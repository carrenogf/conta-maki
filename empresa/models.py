from django.db import models


class Empresa(models.Model):
    cuit = models.CharField(max_length=13)
    razon_social = models.CharField(max_length=100)
    actividad = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    
    def __str__(self):
        return self.razon_social