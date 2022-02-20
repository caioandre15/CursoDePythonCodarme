# Exer. 05 Calcula a média das notas
# Alunos e suas notas representados através de dicionários

alunos = [
    {
        "nome": "Alice",
        "nota": 8
    },
    {
        "nome": "Bob",
        "nota": 7
    },
    {
        "nome": "Carlos",
        "nota": 9
    }
]

soma = 0

for aluno in alunos:
    soma += aluno["nota"]

media = soma / len(alunos)

print("Media dos Alunos: ", media)