
# Classe 1

class Data(object):

    def __init__(self, dd: int, mm: int, aa: int) -> None:
        self.dia = dd
        self.mes = mm
        self.ano = aa
    
# Set / Get

    def get_dd(self) -> int:
        return self.dd

    def set_dd(self, novo_dd: int) -> None:
        self.dd = novo_dd

    def get_mm(self) -> int:
        return self.mm

    def set_mm(self, novo_mm: int) -> None:
        self.mm = novo_mm
    
    def get_aa(self) -> int: 
        return self.aa

    def set_a(self, novo_aa: int) -> None:
        self.aa = novo_aa

# End Set / Get

class CodeData(object):

    def __init__(self) -> None:
        self.cod = []

    def definir_ano(self, aa: int) -> bool:
        
        # Pular Ano
        
        if aa % 400 == True and aa % 4 == True and aa % 100 == False:
            self.aa_bissexto = aa

        else: 
            self.aa_nao_bissexto = aa

        if self.aa_bissexto == True:
            return self.aa_bissexto + 1

        elif self.aa_nao_bissexto == True:
            return self.aa_nao_bissexto + 1
        
        else:
            texto = ("Este ano é inválido1")
            return texto

        # End Pular Ano

    def definir_mes(self, mm:int) -> None:

        # Pular mês

        if mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12:
            self.mes_31 = mm

        elif mm == 4 or mm == 6 or mm == 9 or mm == 11:
            self.mes_30 = mm

        elif mm == 2:
            self.mes_fev = mm

        else: 
            texto2 = ("Este Mês não é válido!")
            return texto2

        if mm == self.mes_31:
            self.new_mes = mm + 1

        elif mm == self.mes_30:
            self.new_mes = mm + 1

        elif mm == 12:
            self.new_mes = 1    

        elif mm == self.mes_fev:
            self.new_mes = mm + 1

        else:
            texto3 = ("Este mês é inválido!")
            return texto3

        # End Pular mês

    def definir_dia(self, dd:int, mm: int, aa: int) -> None:

        # Pular Dia

        if dd > 0 and mm == self.mes_31 and dd < 30:
            self.new_dd = dd + 1

        if dd > 0 and mm == self.mes_30 and dd < 30:
            self.new_dd = dd + 1

        elif dd == 31 and not self.mes_fev and self.mes_31:
            self.new_dd = 1

        elif dd == 30 and not self.mes_fev and self.mes_30:
            self.new_dd = 1

        elif aa == self.aa_bissexto and self.mes_fev and dd == 29:
            self.new_dd = 1

        elif aa == self.aa_nao_bissexto and self.mes_fev and dd == 28:
            self.new_dd = 1

        elif dd > 0 and self.mes_fev and dd < 28:
            self.new_dd = dd + 1

        else: 
            texto2 = ("Este dia é inválido!")
            return texto2
        
        # End Pular dia

class Sala(object):

    def __init__(self) -> None:
        self.num = CodeData
        
        # Avançar data

    def alterar_data(self) -> None:

        # Executar Ano

        aa = int(input("Digite o ano desejado: "))

        aa = self.num.definir_ano()
        print(aa)
        
        # Executar mês 

        mm = int(input("Digite o mês desejado: "))

        if self.num.definir_mes():
            print(mm)
        else:
            print("Não foi possivel encontrar o mês!")

        # Executar Dia

        dd = int(input("Digite o dia desejado: "))

        if self.num.definir_dia():
            print(dd)
        else:
            print("Não foi possivel encontrar o dia!")
    
    def main(self) -> None:
        self.alterar_data()

if __name__ == "__main__":
    app = Sala()
    app.main()