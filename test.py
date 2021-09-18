import unittest 
import casio 

class Teste(unittest.TestCase):
    def test_soma(self):
        calculador = casio.Calculadora()
        result = calculador.calcular(4, 7, 'soma')
        self.assertEqual(result, 11)

    def test_multiplicacao(self):
        calculador = casio.Calculadora()
        result = calculador.calcular(6, 9, 'multiplicacao')
        self.assertEqual(result, 54)

    def test_Divisao(self):
        calculador = casio.Calculadora()
        result = calculador.calcular(16, 4, 'divisao')
        self.assertEqual(result, 4)

    def test_subtracao(self):
        calculador = casio.Calculadora()
        result = calculador.calcular(9, 8, 'subtracao')
        self.assertEqual(result, 1)

    def test_raiz_quadrada(self):
        calculador = casio.Calculadora()
        result = calculador.calcular(8, 2, 'raiz_quadrada')
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()