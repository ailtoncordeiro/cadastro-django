from django.urls import path
from .views import cadastro_pessoa, listar_pessoa

urlpatterns = [
    path('cadastro/', cadastro_pessoa, name='cadastrar-pessoa'),
    path('listar/', listar_pessoa, name='listar-pessoa'),
]