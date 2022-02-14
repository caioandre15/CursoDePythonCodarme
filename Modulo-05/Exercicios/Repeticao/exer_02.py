# Exer. 02 Números Pares

numeroInteiro = int(input("Digite um número inteiro: "))

i = 1
j = 1  

if numeroInteiro % 2 != 0:
    numeroInteiro -= numeroInteiro % 2
while numeroInteiro % 2 == 0 and numeroInteiro != 0:
    numeroInteiro -= 2
    i += 1

while j != i:
    print(2 * j)
    j += 1

   
