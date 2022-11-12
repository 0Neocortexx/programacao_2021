from typing import get_args


class Calculadora:

    def __init__(self):
        self.ultimo_resutado = None

    def somar(self, a: int, b: int) -> int:
        self.ultimo_resultado = a + b
        return self.ultimo_resultado

    def somar_n(self, *arg:) -> int:
        print(arg)
        self.ultimo_resultado = 0
        for numero in arg:
            self.ultimo_resultado += numero
            return self.ultimo_resultado

calculadora =  Calculadora()

print(calculadora.somar(1, 9))