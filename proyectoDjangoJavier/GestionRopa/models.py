from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Tipo(models.Model):
    Nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre

class Tejido(models.Model):
    Nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre

class Ropa(models.Model):
    Nombre = models.CharField(max_length=50,verbose_name="nombre")
    Precio = models.IntegerField(verbose_name="precio")
    Talla = models.CharField(null=True,blank=True,max_length= 10,verbose_name="talla")
    Imagen = models.ImageField(null=True,blank=True,upload_to= 'imagenes/', verbose_name="imagen")
    Tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE,verbose_name="tipo")
    Tejido = models.ForeignKey(Tejido, on_delete=models.CASCADE,verbose_name="tejido")
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="usuario")
    Tienda = models.CharField(max_length=50,verbose_name="tienda")

    def save(self, **kwargs):
        if kwargs is not None and 'request' in kwargs and self.user is None:
            request = kwargs.pop('request')
            self.user = request.user
        super().save(**kwargs)

    def __str__(self):
        return self.Nombre 

    
