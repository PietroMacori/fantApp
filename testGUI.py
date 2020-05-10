from PyQt5 import QtGui,QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea,QHBoxLayout, QVBoxLayout, QGroupBox, QLabel, QPushButton, QFormLayout
from PyQt5.QtCore import *
import sys
from functools import partial


class Window(QWidget):
    def __init__(self,listaG,listaP):
        super().__init__()
        #Window Settings
        self.title = "fantAsta"
        self.top = 0
        self.left =0
        self.width = 1800
        self.height = 900


        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #Scrolling Area Settings
        scrollLayout =QVBoxLayout()
        groupBox = QGroupBox("Giocatori rimanenti")
        listPlayersButton = []

        for i in range(len(listaG)):
            listPlayersButton.append(QPushButton(listaG[i].nome))
            listPlayersButton[i].setFixedHeight(35)
            listPlayersButton[i].clicked.connect(partial(self.showInfoPlayer,listaG[i]))
            scrollLayout.addWidget(listPlayersButton[i])

        groupBox.setLayout(scrollLayout)
        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(800)
        scroll.setFixedWidth(450)

        #Left Zone
        groupBoxLeft=QGroupBox("Partecipanti")
        groupBoxLeft.setFixedHeight(800)
        groupBoxLeft.setFixedWidth(300)
        layoutLeft=QVBoxLayout()
        listaPartecipantiButton = []
        for i in range(len(listaP)):
            listaPartecipantiButton.append(QPushButton(listaP[i].nome))
            listaPartecipantiButton[i].setFixedHeight(78)
            #listaPartecipantiButton[i].setStyleSheet('QPushButton {background-color: #DCDCDC}')
            layoutLeft.addWidget(listaPartecipantiButton[i])


        groupBoxLeft.setLayout(layoutLeft)

        #Central Zone
        layoutCentral=QVBoxLayout()
        groupBoxCentral=QGroupBox("Main")
        groupBoxCentral.setFixedHeight(800)
        groupBoxCentral.setFixedWidth(1000)
        groupBoxCentral.setLayout(layoutCentral)

        #b=QPushButton("Cazzoooo")

        #layoutCentral.addWidget(b)



        #Window Layout
        layout = QHBoxLayout(self)
        layout.addWidget(groupBoxLeft)
        layout.addWidget(groupBoxCentral)
        layout.addWidget(scroll)


        self.show()

    def showInfoPlayer(self, giocatore):
        print(giocatore)
