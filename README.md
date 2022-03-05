# Curso de Python Codar.Me

## Importação de bibliotecas:
```
import os // biblioteca para acessar comandos do sistema operacional.
Ex: os.system('cls') or None // Limpa o prompt de comando.
import json // Para trabalhar com o formto JSON

```

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
Os dois comandos acima são realizados para verificarmos aonde está instaldo o nosso interpretador python.

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



























