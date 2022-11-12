class Torneira(object):

    def __init__(self, nome: str, entrada: bool,
                 vazao: float) -> None:
        self.nome = nome
        self.entrada = entrada
        self.vazao = vazao
        self.aberta = False 

    def abrir(self) -> None:
        self.aberta = True

    def fechar(self) -> None:
        self.aberta = False

class Tanque:

    def __init__(self, base: float, altura: float,
                 profundidade: float) -> None:
        self.base = base
        self.altura = altura
        self.profundidade = profundidade
        self.volume_max = base * altura * profundidade
        self.volume = 0
        self.torneiras =  []
    
    def adiconar_torneira(self, nome: str, vazao: float,
                          entrada: bool) -> None:
        torneira = Torneira(nome, entrada, vazao)
        self.torneiras.append(torneira)

    def remover_torneira(self, nome) -> None:
        for t in self.torneiras:
            if t.nome == nome:
                self.torneiras.remove(t)

    def encher(self) -> None:
        self.volume = self.volume_max

    def esvaziar(self) -> None:
        self.volume = 0

if __name__ == "__main__":
    tanq1 = Tanque(10, 10, 10)
    tanq1.adiconar_torneira("e1", 1, True)
    tanq1.adiconar_torneira("e2", 1, True)
    tanq1.adiconar_torneira("s1", 1, False)
    tanq1.adiconar_torneira("s2", 1, False)
    for t in tanq1.torneiras:
        print("Nome: ", t.nome, "Vazão: ", t.vazao, "Entrada: ", t.entrada)
    print("----------------Fim---------------")
    tanq1.remover_torneira("e2")
    tanq1.remover_torneira("e1")
    for t in tanq1.torneiras:
        print("Nome: ", t.nome, "Vazão: ", t.vazao, "Entrada: ", t.entrada)
    print("----------------Fim---------------")
    print("Volume de água no tanque: ", tanq1.volume)
    tanq1.encher()
    print("Volume de água no tanque: ", tanq1.volume)
    tanq1.esvaziar()
    print("Volume de água no tanque: ", tanq1.volume)