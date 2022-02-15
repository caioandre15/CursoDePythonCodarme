listaVazia = [] # Lista vázia
notas = [8, 10, 8.8] # Lista com dados preenchidos
#          0   1   2 
print(notas[0]) # Exibe o indice zero. 

notas.append(9) # Adiona um valor/objeto ao final da lista
print(notas[3]) # Exibe o indice 03 para verificar se foi adicionado o valor.

print(notas) # Lista antes de ordenar
notas.sort() # Ordena os valores da lista (Crescente)
print(notas) # Lista depois de ordenar

print(notas) # Lista antes de ordenar
notas.sort(reverse=True) # Ordena os valores da lista (Decrescente)
print(notas) # Lista depois de ordenar

notas.pop() # Remove por padão o último elemento da lista
print(notas)

notas.insert(0, 8) # Insere um valor/objeto no indice indicado da lista
print(notas)

notas.pop(0) # Remove o valor/objeto do indíce 0
print(notas)



