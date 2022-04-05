# Curso de Python Codar.Me

## Importação de bibliotecas:
```
import os // biblioteca para acessar comandos do sistema operacional.
Ex: os.system('cls') or None // Limpa o prompt de comando.
import json // Para trabalhar com o formto JSON

```
## Extensões do VSCode:

Django https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django

## Resumos dos Módulos  
### Modulo 01 e 02 - Configurações de ambiente

#### 01. Instalação do Python.
Instalar o python versão 3.10.1

#### 02. Configurando o VSCode
1) Instalar VSCode  
2) Instalar a extensão python  
3) Alterando para o interpretador python  
3.1) View>Command Palette>Digitar"Interpretador">Selecionar a versão 3.10.1 do python  
3.2) Atalho Command Palette - Ctrl + Shift + P  
4) View>Command Palette>Digitar"Path">Selecionar a cópia do arquivo  
4.1) Entrar no diretório do arquivo (.py) e depois rodar o comando "code ."  
4.2) Este comando irá abrir o vscode já na pasta com o arquivo (.py).  
5) Abrir o modo interativo do python:
5.1) Abrir um novo terminal e digitar Python3.  
5.2)  Atalho Command Palette - Ctrl + Shift + P e depois digitar "REPL"  

### Módulo 03 - Introdução ao python
#### 01. O que é python

Podemos nos referir a três conceitos:  
1) Linguagem de programação //Código em si  
2) Código-fonte (.py) // Script em python  
3) Interpretador Python  

Comando:
```
type("Texto") // retorna o tipo da variável.
# Comentário de uma linha
"""
Bloco de comentários
"""
```

### Módulo 04 - Operações no python
#### Operadores Aritméticos
```
Principais operadores são (*), (/), (+), (-). 
Em uma divisão na versão 3 do python o operados (/) realiza a divisão entre dois números,  
sempre retornando um float. Para realizar um opereção que retorne um número inteiro  
devemos utilizar o operador (//).  
Também temos o operador (**) de exponenciação e o opedaror módulo (%) que retorna o resto da divisão. 
```
#### Operadores Relacionais
```
Os operadores relacionais retornão um valor booleano. 
(==) Comparação
(!=) Diferenciação
(>),(<),(>=),(<=)
```
#### Operadores Lógicos
```
Temos três tipos de operadores lógicos, são eles:
- NOT
- AND
- OR
```
#### Recebendo Input do usuário
```
input("Digite: ")
(\n) pula linha
int("texto") realiza a converão de uma string para um número inteiro
```

### Módulo 05 - Controle de fluxo
Condicional e Laços de repetição são utilizados para controlar o fluxo do código.
```
# Exemplo de Condicional:
if [condição]:
   print()
elif [condição]:
   print()
else:
   print()

# Exemplo de Laço de repetição
x = valor
while [condição]:
    print()
    x += 1
```

### Módulo 06 - Estrutura de Dados

Algumas das principais estruturas de dados do Python são:
```
Listas ( list ): [1, 2, 3]
Tuplas ( tuple ): (1, 2, 3)
Conjuntos ( set ): {1, 2, 3}
Dicionários ( dict ): {"a": 1, "b": 2, "c": 3}
```
#### Listas
Comumente utilizadas para armazenar valores. Ex: notas.
As listas são criadas utilizando colchetes []
Comandos:
```
Ex: notas = [8.5, 10, 7.98]
lista.append(valor) # Adiciona um valor/objeto ao final da lista
lista.pop() # Remove por padrão o último elemento da lista
lista.sort() # Ordena os valores da lista (Crescente)
lista.sort(reverse=True) # Ordena os valores da lista (Decrescente)
lista.insert(0, 8) # Insere um valor/objeto no indice indicado da lista
lista.pop(0) # Remove o valor/objeto do indíce 0
```

