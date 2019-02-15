from django.db import models
from django.contrib.auth.models import User
from GestionRopa.models import Ropa


class Pregunta(models.Model):
    Pregunta = models.CharField(max_length=200,verbose_name="pregunta")
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="usuario")
    Ropa = models.ForeignKey(Ropa, on_delete=models.CASCADE,verbose_name="ropa")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, **kwargs):
        if kwargs is not None and 'request' in kwargs and self.user is None:
            request = kwargs.pop('request')
            self.user = request.user
        super().save(**kwargs)

    def __str__(self):
        return self.Pregunta 

class Respuesta(models.Model):
    Respuesta = models.CharField(max_length=200, verbose_name="respuesta")
    Pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE,verbose_name="pregunta")
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="usuario")

    def save(self, **kwargs):
        if kwargs is not None and 'request' in kwargs and self.user is None:
            request = kwargs.pop('request')
            self.user = request.user
        super().save(**kwargs)
        
    def __str__(self):
        return self.Respuesta
