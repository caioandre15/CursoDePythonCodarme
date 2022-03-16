from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return f"{self.nome} <{self.id}>"

class Evento(models.Model):
    nome = models.CharField(max_length=256)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    local = models.CharField(max_length=256, blank=True)
    link = models.CharField(max_length=256, blank=True)
    data = models.DateField(null=True)
    participantes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nome} <{self.id}>"
    
    @classmethod
    def criar_evento(cls, nome, categoria, local, link, data, participantes):
        cls.nome = nome
        cls.categoria = categoria
        cls.link = link
        cls.data = data
        cls.participantes = participantes
        if (local and link == "") or (local == "" and link):
            Evento(cls)
        else:
            raise ValueError("Evento não pode possuir local e link.")
        return Evento(cls)

        