#### Tuplas
Comumente utilizadas para armazenar objetos. Ex: Pessoa.
As tuplas são criadas utilizando parênteses ()
Tuplas são imutáveis não permitem atribuição após serem criadas.
Comandos:
```
Ex: pessoa = ("João", 22, True)
nome, idade, admin = pessoa # "unpacking" - Desempacotamento de tuplas
print(nome, idade, admin)
```
#### Conjuntos Set
Não são ordenados.  
Não permitem elementos repetidos.  
Como não permitem duplicados podemos utilizar esta restrição para criar um conjunto
a partir de um lista com elementos duplicados. Assim, conseguimos remover dados duplicados.
Comandos:
```
Ex: usuarios = {"alice", "bob"}
    usuarios_2 = set(["alice","bob"])
- set([])
- add()
- union ou | 
- intersection &
- difference ou -
```

#### Dicionários
Dicionários são estruturas que armazenam pares de chave-valor.
Comandos:
```
# {key: value}
Ex: pessoa = {
      "nome": "Alice",
      "idade": 27,
      "admin": False
    }
print(pessoa["nome"]) # é utilizado [] para acessar os campos do objeto.

# dict.items()
Ex:
for key, value in lista.items():
   print(key, value)

# dict.keys()
Ex:
for key in lista.keys()
   print(key)
   
# dict.values()
Ex:
for value in lista.values()
   print(value)
```

### Módulo 07 - Funções

São blocos de código isolados que podem ser chamados para realizar alguma ação.  
Como declarar uma função?
```
def f(x):
    return x
```
Parâmetro vs. argumento  
Parâmetro é a variavel declarada na função.  
Argumento é o valor passado no parâmetro.  
keywords arguments - São argumentos nomeados.  
É interessante utilizar este recurso para facilitar o entendimento dos argumentos passados na função.  

Exemplo de keywords arguments:  
```
def dar_boas_vindas(nome, sobrenome, nome_do_curso):
    print("Olá,", nome, sobrenome)
    print("Bem-vindo ao curso de", nome_do_curso)

dar_boas_vindas(nome="João", sobrenome="Silva", nome_do_curso="Python")

*OBS: Argumentos nomeados, sempre devem vir depois de argumentos não nomeados.
```

Uma função sempre possui um retorno, mesmo que o mesmo não esteja declarado.
Neste caso o retorno padrão é igual a None.

Exemplo de parâmetro com valor padrão:
```
def calcular_conta(consumo, taxa_servico=0.1, desconto_fidelidade=5):
    servico = consumo * taxa_servico
    desconto = consumo * desconto_fidelidade
    valor = (consumo + servico) - desconto
    return valor

valor = calcular_conta(consumo=100, taxa_servico=0.1, desconto_fidelidade=0.05)
print("O valor a ser pago é:", valor)

*OBS: Parametros com valor, sempre devem vir depois de parâmetros sem valor padrão.
```

### Módulo 08 - Programação Orientada a Objetos

#### Objetos Imutáveis, Valor e Referência  
Em python existem valores que podem ser atribuidos a uma variavel que são imutáveis. (Ex. um valor inteiro)  
É criado uma instância em memória onde fica armazenado o valor da variavel. Portanto, a variavel aponta para  
a localização do espaço em memória que por sua vez, contem o valor recebido pela variavel. (Conceito de valor e referência).

#### Objetos Mutáveis
São objetos que podem sofrer alteração ex: Listas, Conjuntos e precisamos tomar cuidado.  
Esse objetos devem ser tratados com atenção, pois podem gerar inconsistências de dados.  

