class Livro(object):

    def __init__(self, fisico: bool, autor: str, assunto: str,
                 resumo: str, isbn: str, titulo: str) -> None:
        self.__fisico = fisico
        self.autor = autor
        self.assunto = assunto
        self.resumo = resumo
        self.__isbn = isbn
        self.titulo = titulo

    def get_isbn(self) -> str:
        return self.__isbn

    def set_isbn(self, novo_isbn: str) -> None:
        self.__isbn = novo_isbn

    def get_fisico(self) -> bool:
        return self.__fisico

    def set_fisico(self, novo_tipo: bool) -> None:
        self.__fisico = novo_tipo

class Biblioteca(object):

    def __init__(self):
        self.__livros = []

    def buscar_titulo(self, titulo: str) -> Livro:
        for livro in self.__livros:
            if livro.titulo == titulo:
                return livro
        return None

    def adicionar(self, fisico: bool, autor: str, assunto: str,
                  resumo: str, isbn: str, titulo: str) -> bool:
        if self.buscar_titulo(titulo) is None:
            novo_livro = Livro(fisico, autor, assunto, resumo, isbn, titulo)
            self.__livros.append(novo_livro)
            return True
        return False

    def remover_titulo(self, titulo: str) -> bool:
        livro = self.buscar_titulo(titulo)
        if livro is not None:
            self.__livros.remove(livro)
            return True
        return False

    def listar(self) -> list:
        print(id(self.__livros))
        return self.__livros[:]

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

    def imprimir_menu(self) -> None:
        print("-------------------Menu--------------")
        print("|        1- Cadastrar novo livro    |")
        print("|        2- Remover livro           |")
        print("|        3- Listar livros           |")
        print("|        4- Sair                    |")
        print("-------------------------------------")

    def main(self):
        sair = False
        while not sair:
            self.imprimir_menu()
            opcao = int(input("O que você deseja fazer: "))
            if opcao == 1:
                self.adicionar()
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