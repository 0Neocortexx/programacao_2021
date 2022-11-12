class Carro:

    def __init__(self, marca: str, nome: str,ano: int) -> None:
        self.nome = nome
        self.marca = marca
        self.ano = ano
        self.direcao = None
        self.cor = None

    def tingimento(self,cor: str) -> None:
        if cor in ["Cinza", "Preto", "Azul", "Roxo"]:
            self.colorido = cor
            print("A cor deste carro é",cor)
        else:
            print("Esta cor não está disponivel!!")

    def acelerar(self , nova_direcao: str) -> None:
        if nova_direcao in ["Ré","Frente"]:
            self.direcao= nova_direcao
            print(nova_direcao)
        else:
            print("Esta direção está incorreta")

chevette = Carro ("Chevrolet", "Chevette", 1981)
 #Exemplo Errado