### Classes e objetos
Definindo Classes:  
Classes são estrutura de códigos em que conseguimos definir nossos próprios tipos (String, Float ...) e metódos.  
**Estado:** representação dos dados que o objeto armazena.  
**Comportamento:** São os métodos que o objeto pode realizar.  
```
d = {"a": 1}  # dicionário é o tipo e "d" é o objeto.
d.keys() # método
```
Criando uma classe:  
```
class Evento:
    pass # Informa que é uma classe vazia (pass) ou (...).
```
Adcionando um atributo de classe:
```
class Evento:
    id = 1
```
Adicionando um método:
```
class Evento:
    def altera_nome_evento(self, novo_nome):
        print("Alterando nome do evento")
        self.nome = novo_nome
```
Adicionado um construtor:
```
class Evento:
    def __init__(self, nome):
        self.nome = nome
        self.local = "Brasil"

# Construtor com um valor que não precisa ser preenchindo
class Evento:
    def __init__(self, nome, apelido=""):
        self.nome = nome
        self.apelido = apelido
```
Definição de métodos de (Instância, Classes e Estáticos):
```
class Evento:
    def metodo_intancia(self):
        return ("método de instância chamado", self)
    
    @classmethod
    def metodo_classe(cls):
        return ("método de classe chamado", cls)
    
    @staticmethod
    def metodo_estatico():
        return "estático chamado"
```
Herança e sobrescrita de metodos:
```
# Herança - Evento online é uma especialização da classe Evento
class Evento:
    def __init__(self, nome, local=""):
        self.nome = nome
        self.local = local
        self.id = Evento.id
        Evento.id += 1

class EventoOnline(Evento):
    def __init__(self, nome, _=""):
        local = f"https://tamarcado.com/eventos?id={EventoOnline.id}"
        super().__init__(nome, local)
```
Criação de Módulos - Organização de classes por arquivo
Realizamos a importação dos arquivos .py para acessar as classes do projeto.
```
from evento import Evento
# from nome_arquivo import nome_classe
```


### Módulo 09 - Protocolo HTTP (Client Servidor)
Criando um servidor:
````
# Importação das classes (HTTPServer, BaseHTTPRequestHandler) da bibioteca padrão do Python (http.server):
# BaseHTTPRequestHandler tem a missão de receber as requisições
from http.server import HTTPServer, BaseHTTPRequestHandler

# Criando uma classe que herda de BaseHTTPRequestHandler e implementa o metódo Get:
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200) # Define o retorno do servidor como 200
        self.send_header("Content-Type", "text/html; charset=UTF-8") # Define a codificação para UTF-8
        self.send_header("Teste", "abc") # Adiciona um cabeçalho
        self.end_headers() # Informa que não existem mais cabeçahos
        self.wfile.write("Olá, mundo!".encode()) # Retorna uma mensagem para o cliente
        # encode() Converte a string para binário

# Contrutor por default espera receber o endereço e a porta.
server = HTTPServer(('localhost', 8000), SimpleHandler) 
# Faz com que o servidor fique ativo aguardando uma requisição
server.serve_forever() 
````

### Módulo 10 - Configurando um ambiente virtual

Quando trabalhamos com python devemos criar um ambiente virtual para trabalhar com diferentes  
versões de pacotes instalados em cada projeto. 

Comandos: 
```
Set Path 
```
Exibe a variavel de ambiente Path (usuários windows).

````
cd C:\Users\Caio\Desktop\CursoDePythonCodarme\venv\Scripts
ls
````
Os dois comandos acima são realizados para verificarmos aonde está instalado o nosso interpretador python.

#### Criando um ambiente virtual

No diretório do projeto, digite o comando abaixo:
````
python3 -m venv [nome do ambiente]
````
Para executar o comando acima é necessário estar no diretório do projeto:

Depois, podemos configurar o interpretador padrão seguindo este caminho:
Paleta de Comandos/Selecionar interpretador/ Selecionar o "venv"

Para ativar pelo shell:
CMD:
````
C:\\...  venv\Scripts\activate.bat
````
POWER SHELL
````
C:\\...  venv\Scripts\activate.ps1
````
Para desativar:
````
deactivate
````

Instalando depêndencias externas:
PIP - Package Installer for Python
````
pip install flask
pip install django 
````

### Módulo 11 - API HTTP com Flask

Comandos:
````
flask run
````
Para executar o servidor.

````
from flask import Flask

app = Flask(__name__)

@app.route("/") # Mapeamento de rotas
def index():
    return "<h1>Flask configurado com sucesso!</h1>"
````
Criando um exemplo de API simples.

#### Variáveis de ambiente do Flask
FLASK_APP Serve para apontar para o python qual aplicação será rodada dentro do framework do flask.
Comando para setar um valor a variável FLASK_APP:
````
CMD: 
> set FLASK_APP=main.py
> flask run

PowerShell:
> $env:FLASK_APP = "main.py"
> flask run

***OBS: É necessário estar no diretório raiz do projeto para executar os comandos.
````
FLASK_ENV Serve para apontar qual o ambiente em que está sendo executado a aplicação:
Comando para setar um valor a variável FLASK_ENV:
````
CMD: 
> set FLASK_ENV=development
> flask run

