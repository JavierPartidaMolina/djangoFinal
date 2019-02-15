from django.db import models

class Noticia(models.Model):
    Titulo = models.CharField(max_length=50,verbose_name="titulo")
    Resumen = models.CharField(max_length=300,verbose_name="resumen")
    Cuerpo = models.CharField(null=True,blank=True,max_length= 1000,verbose_name="cuerpo")
    Imagen = models.ImageField(null=True,blank=True,upload_to= 'imagenes/', verbose_name="imagen")

    def __str__(self):
        return self.Titulo 
