from jogo import Jogo

class GravadorDeJogos(object):

    def gravar(self, lista_jogos) -> None:
        arquivo = open("lista_jogos.txt", "w")
        for jogo in lista_jogos:
            arquivo.write(jogo.converter_str()+ "\n")
        arquivo.close()

    def recuperar(self) -> list:
        arquivo = open("lista_jogos.txt", "r")
        lista = []
        for linha in arquivo.readlines():
            linha = linha.replace("\n", "")
            info = linha.split("  ")
            jogo = Jogo(info[0], info[1], info[2], info[3], info[4])
            lista.append(jogo)
        arquivo.close()
        return lista