PowerShell:
> $env:FLASK_ENV = "development"
> flask run
***OBS: É necessário estar no diretório raiz do projeto para executar os comandos.
````
Podemos utilizar também o comando abaixo para executar o flask:
````
app.run()
````

Converte um objeto para um dicionário:
Comando nativo do python
````
obj.__dict__
````

Jsonify:
Utilizado para converter um objeto para JSON, também realiza as configurções dos Headers para o navegador:
Ex: Content-Type: application/json
````
from flask import Flask, jsonify
...
return jsonify(eventos_dict)
````

Adicionando um parametro do tipo inteiro na rota com Flask:
````
@app.route("/api/eventos/<int:id>/")
def detalhar_evento(id):
    for ev in eventos:
        if ev.id == id:
            return jsonify(ev.__dict__)
````
Lançando uma exceção (abort, make_response e @app.errorhandler())

Devemos importar as bibliotecas:
````
from flask import Flask, jsonify, abort, make_response
````

Exemplo de exceção com o status code 404 utilizando apenas o **abort**:
````
abort(404, "Evento não encontrado")
````
Exemplo de exceção com o status code 404 utilizando **make_response**:
````
data = {"erro": f"Não encontrei o evento com id: {id}"}
return make_response(jsonify(data), 404)    
````
Exemplo de exceção com o status code 404 utilizando **@app.errorhandler(404)**:
````
@app.errorhandler(404)
def nao_encontrado(erro):
    # data = {"erro": str(erro)} 
    return (jsonify(erro=str(erro)), 404)
 
abort(404, f"Não encontrei o evento com id: {id}")
````

Criando uma rota com o método POST:

Devemos importar as bibliotecas request e json
````
from flask import Flask, jsonify, abort, make_response, request, json
````

Exemplo:
````
@app.route("/api/eventos/", methods=["POST"])
def criar_evento():
    data = json.loads(request.data)  # Converte de json para dicionário
    nome = data.get("nome") # Realiza o parse do campo "nome" recebido na requisição
    local = data.get("local")
    return data
````

Conversões json:
````
json.dumps dict => json
json.loads(json) = > dict
data = request.get_json()  
````

Validações:
Após realizar o parse dos campos da requisição recebida, precisamos aplicar validações,
para nossa API contemple as regras de negócio. 
````
if not nome:
        abort(400, "'nome' precisa ser informado!")
````

Adicionando o retorno do id do evento criado para o cliente e o direcionamento para a rota de detalhes (HATEOAS)
````
return {
         "id": evento.id,
         "url": f"/api/eventos/{evento.id}/"
       }
````

## Módulo 12 - Desenvolvimento Web com Django

Instalando o Django 
``
pip install Django==4.0.2
``  
  
Comando para criar um projeto Django:
````
django-admin startproject [Nome do projeto] .
````
Comando para iniciar o servidor:
````
python manage.py runserver
````
Comando para criar um aplicativo:
````
django-admin startapp [nome do app]
````
Após criar o app é necessário configurar as urlpatterns do app.
Assim o projeto fica organizado e utilizamos uma boa prática.

Passo a passo:
Criar um arquivo urls.py no diretorio do app;
Ex:
````
from django.urls import URLPattern
from django.urls import path
from agenda.views import index

urlpatterns = [
    path("", index)
]
````
Adicionar as configurações abaixo no arquivo urls.py do diretório raiz do projeto:
````
from django.urls.conf import include
from django.contrib import admin
from django.urls import path

from agenda.urls import urlpatterns as agenda_urls
from agenda.views import index

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", include(agenda_urls))
]
````

Criando Classes:

Dendro do diretório de sua aplicação em django temos um arquivo chamado models.py para criamos as nossas classes.

Criando Templates HTML:

Devemos criar uma pasta chamada templates dendro do diretório de sua aplicação. Depois, criar outra pasta dentro de templates
com o nome da aplicação. Nesta última pasta adicionamos o arquivo .html.

Ex. Django-Template HTML:
````
<html>
    <h1>Evento: {{evento.nome}}</h1>
    <p>Categoria: {{evento.categoria}}</p>
    <p>Local: {{evento.local}}</p>
    <p>Link: {{evento.link}}</p>
