from django.core.validators import MinValueValidator
from django.db import models
from .choices import origen_nacional
from comercial.models import Fruta, Exportador


# Create your models here.

class ProveedorNacional(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre Proveedor", unique=True)
    telefono = models.CharField(max_length=20, verbose_name="Telefono Proveedor", blank=True, null=True)
    email = models.EmailField(max_length=50, verbose_name="Email Proveedor", blank=True, null=True)
    observaciones = models.TextField(verbose_name="Observaciones", blank=True, null=True)

class Empaque(models.Model):
    nombre = models.CharField(max_length=20, verbose_name="Nombre Empaque", unique=True)
    peso = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Peso Empaque", validators=[MinValueValidator(0.0)])


class CompraNacional(models.Model):
    proveedor = models.ForeignKey(ProveedorNacional, on_delete=models.PROTECT, verbose_name="Proveedor")
    origen_compra = models.CharField(max_length=20 , choices=origen_nacional, verbose_name="Origen")
    fruta = models.ForeignKey(Fruta, on_delete=models.PROTECT, verbose_name="Fruta")
    peso_compra = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Peso Guia", default=0, validators=[MinValueValidator(0.0)])
    fecha_compra = models.DateField(verbose_name="Fecha de Compra")
    fecha_llegada = models.DateField(verbose_name="Fecha de Llegada")
    numero_guia = models.CharField(max_length=20, verbose_name="Numero Guia", unique=True, blank=True, null=True)
    remision = models.CharField(max_length=20, verbose_name="Remision", blank=True, null=True, default='Sin Remision')
    peso_remision = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Peso Remision", blank=True, null=True, validators=[MinValueValidator(0.0)], default=0)
    precio_compra_exp = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="$ Compra Exportacion", validators=[MinValueValidator(0.0)])
    precio_compra_nal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="$ Compra Nacional", blank=True, null=True, validators=[MinValueValidator(0.0)])
    tipo_empaque = models.ForeignKey(Empaque, on_delete=models.PROTECT, verbose_name="Tipo Empaque")
    cantidad_empaque = models.PositiveIntegerField(verbose_name="Cantidad Empaque", validators=[MinValueValidator(0)])
    observaciones = models.TextField(verbose_name="Observaciones", blank=True, null=True)

class VentaNacional(models.Model):
    compra_nacional = models.OneToOneField(CompraNacional, on_delete=models.CASCADE, verbose_name="Compra Nacional", primary_key=True)
    exportador = models.ForeignKey(Exportador, on_delete=models.PROTECT, verbose_name="Exportador")
    cantidad_empaque_enviada = models.PositiveIntegerField(verbose_name="Cantidad Empaque Enviada", validators=[MinValueValidator(0)], blank=True, null=True)
    peso_bruto_recibido = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Peso Bruto Recibido", validators=[MinValueValidator(0.0)], blank=True, null=True)
    peso_neto_recibido = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Peso Neto Recibido", validators=[MinValueValidator(0.0)], blank=True, null=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.cantidad_empaque_enviada:  # Si no se ha modificado, ingreso la cantidad de empaque de compra.
            self.cantidad_empaque_enviada = self.compra_nacional.cantidad_empaque
        super().save(*args, **kwargs)

class ReporteCalidadExportador(models.Model):
    venta_nacional = models.OneToOneField(VentaNacional, on_delete=models.CASCADE, primary_key=True, verbose_name="Venta Nacional" )
    fecha_reporte = models.DateField(verbose_name="Fecha Reporte")
    kg_exportacion = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Kg Exp", validators=[MinValueValidator(0.0)])
    precio_kg_exp = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="$ Kg Exp", validators=[MinValueValidator(0.0)])
    kg_nacional = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Kg Nal", validators=[MinValueValidator(0.0)])
    precio_kg_nal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="$ Kg Nal", validators=[MinValueValidator(0.0)])
    kg_desecho = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Kg Desecho", validators=[MinValueValidator(0.0)])
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="$ Total", validators=[MinValueValidator(0.0)])





class PreciosGlobalesExportacion(models.Model):
    fruta = models.ForeignKey(Fruta, on_delete=models.PROTECT, verbose_name="Fruta")
    precio_compra_exportacion = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="$ Compra Exportacion")
    precio_compra_nacional = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="$ Compra Nacional")
    fecha_inicio = models.DateField(verbose_name="Fecha Inicio")
    fecha_fin = models.DateField(verbose_name="Fecha Fin")
    exportador = models.ForeignKey(Exportador, on_delete=models.PROTECT, verbose_name="Exportador")




