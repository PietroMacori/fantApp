import xlrd
from calciatore import *
from movimento import *
from portiere import *

class astaManager():

    def loadPlayer(self,path1,path2):
        listaVecchia=[]
        listaCompleta=[]
        listaNuova={}

        wb2=xlrd.open_workbook(path2)
        sheet2=wb2.sheet_by_index(0)
        sheet2.cell_value(0,0)

        #Load players of this year
        for i in range(sheet2.nrows):
            for j in range(sheet2.ncols):
                if j==0:
                    ruolo=sheet2.cell_value(i,j)
                elif j==1:
                    nome=sheet2.cell_value(i,j)
                elif j==2:
                    squadra=sheet2.cell_value(i,j)
                elif j==3:
                    presenze=sheet2.cell_value(i,j)
                elif j==4:
                    mv=sheet2.cell_value(i,j)
                elif j==5:
                    fv=sheet2.cell_value(i,j)
                elif j==6:
                    if ruolo!="P":
                        gol=sheet2.cell_value(i,j)
                elif j==7:
                    if ruolo=="P":
                        golSubiti=sheet2.cell_value(i,j)
                elif j==8:
                    if ruolo=="P":
                        rigoriParati=sheet2.cell_value(i,j)
                elif j==9:
                    if ruolo!="P":
                        rigoriCalciati=sheet2.cell_value(i,j)
                elif j==12:
                    if ruolo!="P":
                        assist=sheet2.cell_value(i,j)
                elif j==14:
                    gialli=sheet2.cell_value(i,j)
                elif j==15:
                    rossi=sheet2.cell_value(i,j)
                else:
                    pass

            if ruolo=="P":
                newc=portiere(nome,squadra,ruolo,presenze,fv,mv,rigoriParati,golSubiti)
                listaVecchia.insert(i,newc)
            else:
                newc=movimento(nome,squadra,ruolo,presenze,fv,mv,gol,assist,rigoriCalciati,gialli,rossi)
                listaVecchia.insert(i,newc)


        wb=xlrd.open_workbook(path1)
        sheet=wb.sheet_by_index(0)
        sheet.cell_value(0,0)
        #Load players of last year
        for i in range(sheet.nrows):
            for j in range(sheet.ncols):
                if j==0:
                    ruolo=sheet.cell_value(i,j)
                elif j==1:
                    nome=sheet.cell_value(i,j)
                elif j==2:
                    squadra=sheet.cell_value(i,j)

            if ruolo=="P":
                newc=portiere(nome,squadra,ruolo,0,0,0,0,0)
                listaNuova[nome]=newc
            else:
                newc=movimento(nome,squadra,ruolo,0,0,0,0,0,0,0,0)
                listaNuova[nome]=newc

        #Remove players that are no more in Serie A and update teams
        for i in range(len(listaVecchia)):
            if listaNuova.has_key(listaVecchia[i].nome)==True:
                gioc=listaNuova[listaVecchia[i].nome]
                listaVecchia[i].squadra=gioc.squadra
                listaCompleta.append(listaVecchia[i])

        return listaCompleta
