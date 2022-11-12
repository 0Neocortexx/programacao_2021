from gerenciador_de_jogos import GerenciadorDeJogos

class IntGrafica(object):

    def __init__(self)->None:

        self.bib = GerenciadorDeJogos()

    def adicionar_jogo(self)->None: 
        #Adiciona um joga a biblioteca
        titulo = input("Digite o título do jogo:")
        produtora = input("Digite o nome da produtora do jogo:")
        distribuidora = input("Digite o nome da distribuidora:")
        valor = float(input("Digite o valor do jogo:"))
        faixaetaria = input("Digite a classificação etária do jogo:")
        if self.bib.adicionar_jogo(titulo,produtora,distribuidora,valor,faixaetaria):
            print("-----------------------------------------")
            print("Jogo cadastrado com sucesso!!!!!")
        elif faixaetaria not in ["livre","10",'12',"14","16","18"]:
            print("Esta faixa etária não existe")
        else:
            print("Não foi possível realizar o cadastro.")
    
    def remover_jogo(self)->None:
        #Remove um jogo da bibloteca
        titulo = input("Digite o título do jogo que desejá remover:")
        if self.bib.remover_jogo(titulo):
            print("-------------------------------------")
            print("Jogo removido com sucesso!!!!")
        else:
            print("Não foi possível remover o jogo.")
        
    def alterar_dados(self)->None:
        #Altera os dados de um jogo
        titulo = input("Digite o título do jogo que desajá realizar a alteração de dados:")
        novo_titulo = input("Digite o novo título:")
        nova_produtora = input("Digite o nome da nova produtora:")
        nova_distribuidora = input("Digite o nome da nova distribuidora:")
        novo_valor = float(input("Digite o novo valor:"))
        nova_faixaetaria = input("Digite a nova faixa etária:")
        if nova_faixaetaria not in ["livre","10",'12',"14","16","18"]:
            print("Esta faixa etária não existe")
        elif self.bib.alterar_dados(titulo,novo_titulo,nova_produtora,
                                    nova_distribuidora,novo_valor,nova_faixaetaria):
            print("-----------------------------------------")
            print("Alteração de dados executada com sucesso.")
        else:
            print("Não foi possível realizar a alteração de dados")
        
    def listar_jogos(self)->None:
        #Lista os jogos da bibloteca
        print("------------Lista--------------")
        self.bib.listar_jogos()

    def imprimir_menu(self)->None:
        print("-----------------Menu----------------")
        print("|        1- Cadastrar Jogo          |")
        print("|        2- Excluir Jogo            |")
        print("|        3- Alterar dados           |")
        print("|        4- Listar jogos            |")
        print("|        5- Sair                    |")
        print("-------------------------------------")
    
    def main(self):
        sair = False
        while not sair:
            self.imprimir_menu()
            opcao = int(input("Qual operação desejá realizar? "))
            if opcao == 1:
                self.adicionar_jogo()
            elif opcao == 2:
                self.remover_jogo()
            elif opcao == 3:
                self.alterar_dados()
            elif opcao == 4:
                self.listar_jogos()
            elif opcao == 5:
                sair = True
            else:
                print("Esta opção não existe.")
    
if __name__ == "__main__":
    app = IntGrafica()
    app.main()
