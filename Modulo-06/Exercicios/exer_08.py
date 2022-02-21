# Exer 08 - Imprime uma lista invertida

def inverte_lista(lista):
    nova_lista = []
    for item in range(len(lista) - 1, -1, -1):
        nova_lista.append(lista[item])
    return nova_lista

lista = ["a", 5, {1}]
lista_invertida = inverte_lista(lista)
print(lista_invertida)
