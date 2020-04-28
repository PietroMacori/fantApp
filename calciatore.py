class calciatore():

    def __init__(self,nome,squadra,ruolo,presenze=0,fv=0,mv=0):
        self.nome=nome
        self.squadra=squadra
        self.ruolo=ruolo
        self.presenze=presenze
        self.fv=fv
        self.mv=mv
        self.venduto=False


    def __str__(self):
        return self.nome + " " + self.squadra
