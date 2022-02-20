# Exer. 06 Imprime o maior número da lista

lista = [1, 2, 3, 4, 5, 54, 10000, 3]

maiorNumero = lista[0]
for valor in lista:
    if valor > maiorNumero:
        maiorNumero = valor

print(maiorNumero)