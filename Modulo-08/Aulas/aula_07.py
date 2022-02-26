# Aula 07

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
    
    @classmethod
    def cria_evento_online(cls, nome):
        evento = cls(nome, local=f"https://tamarcado.com/eventos?id={cls.id}")
        return evento
    
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

ev_online = Evento.cria_evento_online("Live de Python")
ev2_online = Evento.cria_evento_online("Live de JavaScript")

ev_online.imprime_informacoes()
ev2_online.imprime_informacoes()

print(ev2_online.id)
print(Evento.id)

# Cando consultamos um atributo de uma instância quaso não exista este atributo no objeto
# Será consultado na classe, portanto os objetos tem acesso aos atributos da classe.
