import math

class CalcularRaiz(object):

    def __init__(self, a: float, b: float, c: float):
      
        self.a = a
        self.b = b
        self.c = c
        self.delta = int(self.b ** 2 - 4 * self.a * self.c)      

    def realizar_operacao(self) -> float:
        if self.delta < 0:

            print("Valor de delta negativo, raiz impossivel de ser extraida com numeros reais")
            return

        elif self.delta >= 0:

            rd = math.sqrt(self.delta)

            x1 = ( - self.b + (rd)) / (2 * self.a)
            x2 = ( - self.b - (rd)) / (2 * self.a)

            print("O valor de x1 é:", x1)
            print("O valor de x2 é:", x2)

            return

operacao = CalcularRaiz(2,12,-14)
operacao.realizar_operacao()