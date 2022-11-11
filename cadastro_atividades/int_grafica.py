from lista import Lista

class IntGrafica(object):

    def __init__(self)->None:

        self.list = Lista()

    def adicionar_atividade(self)->None: 

        materia = input("Materia?: ")
        atividade = input("Atividade?: ")
        data_de_entrega = input("Data?: ")

        if self.list.adicionar_atividade(materia, atividade, data_de_entrega):
            print("-----------------------------------------")
            print("Atividade Cadastrada!!")
        else:
            print("Não foi possível realizar o cadastro.")
    
    def remover_atividade(self)->None:
        data_de_entrega = input("Digite a data de entrega para remoção: ")
        if self.list.remover_atividade(data_de_entrega):
            print("-------------------------------------")
            print("Atividade Removida!!")
        else:
            print("Não foi possível remover a atividade :(.")

    def listar_atividades(self)->None:
        print("------------Lista--------------")
        self.list.listar_atividades()

    def imprimir_menu(self)->None:
        print("-----------------Menu----------------")
        print("|        1- Cadastrar atividade     |")
        print("|        2- Excluir atividade       |")
        print("|        3- Listar atividades       |")
        print("|        4- Sair                    |")
        print("-------------------------------------")
    
    def main(self):
        sair = False
        while not sair:
            self.imprimir_menu()
            opcao = int(input("Qual operação desejá realizar? "))
            if opcao == 1:
                self.adicionar_atividade()
            elif opcao == 2:
                self.remover_atividade()
            elif opcao == 3:
                self.listar_atividades()
            elif opcao == 4:
                sair = True
            else:
                print("Esta opção não existe.")
    
if __name__ == "__main__":
    app = IntGrafica()
    app.main()