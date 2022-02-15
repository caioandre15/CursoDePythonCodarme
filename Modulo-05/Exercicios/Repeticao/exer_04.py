import os

# Exer. 04 - O Jogo

numero = 8

resp = "s"
while resp == "s":
    os.system('cls') or None
    print("### Jogo de adivinhação - Acerte o Número ###")
    print("Em qual número inteiro estou pensando?...")
    i = 1
    while i <= 3:
        tentativa = int(input(f"Tentativa número {i}: "))
        if tentativa > numero:
            print("O número digitado é maior do que o número secreto.")
            i += 1
        elif tentativa < numero:
            print("O número digitado é menor do que o número secreto.")
            i += 1
        elif tentativa == numero:
            print("Você acertou o número secreto, parabéns!!")
            break
    resp = input("Deseja jogar novamente? (s) sim (n) não: ")
