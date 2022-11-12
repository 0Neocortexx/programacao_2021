class Jogo(object):

    def __init__(self, titulo:str, produtora:str, distribuidora:str, valor:float, faixaetaria:str) -> None:
       self.titulo = titulo
       self.produtora =  produtora
       self.distribuidora = distribuidora
       self.valor = valor
       self.faixaetaria = faixaetaria

    def set_faixaetaria(self, nova_faixaetaria:str) -> None:
        if nova_faixaetaria in ["livre","10","12",'14','16','18']:
            self.faixaetaria = nova_faixaetaria
        else:
            print("Esta faixa etária não existe!")

    def get_faixaetaria(self) -> str:
        return self.faixaetaria

    def set_titulo(self, novo_titulo:str) ->None:
        self.titulo = novo_titulo

    def get_titulo(self) -> str:
        return self.titulo

    def set_produtora(self, nova_produtora:str)->None:
        self.produtora = nova_produtora

    def get_produtora(self)->str:
        return self.produtora

    def set_distribuidora(self, nova_distribuidora:str)->None:
        self.distribuidora = nova_distribuidora

    def get_distribuidora(self)->str:
        return self.distribuidora

    def set_valor(self, novo_valor:float)->None:
        if novo_valor >= 0:
            self.valor = novo_valor
        else:
            print("O valor não pode ser negativo!")
        
    def __eq__(self, other)->bool:
        if self.titulo == other.titulo:
            return True
        return False
        
    def converter_str(self):
        return self.titulo +"  "+ self.produtora +"  "+ self.distribuidora +"  "+str(self.faixaetaria) +"  "+ str(self.valor)