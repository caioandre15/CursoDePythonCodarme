# OPERADORES LÓGICOS
# NOT
# AND
# OR

# NOT
idade = 16
maior_de_idade = idade >= 18
menor_de_idade = not maior_de_idade

print("Idade da pessoa:", idade)
print("Maior de idade:", maior_de_idade)
print("Menor de idade:", menor_de_idade)

# AND
usuario_correto = True
senha_correto = True
sucesso = usuario_correto and senha_correto
print("Login bem sucedido:", sucesso)

# OR
idade = 14
idade_minima = 16
acompanhada_pelos_pais = False

pode_assistir = idade >= idade_minima or acompanhada_pelos_pais
print("Pode assistir ao filme:", pode_assistir)

