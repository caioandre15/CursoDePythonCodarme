# Aula 04 - Construtores

class Evento:
    def __init__(self, nome):
        self.nome = nome
        self.local = "Brasil"

    def altera_nome_evento(self, novo_nome):
        print("Alterando nome do evento")
        self.nome = novo_nome

# ev = Evento() # ... Evento.__init__(...) Dará um erro por causa do contrutor esperar o atributo nome

ev = Evento("Aula de Python")
ev2 = Evento("Aula de JavaScript")

print(ev.nome)
print(ev.local)
print(ev2.nome)
print(ev2.local)