from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

class Competiciones(models.Model):
    Nombre = models.CharField(max_length=50,verbose_name="nombre")
    Lugar = models.CharField(max_length= 50,verbose_name="lugar")
    Descripcion = RichTextUploadingField(max_length=900, verbose_name="descripcion")
    Fecha = models.DateField(null=True,blank=True,verbose_name="fecha")
    User = models.ManyToManyField(User,related_name="CompeticionUser")

    class Meta():
        verbose_name="Competicion"
        verbose_name_plural="Competiciones"

    def __str__(self):
        return self.Nombre 

class Participaciones(models.Model):
    Competiciones = models.ForeignKey(Competiciones, verbose_name="competiciones", on_delete=models.PROTECT)
    User = models.ForeignKey(User, verbose_name="user", on_delete=models.PROTECT)
    posicion = models.IntegerField(null=True, blank=True)

    class Meta():
        verbose_name="Participacion"
        verbose_name_plural="Participaciones"