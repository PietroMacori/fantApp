from AstaManager import *
class Calciatore():

    def __init__(self,nome,squadra,ruolo,presenze=0,fv=0,mv=0):
        self.nome=nome
        self.squadra=squadra
        self.ruolo=ruolo
        self.presenze=presenze
        self.fv=fv
        self.mv=mv
        self.venduto=False
        self.partecipante=""
        self.costo=0


    def __str__(self):
        return self.nome + " " + self.squadra

    def calciatoreVenduto(self, partecipante):
        self.partecipante=partecipante
        self.venduto=True
