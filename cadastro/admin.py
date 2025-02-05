from django.contrib import admin
from .models import Pessoa, Infracao, Foto

# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Infracao)
admin.site.register(Foto)