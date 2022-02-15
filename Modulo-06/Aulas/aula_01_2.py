from operator import indexOf


notas = [8, 9, 10, 7.5, 4]

i = 0
total = 0
while i < len(notas):
    total = total + notas[i]
    i += 1

print("O total das notas é:", total)

media = total / len(notas)
print("A média das notas é: ", media)