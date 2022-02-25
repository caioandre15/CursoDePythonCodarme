# Aula 3 - Definindo Classes

# Classes são estrutura de códigos em que conseguimos definir
# nossos próprios tipos (String, Float ...) e metódos.

d = {"a": 1}  # dicionário é o tipo e "d" é o objeto.
d.keys()

# Estado: representação dos dados que o objeto armazena.
# Comportamento: São os métodos que o objeto pode realizar,

# definindo uma classe

class Evento:
    pass # Informa que é uma classe vazia (pass) ou (...).

ev = Evento() # cria a instancia a classe Evento em memôria.
ev.nome = "Aula de Python"
print(ev.nome)

def altera_nome_evento(evento, novo_nome):
    print("Alterando nome do evento")
    evento.nome = novo_nome

altera_nome_evento(ev, "Aula de JavaScript")
print(ev.nome)









