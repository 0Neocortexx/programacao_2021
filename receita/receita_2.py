from receita_1 import Receita
# Classe 2
class CodeReceita(object):

    def __init__(self):
        self.__receita = []

    def buscar_receita(self, nome: str) -> Receita:
        for receita in self.__receita:
            if receita.nome == nome:
                return receita
        return None

# Adicionar Receita

    def adicionar_receita(self, nome: str, ingredientes: str, preparo: str) -> bool:
        if self.buscar_receita(nome) is None:
            nova_receita = Receita(nome, ingredientes, preparo)
            self.__receita.append(nova_receita)
            return True
        return False

# Remover receita

    def remover_receita(self, nome: str) -> bool:
        receita = self.buscar_receita(nome)
        if receita is not None:
            self.__receita.remove(receita)
            return True
        return False

# Listar Receitas

    def listar(self) -> list:
        print(id(self.__receita))
        return self.__receita[:]
