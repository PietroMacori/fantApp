from PyQt5 import QtGui,QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea,QHBoxLayout, QVBoxLayout, QGroupBox, QLabel, QPushButton, QFormLayout, QStackedWidget, QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import *
import string
import sys
from functools import partial
import numbers
import operator


class Window(QWidget):
    def __init__(self,listaG,listaP):
        super().__init__()
        #Window Settings
        self.title = "fantAsta"
        self.top = 0
        self.left =0
        self.width = 1800
        self.height = 900
        self.listaG=listaG
        self.listPLayersParziale=[]

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #Scrolling Area Settings
        self.scrollLayout =QVBoxLayout()
        self.groupBox = QGroupBox("Giocatori")
        self.listPlayersButton = []

        #Add all players on the scroll list
        for i in range(len(listaG)):
            self.listPlayersButton.append(QPushButton(listaG[i].nome + '    (' +listaG[i].squadra[:3] +')          FM: '+str(listaG[i].fv)))
            self.listPlayersButton[i].setFixedHeight(35)
            self.listPlayersButton[i].clicked.connect(partial(self.showInfoPlayer,listaG[i]))
            self.scrollLayout.addWidget(self.listPlayersButton[i])

        self.groupBox.setLayout(self.scrollLayout)
        self.scroll = QScrollArea()
        self.scroll.setWidget(self.groupBox)
        self.scroll.setWidgetResizable(True)
        self.scroll.setFixedHeight(800)
        self.scroll.setFixedWidth(650)

        #Left Zone
        self.groupBoxLeft=QGroupBox("Partecipanti")
        self.groupBoxLeft.setFixedHeight(800)
        self.groupBoxLeft.setFixedWidth(300)
        self.layoutLeft=QVBoxLayout()
        listaPartecipantiButton = []
        for i in range(len(listaP)):
            listaPartecipantiButton.append(QPushButton(listaP[i].nome))
            listaPartecipantiButton[i].setFixedHeight(78)
            listaPartecipantiButton[i].clicked.connect(partial(self.showPartecipante, listaP[i]))
            self.layoutLeft.addWidget(listaPartecipantiButton[i])

        self.groupBoxLeft.setLayout(self.layoutLeft)

        #Central Zone
        self.stack=QStackedWidget()
        self.stackBase=QWidget()
        self.stackPartecipanti=QWidget()
        self.stackGiocatori=QWidget()

        self.stackUIbase()
        self.stackUIPartecipanti()
        #self.stackUIGiocatori()


        self.layoutCentral=QHBoxLayout()
        self.layoutCentral.addWidget(self.stack)
        self.groupBoxCentral=QGroupBox('Main')
        self.groupBoxCentral.setFixedWidth(700)
        self.groupBoxCentral.setFixedHeight(800)
        self.groupBoxCentral.setLayout(self.layoutCentral)


        self.stack.addWidget(self.stackBase)
        self.stack.addWidget(self.stackPartecipanti)


        #Window Layout
        layout = QHBoxLayout(self)
        layout.addWidget(self.groupBoxLeft)
        layout.addWidget(self.groupBoxCentral)
        layout.addWidget(self.scroll)

        self.show()

    def showInfoPlayer(self, giocatore):
        print(giocatore)

    def showPartecipante(self, partecipante):
        self.stack.setCurrentIndex(1)
        self.labelNomePartecipante.setText(partecipante.nome)
        self.labelCreditiPartecipante.setText(str(partecipante.crediti))
        self.labelRimastiPartecipante.setText(str(27-len(partecipante.listaAquisti)))
        img=QPixmap('img/'+partecipante.nome+'.jpg')
        img=img.scaled(250,250,Qt.KeepAspectRatio)
        self.imagePartecipante.setPixmap(img)



    def stackUIbase(self):
        self.layoutBaseVertical=QVBoxLayout()
        self.groupBaseVertical=QGroupBox()
        self.layoutBaseHorizontal=QFormLayout()

        self.layoutBaseVertical.addWidget(self.groupBaseVertical)
        self.groupBaseVertical.setLayout(self.layoutBaseHorizontal)
        self.inputNome=QLineEdit(self)
        self.inputSquadra=QLineEdit(self)
        self.inputFM=QLineEdit(self)

        self.inputNome.setMinimumWidth(450)
        self.inputSquadra.setMinimumWidth(450)
        self.inputFM.setMinimumWidth(450)


        self.labelNome=QLabel('Nome')
        self.labelSquadra=QLabel('Squadra')
        self.labelFM=QLabel('FantaMedia')
        self.labelFM.setMinimumWidth(140)
        self.labelSquadra.setMinimumWidth(140)
        self.labelNome.setMinimumWidth(140)
        self.layoutBaseHorizontal.addRow(self.labelNome,self.inputNome)
        self.layoutBaseHorizontal.addRow(self.labelSquadra,self.inputSquadra)
        self.layoutBaseHorizontal.addRow(self.labelFM,self.inputFM)
        self.groupBaseVertical.setFixedHeight(300)

        self.buttonCerca=QPushButton('Cerca')
        self.buttonCerca.clicked.connect(self.cerca)
        self.layoutBaseVertical.addWidget(self.buttonCerca)



        self.stackBase.setLayout(self.layoutBaseVertical)


    def stackUIPartecipanti(self):
        layoutPartecipanti=QVBoxLayout()
        layoutAlto=QHBoxLayout()
        layoutBasso=QHBoxLayout()
        layoutAltoDati=QVBoxLayout()
        layoutPortieri=QVBoxLayout()
        layoutDifensori=QVBoxLayout()
        layoutCentrocampisti=QVBoxLayout()
        layoutAttaccanti=QVBoxLayout()

        self.labelNomePartecipante=QLabel()
        self.labelCreditiPartecipante=QLabel()
        self.labelRimastiPartecipante=QLabel()
        self.imagePartecipante=QLabel()

        p=QLabel('Portieri')
        d=QLabel('Difensori')
        c=QLabel('Centro')
        a=QLabel('Atacca')

        b1=QPushButton('Bonucci')
        b1.setFixedHeight(20)
        b2=QPushButton('Chiellini')
        b2.setFixedHeight(20)
        b3=QPushButton('Parolo')
        b3.setFixedHeight(20)
        b4=QPushButton('De Sciglio')
        b4.setFixedHeight(20)
        b5=QPushButton('Ronaldo')
        b5.setFixedHeight(20)
        b6=QPushButton('Lukaku')
        b6.setFixedHeight(20)
        b7=QPushButton('Icardi')
        b7.setFixedHeight(20)
        b8=QPushButton('Belotti')
        b8.setFixedHeight(20)



        p.setAlignment(Qt.AlignCenter)
        c.setAlignment(Qt.AlignCenter)
        d.setAlignment(Qt.AlignCenter)
        a.setAlignment(Qt.AlignCenter)

        layoutPortieri.addWidget(p)
        layoutDifensori.addWidget(d)
        layoutDifensori.addWidget(b1)
        layoutDifensori.addWidget(b2)
        layoutDifensori.addWidget(b3)
        layoutDifensori.addWidget(b4)
        layoutDifensori.addWidget(b5)
        layoutDifensori.addWidget(b6)
        layoutDifensori.addWidget(b7)
        layoutDifensori.addWidget(b8)
        layoutCentrocampisti.addWidget(c)
        layoutAttaccanti.addWidget(a)

        layoutAltoDati.addWidget(self.labelNomePartecipante)
        layoutAltoDati.addWidget(self.labelCreditiPartecipante)
        layoutAltoDati.addWidget(self.labelRimastiPartecipante)

        layoutBasso.addLayout(layoutPortieri)
        layoutBasso.addLayout(layoutDifensori)
        layoutBasso.addLayout(layoutCentrocampisti)
        layoutBasso.addLayout(layoutAttaccanti)

        layoutAlto.addWidget(self.imagePartecipante)
        layoutAlto.addLayout(layoutAltoDati)

        layoutPartecipanti.addLayout(layoutAlto)
        layoutPartecipanti.addLayout(layoutBasso)


        self.stackPartecipanti.setLayout(layoutPartecipanti)

    def back(self):
        self.stack.setCurrentIndex(0)

    def cerca(self):
        #Remove all players from old scroll
        for i in reversed(range(self.scrollLayout.count())):
            self.scrollLayout.itemAt(i).widget().setParent(None)

        #Remove all players from lista parziale
        self.listPLayersParziale.clear()
        tmpList=[]

        #Check if the FM is a float - if not set to 0
        try:
            inp=float(self.inputFM.text())
        except ValueError:
            inp=0
            self.inputFM.setText('0')

        #Select the filtered players
        for i in range(len(self.listaG)):
            if self.listaG[i].nome.startswith(self.inputNome.text().upper())==True and self.listaG[i].squadra.startswith(self.inputSquadra.text().title())==True and float(self.listaG[i].fv)>=float(inp):
                self.listPLayersParziale.append(QPushButton(self.listaG[i].nome + '    (' +self.listaG[i].squadra[:3] +')          FM: '+str(self.listaG[i].fv)))
                tmpList.append(self.listaG[i])

        #Add the correct players to the scroll list
        for i in range(len(self.listPLayersParziale)):
            self.listPLayersParziale[i].setFixedHeight(35)
            self.listPLayersParziale[i].clicked.connect(partial(self.showInfoPlayer, tmpList[i]))
            self.scrollLayout.addWidget(self.listPLayersParziale[i])
