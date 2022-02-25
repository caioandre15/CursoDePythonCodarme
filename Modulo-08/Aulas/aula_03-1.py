class Evento:
    def altera_nome_evento(self, novo_nome):
        print("Alterando nome do evento")
        self.nome = novo_nome

ev = Evento() # cria a instancia a classe Evento em memôria.
ev.nome = "Aula de Python"
print(ev.nome)

ev.altera_nome_evento("Aula de JavaScript")
# Evento.altera_nome_evento(ev,ev, "...")
print(ev.nome)

# obj.metodo(1, 2, 3) => Evento.metodo(obj, 1, 2, 3)









