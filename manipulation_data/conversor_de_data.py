# Conversor de datas --
class Data:

    def __init__(self, dia: int, mes: int, ano: int) -> None:
        self.dia = input("Digite o dia: ")
        self.mes = input("Digite o mês: ")
        self.ano = input("Digite o ano: ")

    def conclusao (self, dia: int, mes: int, ano: int):
        self.dd = dia
        print(dia)
        self.mm = mes
        print(mes)
        self.aa = ano
        print(ano)
        
dd_mm_aa = Data (00,00,0000)
 #Data Brasileira
print("Data Brasileira:",dd_mm_aa.dia,"/",dd_mm_aa.mes,"/",dd_mm_aa.ano)
 #Data Americana
print("Data Americana:", dd_mm_aa.mes,"/", dd_mm_aa.dia,"/",dd_mm_aa.ano)