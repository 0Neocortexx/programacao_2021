from gerenciador_de_estoque import Gerenciador

class IntGrafica(object):
    def __init__(self) -> None:
        self.acao = Gerenciador()

    def cadastrar(self) -> None:
        nome = input("Digite o nome do produto: ") 
        codigo = input("Digite o código do produto: ") 
        valor = input("Digite o valor: ") 
        quantidade = input("Digite a quantidade de produtos: ") 

        if self.acao.cadastrar(nome, codigo, valor, quantidade):
            print("Produto adicionado !!")
        else:
            print("Produto já existente!")
    
    def remover(self) -> None:
        nome = input("Digite nome do produto: ")
        if self.acao.remover(nome):
            print("Produto removido !!")
        else:
            print("Produto não encontrado!")

    def listar(self) -> None:
        for i in self.acao:
            print(i.nome, i.codigo, i.valor, i.quantidade)

    def imprimir_menu(self) -> None:
        print("Digite 1 Para cadastrar um novo produto!")
        print("Digite 2 para remover um produto!")
        print("Digite 3 para listar os produtos!")
        print("Digite 4 para finalizar!")

    def main(self):
        sair = False
        while not sair:
            self.imprimir_menu()
            opcao = int(input("O que você deseja fazer: "))
            if opcao == 1:
                self.cadastrar()
            elif opcao == 2:
                self.remover()
            elif opcao == 3:
                self.listar()
            elif opcao == 4:
                sair = True
            else:
                print("Opção inválida!")

if __name__ == "__main__":
    app = IntGrafica()
    app.main()