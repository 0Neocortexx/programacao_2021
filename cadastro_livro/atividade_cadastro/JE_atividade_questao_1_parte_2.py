from JE_atividade_questao_1_parte_1 import Livro

class Ferramentas(object):

    def __init__(self) -> None:
        
        self.estante = []

    def repeticao(self, livro: Livro):

        for liv in self.estante:

            if liv == livro:

                return True
                
        return False


    def adicionar_livro(self,autor:str, resumo:str, assunto:str, isbn:int):

        novo_livro = Livro(autor,resumo,assunto,isbn)

        if not self.repeticao(novo_livro):

            self.estante.append(novo_livro)

            return True

        return False

    def mostrar_estante(self):

        for liv in self.estante:
             print("Autor:",liv.autor,"Resumo:",liv.resumo,"Assunto:",liv.assunto,"ISBN:",liv.isbn)
        print("------------------Limite----------------------")

    def remover_livro(self,autor:str, resumo:str, assunto:str, isbn:int):

        for liv in self.estante:

            if liv.autor == autor and liv.resumo == resumo and liv.assunto == assunto and liv.isbn == isbn:

                self.estante.remove(liv)

                return True

        return False


estante = Ferramentas()

estante.adicionar_livro("Autor 1", "Resumo 1","Genero 1",10101)
estante.adicionar_livro("Autor 2", "Resumo 2","Genero 2",10102)
estante.adicionar_livro("Autor 3", "Resumo 3","Genero 3",10103)
estante.adicionar_livro("Autor 4", "Resumo 4","Genero 4",10104)
estante.adicionar_livro("Autor 5", "Resumo 5","Genero 5",10105)
estante.mostrar_estante()
estante.remover_livro("Autor 1", "Resumo 1","Genero 1",10101)
estante.mostrar_estante()