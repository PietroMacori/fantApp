from calciatore import *

class movimento(calciatore):

    def __init__(self,nome,squadra,ruolo,presenze,fv,mv,gol,assist,rigori,gialli,rossi):
        calciatore.__init__(self,nome,squadra,ruolo,presenze,fv,mv)
        self.gol=gol
        self.assist=assist
        self.rigori=rigori
        self.gialli=gialli
        self.rossi=rossi

    def toString(self):
        return self.nome + " " + self.squadra 
