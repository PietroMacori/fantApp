from AstaManager import *
from Calciatore import *
from Movimento import *
from Portiere import *
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
import testGUI
import os


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
    App = QApplication(sys.argv)
    path=os.path.join(os.path.dirname(sys.modules[__name__].__file__),'x.png')
    App.setApplicationName('FANTASTA')

    App.setWindowIcon(QIcon(path))
    window = testGUI.Window(listaG,listaP)
    sys.exit(App.exec())
