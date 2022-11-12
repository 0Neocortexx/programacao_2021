class Casa(object):

    def __init__(self, idlocal:int, vendedor: str, dimensoes: int, valor: int, localizacao: str) -> None:
        self.idlocal = idlocal
        self.vendedor = vendedor
        self.dimensoes = dimensoes
        self.valor = valor
        self.localizacao = localizacao
    
        
class Apartamento(Casa):
    def __init__(self, idlocal:int, vendedor: str, dimensoes: int, valor: int, localizacao: str, valorcondominio: int):
        super().__init__(self, idlocal, vendedor, dimensoes, valor, localizacao)
        self.valorcondominio = valorcondominio

