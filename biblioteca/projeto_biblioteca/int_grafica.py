from biblioteca import Biblioteca

class IntGrafica(object):

    def __init__(self) ->None:
        self.bib = Biblioteca()

    def adicionar(self) -> None:
        fisico = input("Digite o tipo: ")
        if fisico == "fisico":
            fisico = True
        else:
            fisico = False 
        autor = input("Digite o nome do autor: ") 
        assunto = input("Digite o assunto: ") 
        resumo = input("Digite o resumo: ") 
        isbn = input("Digite o isbn: ") 
        titulo = input("Digite o titulo: ")
        if self.bib.adicionar(fisico, autor, assunto, resumo, isbn, titulo):
            print("Livro cadastrado com sucesso!!")
        else:
            print("Livro já existente!")
    def emprestar(self) -> None:
        fisico = input("Digite o tipo: ")
        if fisico == "fisico":
            fisico = True
        else:
            fisico = False 
        autor = input("Digite o nome do autor: ") 
        assunto = input("Digite o assunto: ") 
        resumo = input("Digite o resumo: ") 
        isbn = input("Digite o isbn: ") 
        titulo = input("Digite o titulo: ")
        emprestimo = input("Digite o tempo que ficará com ele: ")
        if self.bib.emprestar(fisico, autor, assunto, resumo, isbn, titulo, emprestimo):
            print("Livro cadastrado com sucesso!!")
        else:
            print("Livro já existente!")

    def remover_titulo(self) -> None:
        titulo = input("Digite o título: ")
        if self.bib.remover_titulo(titulo):
            print("Livro removido com sucesso!")
        else:
            print("Livro não encontrado!")

    def listar(self) -> None:
        livros = self.bib.listar()
        for livro in livros:
            print("--------------------")
            print("Título: ", livro.titulo)
        print("fim da lista de livros")

    def emprestados(self) -> None:
        emprestado = self.bib.emprestados()
        for livro in emprestado:
            print("--------------------")
            print("Título: ", livro.titulo)
        print("fim da lista de livros")

    def mostrar_nao_emprestado(self) -> None:
        nao_emprestado = self.bib.mostrar_nao_emprestado()
        for livro in nao_emprestado:
            print("--------------------")
            print("Título: ", livro.titulo)
        print("fim da lista de livros")

    def imprimir_menu(self) -> None:
        print("-------------------Menu--------------")
        print("|   1- Cadastrar novo livro         |")
        print("|   2- Emprestar livro              |")
        print("|   3- Remover livro                |")
        print("|   4- Litar todos                  |")
        print("|   5- listar emprestados           |")
        print("|   6- listar não emprestados       |")
        print("|   7- Sair                         |")
        print("-------------------------------------")

    def main(self):
        sair = False
        while not sair:
            self.imprimir_menu()
            opcao = int(input("O que você deseja fazer: "))
            if opcao == 1:
                self.adicionar()
            elif opcao == 2:
                self.emprestar()
            elif opcao == 3:
                self.remover_titulo()
            elif opcao == 4:
                self.listar()
            elif opcao == 5:
                self.emprestados()
            elif opcao == 6:
                self.mostrar_nao_emprestado()
            elif opcao == 7:
                sair = True
            else:
                print("Opção inválida!")

if __name__ == "__main__":
    app = IntGrafica()
    app.main()