from typing import List
from jogo import Jogo
from gravador import GravadorDeJogos

class GerenciadorDeJogos(object):

    def __init__(self) -> None:
        
        self.biblioteca = []

    def carregar_lista_jogos(self, lista: list)-> None:
        self.biblioteca = lista

    def buscar_jogo(self, jogo:Jogo)->bool:
        for game in self.biblioteca:
            if jogo == game:
                return True
        return False

    def adicionar_jogo(self, titulo:str, produtora:str, distribuidora:str, 
                        valor:float, faixaetaria:str)->bool:
    
        jogo = Jogo(titulo, produtora, distribuidora, valor, faixaetaria)
        
        if faixaetaria in ["livre","10",'12',"14","16","18"]:
            if self.buscar_jogo(jogo) == False:
                self.biblioteca.append(jogo)
                return True
            return False
        else:
            return False
    
    def remover_jogo(self, titulo:str)->bool:
        for game in self.biblioteca:
            if game.titulo == titulo:
                self.biblioteca.remove(game)
                return True
        return False

    def alterar_dados(self, titulo_do_jogo:str, novo_titulo:str, nova_produtora:str, 
                        nova_distribuidora:str, novo_valor:float, nova_faixaetaria:str) -> bool:
        # O titulo_do_jogo vai ser utilizado para identificar o joga que o usuário deseja alterar
        for game in self.biblioteca:
            if game.titulo == titulo_do_jogo:
                game.set_titulo(novo_titulo)
                game.set_produtora(nova_produtora)
                game.set_distribuidora(nova_distribuidora)
                game.set_valor(novo_valor)
                game.set_faixaetaria(nova_faixaetaria)
                return True
        return False

    def listar_jogos(self)->list:
        return list(self.biblioteca)