import unittest
from tarefa import Tarefa
from lista_de_tarefas import ListaDeTarefas
from datetime import date, datetime

# Uma classe para cada método e cada classse pode conter vários cases de testes.
class TestAdicionarTarefa(unittest.TestCase):
    def test_adiciona_tarefa_a_lista_de_tarefas(self):
        tarefa = Tarefa("Tarefa Teste")
        lista = ListaDeTarefas()

        lista.adicionar_tarefa(tarefa)

        # self.assertEqual(lista.get_tarefas()[0], tarefa)
        # assertIn verifica se um elemento está em uma lista.
        self.assertIn(tarefa, lista.get_tarefas())


class TestGetTarefas(unittest.TestCase):
    def test_retorna_lista_de_tarefas_nao_concluidas(self):
        tarefa_um = Tarefa("Tarefa Teste1")
        tarefa_dois = Tarefa("Tarefa Teste2")
        tarefa_dois.concluir()
        lista = ListaDeTarefas()

        lista.adicionar_tarefa(tarefa_um)
        lista.adicionar_tarefa(tarefa_dois)

        self.assertEqual(lista.get_tarefas(), [
            tarefa_um,
        ])
    
    def test_retorna_lista_de_tarefas_adicionadas(self):
        tarefa_um = Tarefa("Tarefa Teste1")
        tarefa_dois = Tarefa("Tarefa Teste2")
        tarefa_dois.concluir()
        lista = ListaDeTarefas()

        lista.adicionar_tarefa(tarefa_um)
        lista.adicionar_tarefa(tarefa_dois)

        self.assertEqual(lista.get_tarefas(incluir_concluidas=True), [
            tarefa_um,
            tarefa_dois,
        ])

class TestGetTarefasAtrasadas(unittest.TestCase):
    def test_retorna_lista_de_tarefas_atrasadas(self):
        dt_notificao_um = datetime(2022, 3, 10, 9, 10)
        dt_notificao_dois = datetime(2022, 5, 10, 9, 10)
        tarefa_um = Tarefa("Tarefa Teste1", data_notificacao=dt_notificao_um)
        tarefa_dois = Tarefa("Tarefa Teste2", data_notificacao=dt_notificao_dois)
        lista = ListaDeTarefas()

        lista.adicionar_tarefa(tarefa_um)
        lista.adicionar_tarefa(tarefa_dois)

        self.assertEqual(lista.get_tarefas_atrasadas(), [
            tarefa_um
        ])

class TestGetTarefasParaHoje(unittest.TestCase):
    def test_retorna_lista_de_tarefas_para_hoje(self):
        dt_notificao_um = datetime.now()
        dt_notificao_dois = datetime(2022, 5, 10, 9, 10)
        tarefa_um = Tarefa("Tarefa Teste1", data_notificacao=dt_notificao_um)
        tarefa_dois = Tarefa("Tarefa Teste2", data_notificacao=dt_notificao_dois)
        lista = ListaDeTarefas()

        lista.adicionar_tarefa(tarefa_um)
        lista.adicionar_tarefa(tarefa_dois)

        self.assertEqual(lista.get_tarefas_para_hoje(), [
            tarefa_um
        ])

unittest.main()