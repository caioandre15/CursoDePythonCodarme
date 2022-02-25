class Evento:
    def metodo_intancia(self):
        return ("método de instância chamado", self)
    
    @classmethod
    def metodo_classe(cls):
        return ("método de classe chamado", cls)
    
    @staticmethod
    def metodo_estatico():
        return "estático chamado"

ev = Evento()
a = ev.metodo_intancia() # Evento.metodo_instancia(ev)
print(a)

b = Evento.metodo_classe() # Evento.metodo_classe(Evento)
print(b)

c = Evento.metodo_estatico() # Evento.metodo_estatico()
print(c)

# É possivel acessar os métods de classe e estáticos a partir do objeto
print(ev.metodo_classe())
print(ev.metodo_estatico())