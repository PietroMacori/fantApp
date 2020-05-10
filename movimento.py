from Calciatore import *

class Movimento(Calciatore):

    def __init__(self,nome,squadra,ruolo,presenze,fv,mv,gol,assist,rigori,gialli,rossi):
        Calciatore.__init__(self,nome,squadra,ruolo,presenze,fv,mv)
        self.gol=gol
        self.assist=assist
        self.rigori=rigori
        self.gialli=gialli
        self.rossi=rossi
        self.fv=fv

    def __str__(self):
        return self.nome + " " + self.squadra + " "+str(self.fv)
