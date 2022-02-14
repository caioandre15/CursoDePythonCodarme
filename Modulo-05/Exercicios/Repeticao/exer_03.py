# Número Primo

numeroInteiro = int(input("Digite um número inteiro: "))

if numeroInteiro % 1 == 0 and numeroInteiro % numeroInteiro == 0 and numeroInteiro != 1:
    print(f"O número {numeroInteiro} é primo.")
else:
    print(f"O número {numeroInteiro} não é primo.")