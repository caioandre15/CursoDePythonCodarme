# Exer. 02 - Calculadora

operandoA = float(input("Digite um número inteiro ou float: "))
operandoB = float(input("Digite um número inteiro ou float: "))
operadorOp = input("Digite o operador: ")

# Soma
if operadorOp == "+":
    print("Resultado: ", operandoA + operandoB) 
# Subtração
elif operadorOp == "-":
    print("Resultado: ", operandoA - operandoB)
# Multiplicação
elif operadorOp == "*":
    print("Resultado: ", operandoA * operandoB)
# Divisão
elif operadorOp == "/" and operandoB != 0:
    print("Resultados: ", operandoA / operandoB)
else: 
    print("Não foi possível realizar divisão por zero!")