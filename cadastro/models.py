from django.db import models

# Create your models here.

class TimeStamp(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name='Data/hora Criação')
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name='Data/hora Criação')

    class Meta:
        abstract = True

class Pessoa(TimeStamp):
    cpf = models.CharField(max_length=14, unique=True, verbose_name='CPF')
    nome = models.CharField(max_length=255, verbose_name='Nome')
    email = models.CharField(max_length=255, verbose_name='e-mail', null=True)

    # Campo que será exibido na lista da pagina de administração do django
    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
