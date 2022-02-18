# Exer. 03 Cacula Média de uma Lista

lista = [1, 10, 20, 35, 22, 12]

soma = 0
for item in lista:
    soma += item

media = soma // len(lista)

print("Resultado:", media)
