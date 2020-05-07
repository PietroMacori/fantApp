from PyQt5 import QtGui,QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea,QHBoxLayout, QVBoxLayout, QGroupBox, QLabel, QPushButton, QFormLayout
from PyQt5.QtCore import *
import sys


class Window(QWidget):
    def __init__(self,listaG):
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
            listPlayersButton[i].setFixedHeight(45)
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
        bMante=QPushButton("Mante")
        bPixy=QPushButton("Pixy")
        bEugi=QPushButton("Eugi")
        bCava=QPushButton("Cava")

        layoutLeft.addWidget(bMante)
        layoutLeft.addWidget(bPixy)
        layoutLeft.addWidget(bEugi)
        layoutLeft.addWidget(bCava)
        groupBoxLeft.setLayout(layoutLeft)

        #Central Zone
        groupBoxCentral=QGroupBox("Main")
        groupBoxCentral.setFixedHeight(800)
        groupBoxCentral.setFixedWidth(1000)
        b=QPushButton("Cazzoooo")
        b.setFixedWidth(500)



        #Window Layout
        layout = QHBoxLayout(self)
        layout.addWidget(groupBoxLeft)
        layout.addWidget(groupBoxCentral)
        layout.addWidget(scroll)


        self.show()