</html>
````
É utilizado {{}} duas chaves para interpolar os valores das variáveis.

Utilizando o template loader para carregar a view:

Importação da biblioteca:
````
from django.template import loader
````

Exemplo de carregamento de template e injeção de valores:

Importação da biblioteca:
````
def exibir_evento(request):
    evento = eventos[1]
    template = loader.get_template("agenda/exibir_eventos.html")
    rendered_template = template.render(context={"evento": evento}, request=request)
    return HttpResponse(rendered_template)
````

Utilizando a versão reduzida utilizando o django.shortcuts:

````
from django.shortcuts import render
````

````
def exibir_evento(request):
    evento = eventos[1]
    return render(request=request, context={"evento": evento}, template_name="agenda/exibir_eventos.html")
````

Importante: 
Para que a aplicação seja considerada como instalada, devemos adicionar após a última linha 
do diretório principal do projeto no arquivo settings.py a referências das configurações de 
nossa aplicação.
Ex:
````
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'agenda.apps.AgendaConfig'
]
````

Adicionado validação de exibição no template django:

Ex:
````
<html>
    <h1>Evento: {{evento.nome}}</h1>
    <p>Categoria: {{evento.categoria}}</p>
    {% if evento.local %}<p>Local: {{evento.local}}</p>{% endif %}
    {% if evento.link %}<p>Link: {{evento.link}}</p>{% endif %}
</html>
````

Django ORM:

Exemplod de consulta:
````
Evento.objects.filter(organizador_id=1)
````

Exemplo de Mapeamento de objetos no arquivo models.py:
````
from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=256, unique=True)

class Evento:
    nome = models.CharField(max_length=256)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    local = models.CharField(max_length=256, blank=True)
    link = models.CharField(max_length=256, blank=True)
````

Comando para criar as Migrations:

````
python manage.py makemigrations
````

Comando para aplicar as Migrations:

````
python manage.py migrate
````

Comando para abrir um client para sqlite:

````
python manage.py dbshell
````

Comandos SQlite:

````
.table - Exibe todas as tabelas
.quit - sai do teminal
.header on - Exibe cabeçalhos nas consultas
.nullvalue NULL
````

Abrindo shell interativo com o projeto
````
python manage.py shell
````
Comandos Executados:
````
>from agenda.models import Evento, Categoria

Criando instância e persistência de dados
>Categoria.objects.create(nome="Backend")

Busca todos os elementos de uma classe ou tabela no banco de dados:
>Categoria.objects.all()

Criando uma categoria e armazenando em uma variavel
>cat = Categoria.objects.create(nome="Frontend")

Outra Forma de Criar instância e persistir de dados
>categoria_3 = Categoria(nome="Fullstack")
>categoria_3.save()

Realizando filtro
>Categoria.objects.filter(nome="Backend")

Criando um evento:
>categoria = Categoria.objects.filter(nome="Backend")
>evento = Evento(nome="Aula de APIs", categoria=categoria)
>evento.save()

Navegando entre os objetos
>evento.categoria.nome

Realizando filtro:
Evento.objects.filter(categoria=categoria)
Evento.objects.filter(categoria__nome="Backend") #navegando entre as relações de tabelas

````

Django Admin

Descomentar path admin:
````
urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", include(agenda_urls))
]
````

Comando para criar um super usuário:
````
python manage.py createsuperuser
````

Registrando modelos no painel administrativo do Django:
No diretótio da aplicação devemos alterar o arquivo admin.py
````
from django.contrib import admin

from agenda.models import Evento, Categoria

# Register your models here.
admin.site.register(Evento)
admin.site.register(Categoria)
````

Sobrescrevendo o metódo __str__ para melhorar a visualização:
````
def __str__(models.Model):
    return f"{self.nome} <{self.id}>"
````

Iterando os objetos no Django Template html:
````
{% for evento in eventos %}
    <tr>
        <td>{{evento.nome}}</td>
        <td>{{evento.categoria.nome}}</td>
        <td>{% firstof evento.local evento.link %}</td>
        <td>{{ evento.data }}</td>
        <td><a href="exibir_evento.html">Ver detalhes</a></td>
    </tr>
{% endfor %}
````

