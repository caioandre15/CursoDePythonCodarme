# Aula 08

class Evento:
    id = 1 # Adicionando atributos de classe

    def __init__(self, nome, local=""):
        self.nome = nome
        self.local = local
        self.id = Evento.id
        Evento.id += 1
    
    def imprime_informacoes(self):
        print("Id do evento:", self.id)
        print("Nome do evento:", self.nome)
        print("Local do evento:", self.local)
        print("--------------------")
    
    @staticmethod
    def calcula_limite_pessoas_area(area):
        if 5 <= area < 10:
            return 5
        elif 10 <= area < 20:
            return 15
        elif area >= 20:
            return 30
        else:
            return 0

# Herança - Evento online é uma especialização da classe Evento
class EventoOnline(Evento):
    def __init__(self, nome, _=""):
        local = f"https://tamarcado.com/eventos?id={EventoOnline.id}"
        # Forma explicita:
        # Evento.__init__(self, nome, local)
        # Forma implicita
        super().__init__(nome, local)

    def imprime_informacoes(self):
        print("Id do evento:", self.id)
        print("Nome do evento:", self.nome)
        print("Link para acessar o evento:", self.local)
        print("--------------------")


ev_online = EventoOnline("Live de Python")
ev2_online = EventoOnline("Live de JavaScript")

ev_online.imprime_informacoes()
ev2_online.imprime_informacoes()

ev = Evento("Aula de Python", "Rio de Janeiro")
ev.imprime_informacoes()

