from AstaManager import *
from Calciatore import *
from Movimento import *
from Portiere import *

if __name__=="__main__":
    manager=AstaManager();

    listaG=manager.loadPlayer("/Users/pietromacori/github/fantApp/Quotazioni_Fantacalcio_Test.xlsx","/Users/pietromacori/github/fantApp/Statistiche_Fantacalcio_2018-19_Test.xlsx")

    manager.addPlayer("Pietro")
    manager.addPlayer("Bonny")
    manager.addPlayer("Mante")
    manager.addPlayer("Mora")
    manager.addPlayer("Feno")
    manager.addPlayer("Frank")
    manager.addPlayer("Matte")
    manager.addPlayer("Cava")
    manager.addPlayer("Nencio")
    manager.addPlayer("Eugi")

    listaP=manager.partecipanti()


    while True:
        quit=raw_input("Quit? y/n: ")
        if quit=="y":
            break
        else:
            for p in listaP.values():
                print("Please " + p.nome +" is ur turn")
                pick=raw_input("Seleziona giocatore: ")
                money=int(raw_input("Costo: "))
                if int(p.crediti)>int(money):
                    manager.aquista(p,listaG[pick],money)
                else:
                    print("Error")



    for x in listaG.values():
        print(str(x.nome) + " " + str(x.venduto))

    print("")
    for x in listaP.values():
        print(str(x.nome) + " "+ str(x.crediti))
