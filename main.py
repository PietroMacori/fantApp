import xlrd
from calciatore import *
from movimento import *
from portiere import *

if __name__=="__main__":

    loc=("/Users/pietromacori/github/fantApp/Quotazioni_Fantacalcio_Test.xlsx")

    wb=xlrd.open_workbook(loc)
    sheet=wb.sheet_by_index(0)
    sheet.cell_value(0,0)
    listaNuova=[]

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
            listaNuova.insert(i,newc)
        else:
            newc=movimento(nome,squadra,ruolo,0,0,0,0,0,0,0,0)
            listaNuova.insert(i,newc)



    for i in range(len(listaNuova)):
        print(listaNuova[i].toString())
