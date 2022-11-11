from calendario import Calendario

class Lista(object):

    def __init__(self) -> None:
        self.gerenciador = []

    def buscar_atividade(self, calendario:Calendario)->bool:
        for cal in self.gerenciador:
            if calendario == cal:
                return True
        return False

    def adicionar_atividade(self, materia:str, atividade:str, data_de_entrega:str)->bool:
        
        calendario = Calendario(materia, atividade, data_de_entrega)

        if self.buscar_atividade(calendario) == False:
                self.gerenciador.append(calendario)
                return True
        return False

    def remover_atividade(self, data_de_entrega:str)->bool:
        for cal in self.gerenciador:
            if cal.data_de_entrega == data_de_entrega:
                self.gerenciador.remove(cal)
                return True
        return False

    def listar_atividades(self,)->str:
        for cal in self.gerenciador:
            cal.__repr__()