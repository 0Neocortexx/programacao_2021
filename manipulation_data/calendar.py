from os import rename


class Calendario(object):

    def __init__(self, dd: int, mm: int, aa: int) -> None:
        self.dd = dd
        self.mm = mm
        self.aa = aa
        self.dd_final = None
        self.mm_final = None
        self.aa_final = None

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


class CodeDatas(object):

    def __init__(self) -> None:
        self.cad = []
    
    def definir_ano(self, aa:int) -> None:
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
    
    def definir_mes(self, mm:int) -> None:
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

    def definir_dia(self, dd:int, mm:int, aa:int) -> None:
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
            
    def listar(self) -> list:
        print(id(self.cad))
        return self.cad[:]

    def __repr__(self, dd: int, mm:int, aa:int) -> str:
        return "Dia: " + str(dd), "Mês: " + str(mm) , "Ano: " + str(aa)

class IntGrafica(object):
    
    def __init__(self) -> None:
        self.cod = CodeDatas

    def adicionar_data(self, dd: int, mm: int, aa: int) -> None:
        dd = input("Digite o dia: ")
        mm = input("Digite o mês: ")
        aa = input("Digite o ano: ")

        if self.cod.definir_ano(aa):
            print("Ano: ",aa)
        else: 
            print("bosta")

if __name__ == "__main__":
    app = IntGrafica()
    app.adicionar_data()
