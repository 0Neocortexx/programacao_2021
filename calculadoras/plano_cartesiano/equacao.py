from fatores import Fatores
from math import sqrt

class Equacao(object):

    def __init__(self) -> None:
        self.fat = Fatores

    # Medir Distância

    def distancia(self, x1: float, y1: float, x2: float, y2: float) -> None:
        dist = sqrt((x1 - x2)**2(y1 - y2)**2)
        return dist

    def __eq__(self, x1, x2, y1, y2) -> bool:
        return x1 == x2 == y1 == y2

if __name__ == "__main__":
    app = Equacao()
    app.distancia(12.5, 15.2, 12.5, 15.2)