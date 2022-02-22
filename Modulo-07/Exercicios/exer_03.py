# Exer. 03 - Imprime Maior de idade ou não

tupla = ("Jhony", 17)

def maior_idade(tupla):
    nome, idade = tupla
    if (idade >= 18):
        print("Maior de idade.")
    else:
        print("Menor de idade")

maior_idade(tupla)