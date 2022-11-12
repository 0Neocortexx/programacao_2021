class Livro(object):

    def __init__(self, autor: str, resumo: str, assunto, isbn: int):

        self.autor = autor

        self.resumo = resumo

        self.assunto = assunto

        self.isbn = isbn

        self.fisico = False

    def fis(self) -> None:
        self.fisico = True

    def ele(self) -> None:
        self.eletronico = False

