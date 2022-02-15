# Curso de Python Codar.Me

## importação de bibliotecas:
```
import os // biblioteca para acessar comandos do sistema operacional.
Ex: os.system('cls') or None // Limpa o prompt de comando.
```

## Resumos dos Módulos  
### Modulo 01

#### 01. Instalação do Python.
Instalar o python versão 3.10.1

#### 02. O que é python

Podemos nos referir a três conceitos:  
1) Linguagem de programação //Código em si  
2) Código-fonte (.py) // Script em python  
3) Interpretador Python  

#### 03. Configurando o VSCode
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

### Módulo 03
Comando:
```
type("Texto") // retorna o tipo da variável.
```

### Módulo 04
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

### Módulo 05
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










