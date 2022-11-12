from livro import Livro

class Biblioteca(object):

    def __init__(self):
        self.__livros = []
        self.__emprestado = []
        self.__nao_emprestado = []

    def buscar_titulo(self, titulo: str) -> Livro:
        for livro in self.__livros:
            if livro.titulo == titulo:
                return livro
        return None

    def buscar_titulo2(self, titulo: str) -> Livro:
        for livro in self.__nao_emprestado:
            if livro.titulo == titulo:
                return livro

    def buscar_titulo3(self, titulo: str) -> Livro:
        for livro in self.__nao_emprestado:
            if livro.titulo == titulo:
                return livro
        return None

    def adicionar(self, fisico: bool, autor: str, assunto: str,
                  resumo: str, isbn: str, titulo: str) -> bool:
        if self.buscar_titulo(titulo) is None:
            novo_livro = Livro(fisico, autor, assunto, resumo, isbn, titulo, None)
            self.__livros.append(novo_livro)
            self.__nao_emprestado.append(novo_livro)
            return True
        return False

    def emprestar(self, fisico: bool, autor: str, assunto: str, resumo: str, isbn: str, titulo: str, emprestimo:str) -> bool:
        if self.buscar_titulo(titulo) is None:
            novo_livro = Livro(fisico, autor, assunto, resumo, isbn, titulo, emprestimo)
            self.__livros.append(novo_livro)
            self.__emprestado.append(novo_livro)
            return True
        return False    

    def remover_titulo(self, titulo: str) -> bool:
        livro = self.buscar_titulo(titulo)
        if livro is not None:
            self.__livros.remove(livro)
            return True
        return False

        livro = self.buscar_titulo2(titulo)
        if livro is not None:
            self.__nao_emprestado.remove(livro)
            return True
        return False

        livro = self.buscar_titulo3(titulo)
        if livro is not None:
            self.__emprestado.remove(livro)
            return True
        return False

    def listar(self) -> list:
        print(id(self.__livros))
        return self.__livros[:]

    def emprestados(self) -> list:
        print (id(self.__emprestado))
        return self.__emprestado[:]

    def mostrar_nao_emprestado(self) -> list:
        print (id(self.__nao_emprestado))
        return self.__nao_emprestado[:]

    






