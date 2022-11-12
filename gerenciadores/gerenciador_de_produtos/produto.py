class Produto(object):

    def __init__(self, nome: str, codigo: str, valor: float, quantidade: int):
        self.nome = nome
        self.codigo = codigo
        self.valor = valor
        self.quantidade = quantidade