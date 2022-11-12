from JE_atividade_questao_2_parte_1 import Torneira

class Tanque(object):
    
    def __init__(self, altura: float, largura: float, profundidade: float) -> None:
        self.altura = altura
        self.largura = largura
        self.profundidade = profundidade
        self.volume = 0
        self.volume_max = altura * largura * profundidade
        self.torneiras = []

    def encher_tanque(self) -> None:
        self.volume = self.volume_max

    def esvaziar_tanque(self) -> None:
        self.volume = 0

    def adiconar_torneira(self, nome: str, entrada: bool) -> None:
        torneira = Torneira(nome, entrada)
        self.torneiras.append(torneira)
    
    def remover_torneira(self, nome) -> None:
        for tor in self.torneiras:
            if tor.nome == nome:
                self.torneiras.remove(tor)


if __name__ == "__main__":
    valor_tanque =  Tanque(5,10,15)
    valor_tanque.adiconar_torneira("Tanque 1",False)
    valor_tanque.adiconar_torneira("Tanque 2",True)
    valor_tanque.adiconar_torneira("Tanque 3",False)
    valor_tanque.adiconar_torneira("Tanque 4",True)

    for tor in valor_tanque.torneiras:
        print("Nome: ", tor.nome, "Entrada: ", tor.entrada)
    print("--------------------------------------------------------------------------------------------")

    valor_tanque.remover_torneira("Tanque 1")
    valor_tanque.remover_torneira("Tanque 3")
    valor_tanque.remover_torneira("Tanque 4")

    for tor in valor_tanque.torneiras:
        print("Nome: ", tor.nome,"Entrada: ", tor.entrada)
    print("--------------------------------------------------------------------------------------------")

    print("Volume de água no tanque: ", valor_tanque.volume)

    valor_tanque.encher_tanque()

    print("Volume de água no tanque: ", valor_tanque.volume)

    valor_tanque.esvaziar_tanque()
    
    print("Volume de água no tanque: ", valor_tanque.volume)
