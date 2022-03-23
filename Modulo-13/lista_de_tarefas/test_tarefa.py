import unittest
from tarefa import Tarefa


class TestConcluir(unittest.TestCase):
    def test_concluir_tarefa_altera_concluido_para_true(self):
        tarefa = Tarefa("Estudar Python")
        tarefa.concluir()
        self.assertEqual(tarefa.concluida, True)
    
    def test_concluir_tarefa_concluida_mantem_concluida_como_true(self):
        tarefa = Tarefa("Estudar Python")
        tarefa.concluir()
        self.assertEqual(tarefa.concluida, True)
        tarefa.concluir()
        self.assertEqual(tarefa.concluida, True)

class TestAdicionarDescricao(unittest.TestCase):
    def test_adicionar_descricao_na_tarefa(self):
        tarefa = Tarefa("Estudar Python")
        tarefa.adicionar_descricao("Aulas ao vivo")
        self.assertNotEqual(tarefa.descricao, "")

unittest.main()