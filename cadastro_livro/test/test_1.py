class Livro:

    def __init__(self, titulo:str, autor:str, resumo:str, assunto, isbn:int):

        self.titulo = titulo
        self.autor = autor
        self.resumo = resumo
        self.assunto = assunto
        self.isbn = isbn

class Gerencidordelivros:

    def __init__(self):

        self.bibloteca=[]

    def procurar_livro(self, livro:Livro):

        for liv in self.bibloteca:
            if liv == livro:
                return True
        return False


    def adicionar_livro(self,titulo:str, autor:str, resumo:str, assunto:str, isbn:int):

        novo_livro = Livro(titulo,autor,resumo,assunto,isbn)
        if not self.procurar_livro(novo_livro):
            self.bibloteca.append(novo_livro)
            return True
        return False

    def remover_livro(self,titulo:str, autor:str, resumo:str, assunto:str, isbn:int):

        for liv in self.bibloteca:
            if liv.titulo == titulo and liv.autor == autor and liv.resumo == resumo and liv.assunto == assunto and liv.isbn == isbn:
                self.bibloteca.remove(liv)
                return True
        return False

    def imprimir_lista(self):

        for liv in self.bibloteca:
            print("Titulo:",liv.titulo,"Autor:",liv.autor,"Resumo:",liv.resumo,"Assunto:",liv.assunto,"ISBN:",liv.isbn)
        print("------------fim da lista-----------------")

bibloteca = Gerencidordelivros()
bibloteca.adicionar_livro('Livroteste','josé A.',".","sobre aquilo lá",456987)
bibloteca.adicionar_livro('Livroteste2','josé B.',"..","sobre aquilo lá 2",147896)
bibloteca.adicionar_livro('Livroteste3','josé C.',"...","sobre aquilo lá 3",762497)
bibloteca.adicionar_livro('Livroteste4','josé H.',"....","sobre aquilo lá 4",345698)
bibloteca.adicionar_livro('Livroteste5','josé i.',".....","sobre aquilo lá 5",896577)
bibloteca.adicionar_livro('Livroteste6','josé l.',"......","sobre aquilo lá 6",685269)
bibloteca.adicionar_livro('livroteste7','jose 49.', "......","sobre aquilo lá 49", 989898989)
bibloteca.imprimir_lista()
bibloteca.remover_livro('Livroteste6','josé l.',"......","sobre aquilo lá 6",685269)
bibloteca.imprimir_lista()