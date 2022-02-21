# Exer 07 Exibe quantas cada letra aparece na palavra

palavra = input("Digite uma palavra: ")
dicionarioDeLetras = {}
letraAdicionada = False
for letra in palavra:
    if dicionarioDeLetras.get(letra) == None:
       dicionarioDeLetras[letra] = 1
    else:
        count = dicionarioDeLetras[letra] + 1
        dicionarioDeLetras.update({letra: count})

print(dicionarioDeLetras) 

# Versão 1
# palavra = input("Digite uma palavra: ")
# dicionarioDeLetras = {}
# letraAdicionada = False
# for letra in palavra:
#     for item in dicionarioDeLetras:
#         if item == letra:
#            letraAdicionada = True
#            break
#     if letraAdicionada == False:
#        dicionarioDeLetras[letra] = 1
#     else:
#         count = dicionarioDeLetras[letra] + 1
#         dicionarioDeLetras.update({letra: count})

# print(dicionarioDeLetras) 
      
