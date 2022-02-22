# Exer. 02 - Retorna Tupla

list = [1, 2, 3, 4, 5, 8, 10, 30]

def retorna_tupla(list):
    pos = len(list) - 1
    num = list[pos]
    return (pos, num)

print(retorna_tupla(list))