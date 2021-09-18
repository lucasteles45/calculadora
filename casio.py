import abc

class Calculadora (object):

    def calcular(self, valor1, valor2, operador):
        operacaoFabrica = OperacaoFabrica()
        operacao = operacaoFabrica.criar(operador)
        if(operacao == None):
            return 0
        else:
            operacao = operacaoFabrica.criar(operador)
            resultado = operacao.executar(valor1, valor2)
            return resultado


class OperacaoFabrica(object):

    def criar(self, operador):
        if(operador == 'soma'):
            return Soma()
        elif(operador == 'subtracao'):
            return Subtracao()
        elif (operador == 'divisao'):
            return Divisao()
        elif (operador == 'multiplicacao'):
            return Multiplicacao()


class Operacao(metaclass=abc.ABCMeta):

    @abc.abstractclassmethod
    def executar(self, valor1, valor2):
        pass



class Soma(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 + valor2
        return resultado


class Subtracao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 - valor2
        return resultado


class Divisao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 / valor2
        return resultado


class Multiplicacao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 * valor2
        return resultado


calculador = Calculadora()
x = calculador.calcular(1,7,'multiplicacao')
print(x)