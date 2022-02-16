# Curso de Python Codar.Me

## Importação de bibliotecas:
```
import os // biblioteca para acessar comandos do sistema operacional.
Ex: os.system('cls') or None // Limpa o prompt de comando.
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
```











