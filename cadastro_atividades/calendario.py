class Calendario(object):

    def __init__(self, materia: str, atividade: str, data_de_entrega: int) -> None:
        self.materia = materia
        self.atividade = atividade
        self.data_de_entrega = data_de_entrega

    def set_materia(self, nova_materia:str) ->None:
        self.materia = nova_materia
    
    def get_materia(self) -> str:
        return self.materia

    def set_atividade(self, nova_atividade:str) ->None:
        self.atividade = nova_atividade

    def get_atividade(self) -> str:
        return self.atividade

    def set_data_de_entrega(self, nova_data_de_entrega:str) ->None:
        self.data_de_entrega = nova_data_de_entrega

    def get_data_de_entrega(self) -> str:
        return self.data_de_entrega

    def __repr__(self) -> str:

        print("Matéria:", self.materia)
        print("Atividade:", self.atividade)
        print("Data de entrega:", self.data_de_entrega)
        print("--------------------------------")