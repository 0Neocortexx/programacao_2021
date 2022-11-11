class Nota(object):
    def __init__(self,matricula: int, nome: str, prova1: float, prova2: float, trabalho: float) -> None:
        self.matricula = matricula
        self.nome = nome
        self.prova1 = prova1
        self.prova2 = prova2
        self.trabalho = trabalho
        self.media = None
        self.final = None

    def definir_media(self, media) -> float:
        media = (float(self.prova1 * 2.5) + (self.prova2 * 2.5) + (self.trabalho * 2) / 7)
        self.media = media
        media = self.media
        return media

    def definir_final(self) -> float:
        final = (float(7 - self.media))
        self.final = final
        if self.final == 0:
            return 0
        else:
            return self.final


aluno = Nota(1234, "Jonathan Emmanuel De Oliveira", 2.5, 2.5, 2)

print("Matricula do aluno:",aluno.matricula)
print("Nome do aluno:",aluno.nome)
print("Média do aluno:",aluno.definir_media)
print("Nota final necessaria para passar de ano na prova final:",aluno.definir_final)
    