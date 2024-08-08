from django.db import models
from empresa.models import Empresa
from django.core.exceptions import ValidationError

tipo_liquidacion_choices = (
    ("M","M"),
    ("D","D"),
    ("H","H")
)
tipo_concepto_choices = (
    ("C","C"),
    ("D","D")
)
class Empleado(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=8)
    cuil = models.CharField(max_length=13)
    tipo_liquidacion = models.CharField(max_length=2,choices=tipo_liquidacion_choices)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    fecha_ingreso = models.DateField()
    conyugue = models.BooleanField(default=False)
    hijos = models.IntegerField(default=0)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=20,blank=True, null=True)
    direccion = models.CharField(max_length=300,blank=True, null=True)
    activo = models.BooleanField(default=True)
    sicoss_cod_situacion = models.CharField(max_length=3)
    sicoss_cod_condicion = models.CharField(max_length=3)
    sicoss_cod_actividad = models.CharField(max_length=3)
    sicoss_cod_mod_contratacion = models.CharField(max_length=3)
    sicoss_cod_siniestrado = models.CharField(max_length=3)
    sicoss_cod_localidad = models.CharField(max_length=3)
    cod_obra_social = models.CharField(max_length=20)
    cantidad_adherentes = models.IntegerField(default=0)
    cbu = models.CharField(max_length=22,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre + ' ' + self.apellido


class Liquidacion(models.Model):
    nombre = models.CharField(max_length=200)
    abierta = models.BooleanField(default=True)
    periodo = models.DateField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Liquidacion"
        verbose_name_plural = "Liquidaciones"
    def __str__(self):
        return self.nombre + ' - ' + self.periodo.strftime('%m/%Y')
    
    

class Recibo(models.Model):
    liquidacion = models.ForeignKey('liquidacion', on_delete=models.CASCADE, limit_choices_to={'abierta': True})
    empleado = models.ForeignKey('Empleado', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.empleado.nombre + ' ' + self.empleado.apellido + ' - ' + self.liquidacion.periodo.strftime('%m/%Y')

    def clean(self):
        if self.empleado.empresa != self.liquidacion.empresa:
            raise ValidationError('El empleado no pertenece a la misma empresa de la liquidación.')
    
class Concepto(models.Model):
    codigo = models.CharField(max_length=10,unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    tipo = models.CharField(max_length=1, choices=tipo_concepto_choices)
    computa_sac = models.BooleanField(default=False)
    computa_ObraSocial = models.BooleanField(default=False)
    computa_Aporte = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre + ' - ' + self.tipo

class DetalleRecibo(models.Model):
    recibo = models.ForeignKey(Recibo, on_delete=models.CASCADE)
    concepto = models.ForeignKey(Concepto, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.concepto.nombre