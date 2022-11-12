from lista import Apartamento

class Informacoes(object):

    def __init__(self):
        self.__lista = []

    def buscar_id(self, idlocal: int) -> Apartamento:
        for lista in self.__lista:
            if lista.idlocal == idlocal:
                return lista
        return None

    def adicionar(self, idlocal: int, vendedor: str, dimensoes: int, valor: int, localizacao: str, 
                  valorcondominio: int) -> None:
        novo_local = (idlocal, vendedor,dimensoes,valor,localizacao,valor,valorcondominio)
        self.__lista.append(novo_local)

    def remover_local(self, idlocal: str) -> None:
        lista = self.buscar_id(idlocal)
        if lista is not None:
            self.__lista.remove(lista)
            return None

    def listar(self) -> None:
        print(id(self.__lista))
        return self.__lista[:]

