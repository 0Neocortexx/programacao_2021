class Fatores(object):

    def __init__(self, x1: float, y1: float, x2: float, y2: float) -> None:
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_x1(self) -> float:
        return self.x1

    def set_x1(self, novo_x1: float) -> None:
        self.x1 = novo_x1

    def get_y1(self) -> float:
        return self.y1

    def set_y1(self, novo_y1: float) -> None:
        self.y1 = novo_y1
    
    def get_x2(self) -> float: 
        return self.x2

    def set_x2(self, novo_x2: float) -> None:
        self.x2 = novo_x2
    
    def get_y2(self) -> float: 
        return self.y2

    def set_y2(self, novo_y2: float) -> None:
        self.y2 = novo_y2