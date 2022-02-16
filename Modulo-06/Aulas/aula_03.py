# Conjuntos - Set

usuarios = {"alice", "bob"}
usuarios_2 = set(["alice","bob"]) # Criando conjunto com o Método SET

print("Comparando as duas maneiras de criação:")
print(usuarios == usuarios_2) # Comparando as duas maneiras de criação

# Conjuntos não são ordenados
# Conjuntos não permitem valores repetidos.
print(usuarios)
usuarios.add("bob")
print(usuarios) # bob não será acrescentado, pois já existe no conjunto

# Como não permitem duplicados podemos utilizar esta restrição para criar um conjunto
# a partir de um lista com elementos duplicados. Assim conseguimos remover dados duplicados de uma lista.

print("Removendo duplicados:")
usuarios_3 = ["alice", "bob", "alice"]
print(usuarios_3)
usuarios_unicos = set(usuarios_3)
print(usuarios_unicos)

# União
print("Unindo conjuntos:")
usuarios_4 = {"alice", "bob", "pedro"}
print(usuarios_4)
usuarios_5 = set(["alice", "jamau", "jose"])
print(usuarios_5)

print(usuarios_4.union(usuarios_5))

# Existem duas maneiras de realizar a união
print("Comparando union e |:")
e_igual = usuarios_4.union(usuarios_5) == usuarios_4 | usuarios_5
print(e_igual)

# Interseção
print("Intersecção conjuntos:")
usuarios_4 = {"alice", "bob", "pedro"}
print(usuarios_4)
usuarios_5 = set(["alice", "jamau", "jose"])
print(usuarios_5)

print(usuarios_4.intersection(usuarios_5))

# Existem duas maneiras de realizar a união
print("Comparando intersection e &:")
e_igual = usuarios_4.intersection(usuarios_5) == usuarios_4 & usuarios_5
print(e_igual)

# Diferença
print("Diferença conjuntos:")
usuarios_4 = {"alice", "bob", "pedro"}
print(usuarios_4)
usuarios_5 = set(["alice", "jamau", "jose"])
print(usuarios_5)

print(usuarios_4.difference(usuarios_5))

# Existem duas maneiras de realizar a união
print("Comparando difference e -:")
e_igual = usuarios_4.difference(usuarios_5) == usuarios_4 - usuarios_5
print(e_igual)

