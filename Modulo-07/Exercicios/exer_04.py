# Exer. 04 - Adaptação da função Maior de idade

tupla = ("Jhony", 17)
dicionario = {"Jhony": 18}

def teste_maior_idade(idade):
    if (idade >= 18):
        print("Maior de idade.")
    else:
        print("Menor de idade")

def maior_idade(tupla_ou_Dicionario):
    
    if (isinstance(tupla_ou_Dicionario, tuple)):
        nome, idade = tupla_ou_Dicionario
        teste_maior_idade(idade)
    else:
        for pessoa, idade in tupla_ou_Dicionario.items():
            teste_maior_idade(idade)

maior_idade(tupla)