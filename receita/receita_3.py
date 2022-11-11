from receita_2 import CodeReceita

# Classe 3

class IntGrafica(object):

    def __init__(self) ->None:
        self.cod = CodeReceita()

# Adicionar Receita

    def adicionar_receita(self) -> None:
        nome = input("Digite o nome da receita: ") 
        ingredientes = input("Digite os ingredientes da receita: ") 
        preparo = input("Digite o preparo da receita: ") 

        if self.cod.adicionar_receita(nome, ingredientes, preparo):
            print("Receita cadastrada com sucesso!!")
        else:
            print("Receita já existente!")
        
# Remover receita

    def remover_receita(self) -> None:
        nome = input("Digite o nome: ")
        if self.cod.remover_nome(nome):
            print("Receita removida com sucesso!")
        else:
            print("Receita não encontrada!")

# Listar Receitas

    def listar(self) -> None:
        receitas = self.cod.listar()
        for receita in receitas:
            print("--------------------")
            print("Receita: ", receita.nome)
        print("Fim das receitas!")

# Interface Interativa

    def imprimir_menu(self) -> None:
        print("-------------------Menu--------------")
        print("|        1- Cadastrar nova receita  |")
        print("|        2- Remover receita         |")
        print("|        3- Listar receitas         |")
        print("|        4- Sair                    |")
        print("-------------------------------------")

    def main(self):
        sair = False
        while not sair:
            self.imprimir_menu()
            opcao = int(input("O que você deseja fazer: "))
            if opcao == 1:
                self.adicionar_receita()
            elif opcao == 2:
                self.remover_receita()
            elif opcao == 3:
                self.listar()
            elif opcao == 4:
                sair = True
            else:
                print("Opção inválida!")

# Interface Interativa

if __name__ == "__main__":
    app = IntGrafica()
    app.main()
