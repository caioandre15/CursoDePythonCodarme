# Exer. 04 Calcula a média das notas

alunos = [
    ("Alice", 8.3),
    ("Bob", 7),
    ("Carlos", 9)
]

soma = 0
for aluno in alunos:
    nome, nota = aluno
    soma += nota

media = soma / len(alunos)
print("Média dos Alunos:", media)
