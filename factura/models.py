from django.db import models

# Create your models here.


class Factura(models.Model):
    fecha = models.DateTimeField()
    cliente = models.ForeignKey('Cliente')
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return "Factura %s (%s)" % (self.id, self.cliente)


class Renglon(models.Model):
    factura = models.ForeignKey('Factura')
    cantidad = models.IntegerField()
    articulo = models.ForeignKey('Articulo')
    total = models.DecimalField(max_digits=6, decimal_places=2)


class Articulo(models.Model):

    descripcion = models.CharField(max_length=50)
    precio_compra = models.DecimalField(max_digits=6, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=6, decimal_places=2)
    cantidad_por_bulto = models.IntegerField()
    codigo_barra = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    def __str__(self):
        return "%s (cod %s)" % (self.descripcion, self.id)




class Cliente(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    condicion = models.CharField(max_length=50, choices=(('responsable', 'Responsable Inscripto'),
                                                         ('montributo', 'Monotributista')))
    cuit = models.CharField(max_length=50)


    def __str__(self):
        return "%s %s" % (self.nombre, self.apellido)