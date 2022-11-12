class endereço:
    
    def __init__(self, bairro: str ,casa: int, rua: str) -> None:

        self.bairro = input("Digite o nome do seu bairro: ") 
        self.rua = input("Digite sua rua: ")
        self.casa = input("Digite o numero da sua casa: ")
        
        self.numero = None
        self.rua_casa = None
        self.local = None

    def rua(self, rua: str, seu_endereço: str, casa:int, bairro: str)-> None:

        self.local = bairro_casa
        print(bairro_casa)
        self.rua_casa = seu_endereço
        print(seu_endereço)
        self.numero = numero_casa
        print(numero_casa)
        
# QUESTÃO DOIS ACIMA ---- QUESTAO TRÊS ABAIXO 
# QUESTÃO DOIS ACIMA ---- QUESTAO TRÊS ABAIXO

class Pessoa:
    
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome

final = endereço("Aleatorio","aleatorio" , "aleatorio")

usuário = Pessoa(input("Digite seu nome: ")) 

print("Meu nome é",usuário,"resido na rua",final.rua,
      "numero",final.casa,"bairro", final.bairro,"! :D" )