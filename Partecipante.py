class Partecipante():
    def __init__(self, nome):
        self.nome=nome
        self.crediti=500
        self.listaAquisti=[]

    def __str__(self):
        return str(self.nome)+": "+str(self.crediti)

    def addPlayer(self,calciatore, crediti):
        self.listaAquisti.append(calciatore)
        self.crediti=self.crediti-crediti

    def numeroRuolo(self,ruolo):
        count=0
        for i in self.listaAquisti:
            if i.ruolo==ruolo:
                count+=1
        return count