Abrindo o Python shell para implentar a solução:
````
(InteractiveConsole)
>>> from agenda.models import Evento
>>> Evento.objects.all()
<QuerySet [<Evento: Aula de APIS <1>>, <Evento: Outro evento <2>>, <Evento: Aula de React <3>>, <Evento: Aula de PHP <4>>]>
>>> evs = Evento.objects.all()
>>> for ev in evs: print(ev.nome)
... 
Aula de APIS 
Outro evento 
Aula de React
Aula de PHP  
>>> evs_futuros = Eventos.objects.filter(data__gte=data_de_hoje)
Traceback (most recent call last):      
  File "<console>", line 1, in <module> 
NameError: name 'Eventos' is not defined
>>> from datetime import date
>>> date.today()   
datetime.date(2022, 3, 9)
>>> evs_futuros = Evento.objects.filter(data__gte=date.today())  
>>> evs_futuros
<QuerySet [<Evento: Outro evento <2>>, <Evento: Aula de React <3>>]>
>>> for ev in evs_futuros:print(ev.nome)
... 
Outro evento
Aula de React
````
Adicionando uma rota eventos, consultando por id:
````
urlpatterns = [
    path("", listar_eventos),
    path("eventos/<int:id>/", exibir_evento)
]
````
Adionando a biblioteca para o tratamento do erro 404:
````
from django.shortcuts import render, get_object_or_404
````

Implementando o metódo da rota exibir eventos:
````
def exibir_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    evento = Evento.objects.get(id=id) #Get() vai tentar buscar apenas um elemento
    return render(
        request=request, 
        context={"evento": evento}, 
        template_name="agenda/exibir_eventos.html"
    )
````

Adcionando um nome para a view:
````
urlpatterns = [
    path("", listar_eventos, name="listar_eventos"),
    path("eventos/<int:id>/", exibir_evento, name="exibir_evento")
]
````

Exemplo de utilização em um template django:
````
<td><a href="{% url 'exibir_evento' evento.id %}">Ver detalhes</a></td>
````

Implementando uma view com HttpResponseRedirect:
Importante a utilização deste recurso para que o cliente não realize uma operação 
indevida ao atualizar a página do navegador.
````
def participar_evento(request):
    evento_id = request.POST.get("evento_id")
    evento = get_object_or_404(Evento, id=evento_id)
    evento.participantes += 1
    evento.save()
    
    return HttpResponseRedirect(f"/eventos/{evento.id}/")
    
    Outra forma de redirecionamento com o reverse:
    from django.urls import reverse
    return HttpResponseRedirect(reverse('exibir_evento', args=(evento_id,)))
````

### Módulo 13 - Escrevendo Testes Automatizados

Adicionar testes há um projeto é escrever um script de validação dos possiveis casos em que os valores das váriaveis podem entrar.

Para criar testes com Unittest:
1) Importar a biblioteca unitest.
2) Criar uma classe que herde de unittest.TestCase
3) Cada teste será uma função da classe
4) Método assertEquals compara se o resultado da sua função é igual o resultado esperado
5) Para executar o teste utilizamos o comando unittest.main()

Padrão adotado: Uma classe para cada método e cada classse pode conter vários cases de testes.

Teste TDD - Simplesmente é criar os testes antes de desenvolver uma funcionalidade.

Link interessante sobre assert: https://docs.python.org/pt-br/3/library/unittest.html#unittest.TestCase.assertEqual

AssertIn:
````
 # assertIn verifica se um elemento está em uma lista.
 ex:  
   self.assertIn(tarefa, lista.get_tarefas())
````

Biblioteca datetime:

Como importar:
````
from datetime import date, datetime

````

Documentação de Time e TimeDelta: https://docs.python.org/pt-br/3/library/datetime.html#examples-of-usage-timedelta

### Django Test

Exemplo:
````
# Importando biblioteca
from django.test import TestCase, Client
    
    class TestPaginaIncial(TestCase):
        def test_lista_eventos(self):
            client = Client()
            response = client.get("/")
            self.assertContains(response, "<th>Nome</th>")
