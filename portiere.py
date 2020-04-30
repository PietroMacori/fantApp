from Calciatore import *

class Portiere(Calciatore):

    def __init__(self,nome,squadra,ruolo,presenze,fv,mv, rigoriParati, golSubiti):
        Calciatore.__init__(self,nome,squadra,ruolo,presenze,fv,mv)
        self.rigoriParati=rigoriParati
        self.golSubiti=golSubiti


    def __str__(self):
        return self.nome + " " + self.squadra + " " + self.ruolo + " " + str(self.golSubiti)
