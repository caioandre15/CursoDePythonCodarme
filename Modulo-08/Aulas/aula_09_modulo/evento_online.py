from evento import Evento
# from nome_arquivo import nome_classe

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