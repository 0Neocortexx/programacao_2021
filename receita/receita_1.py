# Classe 1

class Receita(object):

    def __init__(self, nome: str, ingredientes: str, preparo:str) -> None:
        self.nome = nome
        self.ingredientes = ingredientes
        self.preparo = preparo
