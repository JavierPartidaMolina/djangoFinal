from django.contrib import admin
from .models import Pregunta, Respuesta

class PreguntaAdmin(admin.ModelAdmin):
    readonly_fields=('created' , 'updated')

admin.site.register(Pregunta,PreguntaAdmin),
admin.site.register(Respuesta)