from lista import Apartamento, Casa
from gerenciadordevenda import Informacoes

class IntGrafica(object):

    def __init__(self) ->None:
        self.home = ()

    def adicionar(self) -> Casa:
        idlocal = input("Digite o ID da residência: ")
        vendedor = input("Digite o nome do vendedor: ") 
        dimensoes = input("Digite as dimensões: ") 
        valor = input("Digite o valor da residência: ") 
        localizacao = input("Digite a localização: ") 
        valorcondominio = input("Digite o valor do condominio (Caso não houver digite 0): ")
        if self.home.adicionar(idlocal, vendedor, dimensoes, valor, localizacao, valorcondominio):
            print("Local cadastrado com sucesso!!")
        else:
            print("Local já existente!")
        
    def remover_local(self) -> None:
        idlocal = input("Digite o ID da residência: ")
        self.home.remover_local(idlocal)

    def listar(self) -> None:
        listas = self.home.listar()
        for lista in listas:
            print("--------------------")
            print("Título: ", lista.titulo)
        print("fim da lista de residências")

    def imprimir_menu(self) -> None:
        print("-------------------Menu-------------------")
        print("|        1- Cadastrar nova residência     |")
        print("|        2- Remover Local                 |")
        print("|        3- Listar                        |")
        print("|        4- Sair                          |")
        print("------------------------------------------")

    def main(self):
        sair = False
        while not sair:
            self.imprimir_menu()
            opcao = int(input("O que você deseja fazer: "))
            if opcao == 1:
                self.adicionar()
            elif opcao == 2:
                self.remover_titulo()
            elif opcao == 3:
                self.listar()
            elif opcao == 4:
                sair = True
            else:
                print("Opção inválida!")

if __name__ == "__main__":
    app = IntGrafica()
    app.main()
