total = 0
continuar = "s"
while continuar == "s":
    valor = float(input("Digite o valor da compra: \n")) # "123.10" - 123.1
    total = total + valor

    continuar = input("Deseja continuar? (s/n)")

print("O valor total da compra é: ", total)
