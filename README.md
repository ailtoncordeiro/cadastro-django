# Django Project Setup

Este guia irá ajudá-lo a configurar um novo projeto Django, criar um aplicativo, gerenciar migrações, criar um usuário inicial e iniciar o servidor de desenvolvimento.

## Pré-requisitos
Certifique-se de ter o seguinte instalado em sua máquina:
- Python (>= 3.8)
- pip (gerenciador de pacotes do Python)
- virtualenv (opcional, mas recomendado)

---

## Passos para iniciar um projeto Django

### 1. Criar e ativar um ambiente virtual
É uma boa prática usar um ambiente virtual para isolar as dependências do projeto.

```bash
# Criar um ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
# No Windows
venv\Scripts\activate

# No macOS/Linux
source venv/bin/activate
```

### 2. Instalar o Django

Com o ambiente virtual ativado, instale o Django usando o pip:

```bash
pip install django
```

### 3. Criar um novo projeto

Crie um novo projeto Django com o comando:

```bash
django-admin startproject core .
```
O parâmetro `.` cria o projeto no diretório atual. Substitua `nome_do_projeto` pelo nome desejado para o seu projeto.

### 4. Criar um novo app

No Django, um app é uma funcionalidade ou módulo do projeto. Para criar um novo app:

Quando criar um novo app, adicionar dentro do diretório do novo app criado o arquivo urls.py e a pasta templates para colocar os arquivos HTML

(!!!QUANDO ADICIONA O BASE.HTML DENTRO DO CORE, ELE NÃO FUNCIONA!!!)

```bash
python manage.py startapp paginas
```

Adicione o app recém-criado no arquivo `settings.py` do projeto, na lista `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...,
    'nome_do_app',
]
```

### 5. Criar modelos e migrações

#### Criar modelos
Defina seus modelos no arquivo `models.py` do app:

```python
from django.db import models

class MeuModelo(models.Model):
    nome = models.CharField(max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)
```

#### Criar migrações
Depois de definir os modelos, crie as migrações:

```bash
python manage.py makemigrations
```

#### Aplicar as migrações
Para aplicar as migrações ao banco de dados:

```bash
python manage.py migrate
```

### 6. Criar um usuário administrador

Para acessar o painel de administração do Django, é necessário criar um superusuário:

```bash
python manage.py createsuperuser
```
Siga as instruções para definir o nome de usuário, e-mail e senha.

### 7. Iniciar o servidor de desenvolvimento

Para verificar se tudo está funcionando, inicie o servidor de desenvolvimento do Django:

```bash
python manage.py runserver
```

O servidor será iniciado em `http://127.0.0.1:8000/` por padrão.

---

## Resumo dos comandos principais

- **Criar e ativar ambiente virtual:**
  ```bash
  python -m venv venv && source venv/bin/activate
  ```

- **Instalar Django:**
  ```bash
  pip install django
  ```

- **Criar um projeto:**
  ```bash
  django-admin startproject nome_do_projeto .
  ```

- **Criar um app:**
  ```bash
  python manage.py startapp nome_do_app
  ```

- **Criar migrações:**
  ```bash
  python manage.py makemigrations
  ```

- **Aplicar migrações:**
  ```bash
  python manage.py migrate
  ```

- **Criar superusuário:**
  ```bash
  python manage.py createsuperuser
  ```

- **Iniciar o servidor de desenvolvimento:**
  ```bash
  python manage.py runserver
  ```

---

Pronto! Agora você tem um projeto Django funcional com o básico configurado.
