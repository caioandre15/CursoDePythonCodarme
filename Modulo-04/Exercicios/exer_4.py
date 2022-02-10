# Exer. 4

valorDeCompra = float(input("Digite o Valor da compra: "))
valorDoFrete = float(input("Digite o Valor do frete: "))
cadastroProgramaFidelidade = input("Digite (s) para sim ou (n) para não: ")
cadastroProgramaFidelidade = cadastroProgramaFidelidade == "s" if True else False

cupomValido = (valorDeCompra + valorDoFrete > 100.0) or cadastroProgramaFidelidade

print("O cupom pode ser utilizado ", cupomValido)