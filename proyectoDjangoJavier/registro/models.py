from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class perfil(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, blank=True)
    web = models.URLField(blank=True)

    def __str__(self): 
        return self.usuario.username

