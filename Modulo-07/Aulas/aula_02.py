def calcular_conta(consumo, taxa_servico=0.1, desconto_fidelidade=5):
    servico = consumo * taxa_servico
    desconto = consumo * desconto_fidelidade
    valor = (consumo + servico) - desconto
    return valor

valor = calcular_conta(consumo=100, taxa_servico=0.1, desconto_fidelidade=0.05)
print("O valor a ser pago é:", valor)

"""
consumo = 100
servico = consumo * taxa_servico # 10
desconto = consumo * desconto_fidelidade # 5

valor = consumo + servico # 100 + 10 = 110
valor = valor - desconto # 110 - 5

=> 105
"""