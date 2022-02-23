# Exer. 05 - Procura um elemento

lista = [1, 2, 3]

elemento = 3

def func(lista, elemento):
    count = 0
    elementoEncontrado = False
    while (count < len(lista)):
        if (lista[count] == elemento):
            elementoEncontrado = True
        count += 1
    return elementoEncontrado    
    

print(func(lista, elemento))