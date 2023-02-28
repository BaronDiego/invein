import datetime
from django.db import models
from django.contrib.auth.models import User


class Base(models.Model):
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    uc = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario que Crea")
    um = models.IntegerField(blank=True, null=True, verbose_name="Usuario que modifica")


ESTADO = (
    ('SI', 'SIN INICIO'),
    ('I', 'INICIANDO'),
    ('P', 'PROGRESANDO'),
    ('A', 'AVANZADO'),
    ('T', 'TERMINADO'),
)

APROBADO = (
    ('S', 'Si'),
    ('N', 'No'),
)

class Comercial(models.Model):
    nombre = models.CharField(max_length=250)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    uc = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario que Crea")
    um = models.IntegerField(blank=True, null=True, verbose_name="Usuario que modifica")

    class Meta:
        ordering = ['-creado']

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=250)
    direccion = models.CharField(max_length=250)
    telefono = models.IntegerField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    uc = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario que Crea")
    um = models.IntegerField(blank=True, null=True, verbose_name="Usuario que modifica")

    class Meta:
        ordering = ['-creado']

    def __str__(self):
        return self.nombre
    

class Oferta(models.Model):
    comercial = models.ForeignKey(Comercial, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nro_de_oferta = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=250)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    uc = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario que Crea")
    um = models.IntegerField(blank=True, null=True, verbose_name="Usuario que modifica")

    class Meta:
        ordering = ['-creado']

    def __str__(self):
        return self.nro_de_oferta


class Montaje(Base):
    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE)
    costo = models.BigIntegerField(default=0, blank=True, null=True)
    aprobado = models.CharField(max_length=2, choices=APROBADO)
    numero_orden =  models.CharField(max_length=20)
    solicitud_de_factura = models.CharField(max_length=20)
    nro_Factura_invein = models.CharField(max_length=20)
    ceco = models.CharField(max_length=20)
    valor_de_venta = models.BigIntegerField(default=0, blank=True, null=True)
    avance = models.FloatField(max_length=5, blank=True, null=True)
    estado = models.CharField(max_length=2, choices=ESTADO)

    class Meta:
        ordering = ['-creado']

    def __str__(self):
        return self.numero_orden


class Fabricacion(Base):
    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE)
    costo = models.BigIntegerField(default=0, blank=True, null=True)
    aprobado = models.CharField(max_length=2, choices=APROBADO)
    numero_orden =  models.CharField(max_length=20)
    solicitud_de_factura = models.CharField(max_length=20)
    nro_Factura_invein = models.CharField(max_length=20)
    ceco = models.CharField(max_length=20)
    valor_de_venta = models.BigIntegerField(default=0, blank=True, null=True)
    avance = models.FloatField(max_length=5, blank=True, null=True)
    estado = models.CharField(max_length=2, choices=ESTADO)

    class Meta:
        ordering = ['-creado']

    def __str__(self):
        return self.numero_orden


class Proyecto(Base):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=250)
    numero_contrato = models.CharField(max_length=150,verbose_name="Número Contrato")
    objeto = models.TextField()
    estado = models.CharField(max_length=2, choices=ESTADO)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    valor_proyecto = models.BigIntegerField(default=0, blank=True, null=True)
    valor_proyecto_planeado = models.BigIntegerField(default=0, blank=True, null=True, verbose_name='Costo Planeado')
    programado = models.FloatField(max_length=5, blank=True, null=True)
    avance = models.FloatField(max_length=5, blank=True, null=True)
    responsable = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ['-creado']

    def __str__(self):
        return self.nombre

    def duracion(self):
        duracion = self.fecha_fin - self.fecha_inicio
        return duracion.days
    


class Actividad(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    actualizado = models.DateTimeField(auto_now=True)
    programado = models.FloatField(max_length=5, blank=True, null=True)
    avance = models.FloatField(max_length=5, blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    uc = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario que Crea")
    um = models.IntegerField(blank=True, null=True, verbose_name="Usuario que modifica")

    class Meta:
        ordering = ['creado']

    def __str__(self):
        return self.nombre

    def duracion(self):
        duracion = (self.fecha_fin - self.fecha_inicio) + datetime.timedelta(days=1)
        return duracion.days
    

class CurvaS(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    fecha = models.DateField()
    programado = models.FloatField(max_length=5, blank=True, null=True)
    avance = models.FloatField(max_length=5, blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    uc = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario que Crea")
    um = models.IntegerField(blank=True, null=True, verbose_name="Usuario que modifica")

    class Meta:
        ordering = ('creado',)

class Comentarios(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='comentarios')
    comentarios = models.TextField()
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    uc = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario que Crea")
    um = models.IntegerField(blank=True, null=True, verbose_name="Usuario que modifica")

    class Meta:
        ordering = ('-creado',)
             
