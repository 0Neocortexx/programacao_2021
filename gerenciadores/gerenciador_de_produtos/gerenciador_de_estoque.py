from produto import Produto

class Gerenciador(object):

    def __init__(self) -> None:
        self.configurar = []

    def repeticao(self, produto: Produto):
        for pod in self.configurar:
            if pod == produto:
                return True        
        return False

    def cadastrar(self, nome: str, codigo: str, valor: float, quantidade: int):
        novo_produto = Produto(nome, codigo, valor, quantidade)
        if not self.repeticao(novo_produto):
            self.configurar.append(novo_produto)
            return True
        return False

    def remover(self, nome: str, codigo: str, valor: float, quantidade: int):
        for pod in self.configurar:
            if pod.nome == nome and pod.codigo == codigo and pod.valor == valor and pod.quantidade == quantidade:
                self.configurar.remove(pod)
                return True
            return False

    def listar(self) -> list:
        print(id(self.__produto))
        return self.__produto[:]
