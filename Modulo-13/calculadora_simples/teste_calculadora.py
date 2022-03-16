from calculadora import somar, dividir, multiplicar, subtrair
import unittest


# Para criar testes
# Importar a biblioteca unitest.
# Criar uma classe que herde de unittest.TestCase
# Cada teste será uma função da classe
# Para executar o teste utilizamos o comando unittest.main()

class TesteSomar(unittest.TestCase):
    def test_soma_de_dois_numeros_inteiros(self):
        soma = somar(2, 4)
        self.assertEqual(soma, 6)
    
    def test_soma_de_numero_com_zero(self):
        soma = somar(2,0)
        self.assertEqual(soma, 2)
    
class TesteDividir(unittest.TestCase):
    def test_divide_numero_por_1_retorna_o_numero(self):
        dividi = dividir(4, 2)
        self.assertEqual(dividi, 2)
    
    def test_divide_por_zero_(self):
        dividi = dividir(10, 0)
        self.assertEqual(dividi, "Não é um número")

class TesteMultiplicar(unittest.TestCase):
    def test_multiplicacao_de_dois_numeros_inteiros(self):
        multiplica = multiplicar(2, 2)
        self.assertEqual(multiplica, 4)
    
    def test_multiplicacao_ordem_dos_fatores(self):
        multiplica1 = multiplicar(2, 3)
        multiplica2 = multiplicar(3, 2)
        self.assertEqual(multiplica1, multiplica2)
    
    def test_multiplicacao_por_um(self):
        multiplica = multiplicar(3, 1)
        self.assertEqual(multiplica, 3)

class TesteSubtrair(unittest.TestCase):
    def test_subtracao_entre_dois_numeros(self):
        subtrai = subtrair(10, 5)
        self.assertEqual(subtrai, 5)
    
    def test_subtracao_entre_numeros_negativos(self):
        subtrai = subtrair(-5, -8)
        self.assertEqual(subtrai, 3)

        

unittest.main()



   