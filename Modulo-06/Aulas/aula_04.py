# {key: value}

pessoa = {
    "nome": "Alice",
    "idade": 27,
    "admin": False
}

print(pessoa["nome"])

pessoa_2 = {
    "nome": "Alice",
    "endereco": {
        "rua": "25 de Março",
        "número": 278
    }
}
print(pessoa_2["nome"])
print(pessoa_2["endereco"])
print(pessoa_2["endereco"]["rua"])