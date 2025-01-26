from django.shortcuts import render, redirect
from .models import Pessoa

# Create your views here.
def cadastro_pessoa(request):
    #Se a requisição for do tipo POST ele bate aqui
    if request.method=='POST':
        pessoa = Pessoa()
        pessoa.nome = request.POST.get('nome')
        pessoa.email = request.POST.get('email')
        pessoa.cpf = request.POST.get('cpf')
        pessoa.save()

        return redirect('listar-pessoa')
    
    #Se a requisição for do tipo GET ele bate aqui
    return render(request, 'cadastrar.html')

def listar_pessoa(request):
    pessoas = Pessoa.objects.all()
    response = {
        'pessoas': pessoas
    }

    return render(request, 'listar.html', response)