from django.test import TestCase, Client
from agenda.models import Evento, Categoria
from datetime import date

class TestPaginaIncial(TestCase):
    def test_lista_eventos(self):
        client = Client()
        response = client.get("/")
        # print(response.content)
        # self.assertContains(response, "<th>Nome</th>")
        self.assertTemplateUsed(response, "agenda/listar_eventos.html")

class TestListagemDeEventos(TestCase):
    def test_evento_com_data_de_hoje_e_exibido(self):
        # Criando Categoria
        categoria = Categoria()
        categoria.name = "Backend"
        categoria.save()
        # Criando Evento
        evento = Evento()
        evento.nome = "Aula de Python"
        evento.categoria = categoria
        evento.local = "Rio de Janeiro"
        evento.data = date.today()
        evento.save()

        client = Client()
        response = client.get("/")
        self.assertContains(response, "Aula de Python")
        self.assertEqual(response.context["eventos"][0], evento)
        self.assertEqual(list(response.context["eventos"]), [evento])




