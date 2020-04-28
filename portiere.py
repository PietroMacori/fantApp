from calciatore import *

class portiere(calciatore):

    def __init__(self,nome,squadra,ruolo,presenze,fv,mv, rigoriParati, golSubiti):
        calciatore.__init__(self,nome,squadra,ruolo,presenze,fv,mv)
        self.rigoriParati=rigoriParati
        self.golSubiti=golSubiti


    def __str__(self):
        return self.nome + " " + self.squadra + " " + self.ruolo + " " + str(self.golSubiti)
