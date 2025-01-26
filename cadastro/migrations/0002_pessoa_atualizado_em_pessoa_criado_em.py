# Generated by Django 5.1.5 on 2025-01-26 20:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='atualizado_em',
            field=models.DateTimeField(auto_now=True, verbose_name='Data/hora Criação'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Data/hora Criação'),
            preserve_default=False,
        ),
    ]
