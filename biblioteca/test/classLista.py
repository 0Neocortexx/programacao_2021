class Livro(object):

    def __init__(self, autor: str, resumo: str, assunto, isbn: int):

        self.autor = autor

        self.resumo = resumo

        self.assunto = assunto

        self.isbn = isbn

        self.formato = None

class Ferramentas(object):

    def __init__(self):

       self.estante = []

    def adicionar_livro(self):

        novo_livro = Livro("Pedro","Joaozinho","Joãozinho chora no banho","Joaozinho vai pro banho e chora",1243435)
        if not self.procurar_livro(novo_livro):
            self.bibloteca.append(novo_livro)
            return True
        return False

    def mostrar_estante(self):

        for liv in self.estante:

            print("Autor:",liv.autor, "Resumo:",liv.resumo, "Assunto:",liv.assunto, "ISBN:",liv.isbn)

estante = Ferramentas()

estante.adicionar_livro("lala", "lala", "lala", 111)

estante.mostrar_estante()