````
Obs: É obrigatório o nome da classe e do método começarem com "Test" e receber o TestCase.

Comando para executar o teste:
````
python manage.py test
````

### Módulo 14 - REST API com Django Rest Framework

Criando um projeto:
````
( ">" significa comandos executados no terminal PowerShell)
1) Criar uma pasta;
2) Criar um ambiente virtual:
> python3 -m venv venv
3) Instalar o Framework Django na versão 4.0.2:
> pip install Django==4.0.2
4) Instalar a bilioteca DjangoRest
> pip install djangorestframework
5) Criar o projeto:
> django-admin startproject tamarcado . # O ponto siginifca criar o projeto na pasta raiz.
6) Criando um app:
> django-admin startapp agenda
7) Definir escopo de rotas da API.
8) Criar os modelos de dados em model.py.
9) Instalar o app criado em INSTALLED_APPS no arquivo settings.py 
10) Criar Migrations:
> python manage.py makemigrations
11) Executar as Migrations:
> python manage.py migrate
12) Criar arquivo urls.py no diretório do app.
13) Incluir urls do app no projeto em "urlpatterns" no arquivo urls.py, importando via include. 
Ex:
from django.conf.urls import include
urlpatterns = [
    path('api/', include('agenda.url'))
]
14) Adicionar rotas em url.py do app:
Ex:
from django.urls import path
urlpatterns = [
    path('agendamentos/', agendamento_list),
    path('agendamentos/<int:id>', agendamento_detail),
]
* Sempre seguir padrão de nomes para as views (list e detail)
15) Criar views:
- importar models e "get_object_or_404" para tratamento de erros.
- importar view no arquivo url.py.
Ex:
def agendamento_detail(request, id):
    obj = get_object_or_404(Agendamento, id=id)
16) Serializar dados:
- Criar um arquivo "serializers.py"
- Importar serializers de rest_framework 
from rest_framework import serializers
- Criar uma classe herdando de Serializer, mapeando os campos:
Ex:
class AgendamentoSerializer(serializers.Serializer):
    data_horario = serializers.DateTimeField()
    nome_cliente = serializers.CharField(max_length=200)
17) Adicionar o objeto serializer na view agendamento_detail:
- Recebe o construtor que consegue realizar o de para de campos, pois são os mesmos nomes criados em models.
Ex:
serializer = AgendamentoSerializer(obj)
18) Para retornar os dados serializados no formato JSON:
- Importar bibioteca JsonResponse:
from django.http import JsonResponse
- Depois basta retornar o método JsonResponse:
return JsonResponse(serializer.data)
19) Rodar aplicação:
> python manage.py runserver
20) Criar superUser e adicionar Models em admin.py.
21) Criar view agendamento_list:
- qs (query settings)
- Utilizando o Serializer podemos realizar serializar um objeto interavel passando o parâmetro many=true e safe=False:
Ex:
def agendamento_list(request):
    qs = Agendamento.objects.all()
    serializer = AgendamentoSerializer(qs, many=True)
    return JsonResponse(serializer.data, safe=False) 
22) Adicionar o decorator api_view para que a api seja consistente e sempre retorne um json:
- Importar:
from rest_framework.decorators import api_view
- Adicionar anotações:
@api_view(http_method_names=["GET"])
23) Criando um Post com Serializer:
- data = request.data # adiciona os dados da requisição
- serializer = AgendamentoSerializer(data=data) # realiza a comparação dos dados
- if serializer.is_valid(): # Faz a validação dos dados comparando a model com serializer validando os tipos dos campos e tamanhos.
- validated_data = serializer.validated_data # caso a resição seja valida adiciona os dados.
- Cria um regitro na base:
Agendamento.objects.create(
    data_horario=validated_data["data_horario"],
    nome_cliente=validated_data["nome_cliente"],
    email_cliente=validated_data["email_cliente"]
    telefone_cliente=validated_data["telefone_cliente"]
)
- Retorna um json do objeto criado com status 201:
return JsonResponse(serializer.data, status=201)
- Caso serializer.is_valid() for igual false retorna um json com erros e com status 400:
return JsonResponse(serializer.errors, status=400)

````












