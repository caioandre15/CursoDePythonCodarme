from django.test import TestCase, Client

class TestPaginaIncial(TestCase):
    def test_lista_eventos(self):
        client = Client()
        response = client.get("/")
        # print(response.content)
        # self.assertContains(response, "<th>Nome</th>")
        self.assertTemplateUsed(response, "agenda/listar_eventos.html")
        


