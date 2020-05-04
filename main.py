from AstaManager import *
from Calciatore import *
from Movimento import *
from Portiere import *
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from testGUI import *



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


    #GUI
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
