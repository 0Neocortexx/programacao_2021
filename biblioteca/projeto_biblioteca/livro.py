class Livro(object):

    def __init__(self, fisico: bool, autor: str, assunto: str,
                 resumo: str, isbn: str, titulo: str, emprestimo = str) -> None:
        self.__fisico = fisico
        self.autor = autor
        self.assunto = assunto
        self.resumo = resumo
        self.__isbn = isbn
        self.titulo = titulo
        self.emprestimo = emprestimo

    def get_isbn(self) -> str:
        return self.__isbn

    def set_isbn(self, novo_isbn: str) -> None:
        self.__isbn = novo_isbn

    def get_fisico(self) -> bool:
        return self.__fisico

    def set_fisico(self, novo_tipo: bool) -> None:
        self.__fisico = novo_tipo