from django.contrib import admin

# Register your models here.
from .models import Ropa, Tejido, Tipo

admin.site.register(Ropa),
admin.site.register(Tejido),
admin.site.register(Tipo),
