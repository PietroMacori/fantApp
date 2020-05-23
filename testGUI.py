from PyQt5 import QtGui,QtCore
from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox,QComboBox,QLayoutItem,QSizePolicy,QSpacerItem,QAbstractItemView, QScrollArea,QHBoxLayout, QVBoxLayout, QGroupBox, QLabel,QHeaderView ,QPushButton, QFormLayout, QStackedWidget, QLineEdit,QAction ,QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QPixmap,QIcon,QFont
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
        self.listaP=listaP
        self.listPLayersParziale=[]
        self.ruoli={'P':'Portiere','C':'Centrocampista','D':'Difensore','A':'Attaccante'}
        self.disp={'P':3,'D':8,'C':8,'A':6}

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #Scrolling Area Settings
        self.scrollLayout =QVBoxLayout()
        self.scrollLayout.setAlignment(Qt.AlignTop)
        self.groupBox = QGroupBox("Giocatori")
        self.listPlayersButton = []

        #Add all players on the scroll list
        self.listaG.sort(key=operator.attrgetter('fv'),reverse=True)
        for i in range(len(listaG)):
            self.listPlayersButton.append(QPushButton(self.listaG[i].nome + '    (' +self.listaG[i].squadra[:3] +')          FM: '+str(self.listaG[i].fv)))
            self.listPlayersButton[i].setFixedHeight(35)
            self.listPlayersButton[i].clicked.connect(partial(self.showInfoPlayer,self.listaG[i]))
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
        self.stackUIGiocatori()

        self.layoutCentral=QHBoxLayout()
        self.layoutCentral.addWidget(self.stack)
        self.groupBoxCentral=QGroupBox()
        self.groupBoxCentral.setFixedWidth(700)
        self.groupBoxCentral.setFixedHeight(800)
        self.groupBoxCentral.setLayout(self.layoutCentral)


        self.stack.addWidget(self.stackBase)
        self.stack.addWidget(self.stackPartecipanti)
        self.stack.addWidget(self.stackGiocatori)


        #Window Layout
        layout = QHBoxLayout(self)
        layout.addWidget(self.groupBoxLeft)
        layout.addWidget(self.groupBoxCentral)
        layout.addWidget(self.scroll)

        self.show()

    def showInfoPlayer(self, giocatore):
        self.compraButton.setEnabled(True)
        self.selectedPlayer=giocatore

        self.inputNomeLabel.setText(giocatore.nome)
        self.inputRuoloLabel.setText(self.ruoli[giocatore.ruolo])
        self.inputFmLabel.setText(str(giocatore.fv))
        self.inputMvLabel.setText(str(giocatore.mv))

        self.inputProprietarioLabel.setText(giocatore.partecipante)
        self.inputSquadraLabel.setText(giocatore.squadra)
        self.inputPresenzeLabel.setText(str(int(giocatore.presenze)))



        self.layoutInfoGiocatoriSX.addRow(self.nomeLabel,self.inputNomeLabel)
        self.layoutInfoGiocatoriSX.addRow(self.ruoloLabel,self.inputRuoloLabel)
        self.layoutInfoGiocatoriSX.addRow(self.squadraLabel,self.inputSquadraLabel)
        self.layoutInfoGiocatoriSX.addRow(self.presenzeLabel,self.inputPresenzeLabel)
        self.layoutInfoGiocatoriSX.addRow(self.fmLabel,self.inputFmLabel)
        self.layoutInfoGiocatoriSX.addRow(self.mvLabel,self.inputMvLabel)




        if giocatore.ruolo!="P":
            self.inputGolLabel.setText(str(int(giocatore.gol)))
            self.inputAssistLabel.setText(str(int(giocatore.assist)))
            self.inputRigoriLabel.setText(str(int(giocatore.rigori)))
            self.inputGialliLabel.setText(str(int(giocatore.gialli)))
            self.inputRossiLabel.setText(str(int(giocatore.rossi)))
            self.golLabel.setText('Gol: ')
            self.assistLabel.setText('Assist: ')

            self.layoutInfoGiocatoriDX.addRow(self.golLabel,self.inputGolLabel)
            self.layoutInfoGiocatoriDX.addRow(self.assistLabel,self.inputAssistLabel)


        else:
            self.golLabel.setText('Rigori parati: ')
            self.assistLabel.setText('Gol subiti')
            self.inputAssistLabel.setText(str(int(giocatore.golSubiti)))
            self.inputGolLabel.setText(str(int(giocatore.rigoriParati)))


        self.layoutInfoGiocatoriDX.addRow(self.gialliLabel,self.inputGialliLabel)
        self.layoutInfoGiocatoriDX.addRow(self.rossiLabel,self.inputRossiLabel)
        self.layoutInfoGiocatoriDX.addRow(self.proprietarioLabel,self.inputProprietarioLabel)
        self.stack.setCurrentIndex(2)

    def showPartecipante(self, partecipante):
        self.stack.setCurrentIndex(1)
        self.labelNomePartecipante.setText('Nome:\t'+partecipante.nome)
        self.labelCreditiPartecipante.setText('Crediti rimasti:\t'+str(partecipante.crediti))
        self.labelRimastiPartecipante.setText('Posti disponibili:\t'+str(25-len(partecipante.listaAquisti)))
        img=QPixmap('img/'+partecipante.nome+'.jpg')
        img=img.scaled(250,250,Qt.KeepAspectRatio)
        self.imagePartecipante.setPixmap(img)
        portieri=[]
        difensori=[]
        centrocampisti=[]
        attaccanti=[]

        for i in range(8):
            for j in range(4):
                self.tableGiocatori.setItem(i+1,j,QTableWidgetItem(''))

        for i in partecipante.listaAquisti:
            if i.ruolo=='P':
                portieri.append(i)

        portieri.sort(key=operator.attrgetter('costo'),reverse=True)
        for i in range(len(portieri)):
            item=QTableWidgetItem(portieri[i].nome+ ' ('+str(portieri[i].costo)+')')
            item.setTextAlignment(Qt.AlignCenter)
            self.tableGiocatori.setItem(i+1,0,item)

        for i in partecipante.listaAquisti:
            if i.ruolo=='D':
                difensori.append(i)
        difensori.sort(key=operator.attrgetter('costo'),reverse=True)
        for i in range(len(difensori)):
            item=QTableWidgetItem(difensori[i].nome+ ' ('+str(difensori[i].costo)+')')
            item.setTextAlignment(Qt.AlignCenter)
            self.tableGiocatori.setItem(i+1,1,item)

        for i in partecipante.listaAquisti:
            if i.ruolo=='C':
                centrocampisti.append(i)
        centrocampisti.sort(key=operator.attrgetter('costo'),reverse=True)
        for i in range(len(centrocampisti)):
            item=QTableWidgetItem(centrocampisti[i].nome+ ' ('+str(centrocampisti[i].costo)+')')
            item.setTextAlignment(Qt.AlignCenter)
            self.tableGiocatori.setItem(i+1,2,item)

        for i in partecipante.listaAquisti:
            if i.ruolo=='A':
                attaccanti.append(i)
        attaccanti.sort(key=operator.attrgetter('costo'),reverse=True)
        for i in range(len(attaccanti)):
            item=QTableWidgetItem(attaccanti[i].nome+ ' ('+str(attaccanti[i].costo)+')')
            item.setTextAlignment(Qt.AlignCenter)
            self.tableGiocatori.setItem(i+1,3,item)


    def stackUIGiocatori(self):
        layoutBaseGiocatori=QVBoxLayout()
        layoutInfoGiocatori=QHBoxLayout()
        self.layoutInfoGiocatoriSX=QFormLayout()
        self.layoutInfoGiocatoriDX=QFormLayout()
        layoutCompraGiocatori=QFormLayout()

        indietroButton1=QPushButton('Indietro')
        indietroButton1.clicked.connect(self.back)
        indietroButton1.setMinimumHeight(53)

        self.nomeLabel=QLabel('Nome:')
        self.nomeLabel.setAlignment(Qt.AlignLeft)
        self.ruoloLabel=QLabel('Ruolo:')
        self.squadraLabel=QLabel('Squadra:')
        self.presenzeLabel=QLabel('Presenze:')
        self.fmLabel=QLabel('FantaMedia:')
        self.mvLabel=QLabel('Media voto:')
        self.golLabel=QLabel('Gol:')
        self.assistLabel=QLabel('Assist:')
        self.gialliLabel=QLabel('Gialli:')
        self.rossiLabel=QLabel('Rossi')
        self.subitiLabel=QLabel('Gol subiti:')
        self.rigoriParatiLabel=QLabel('Rigori parati:')
        self.rigoriLabel=QLabel('Rigori calciati:')
        self.proprietarioLabel=QLabel('Proprietario:')

        self.inputNomeLabel=QLabel()
        self.inputRuoloLabel=QLabel()
        self.inputSquadraLabel=QLabel()
        self.inputPresenzeLabel=QLabel()
        self.inputFmLabel=QLabel()
        self.inputMvLabel=QLabel()
        self.inputGolLabel=QLabel()
        self.inputAssistLabel=QLabel()
        self.inputGialliLabel=QLabel()
        self.inputRossiLabel=QLabel()
        self.inputSubitiLabel=QLabel()
        self.inputRigoriParatiLabel=QLabel()
        self.inputRigoriLabel=QLabel()
        self.inputProprietarioLabel=QLabel()


        boxAcquisto=QGroupBox('Acquisto giocatore')
        boxAcquisto.setLayout(layoutCompraGiocatori)

        labelAcquirente=QLabel('Proprietario')
        labelCosto=QLabel('Costo')
        self.comboAcquirente=QComboBox(self)
        self.comboAcquirente.setMinimumWidth(450)
        self.comboAcquirente.addItem('')
        for i in range(len(self.listaP)):
            self.comboAcquirente.addItem(self.listaP[i].nome)

        self.inputCosto=QLineEdit(self)

        verticalSpacerSuper=QSpacerItem(20,20,QSizePolicy.Minimum,QSizePolicy.Minimum)
        layoutCompraGiocatori.addItem(verticalSpacerSuper)
        layoutCompraGiocatori.addRow(labelAcquirente,self.comboAcquirente)
        verticalSpacerHigh=QSpacerItem(20,20,QSizePolicy.Minimum,QSizePolicy.Minimum)
        layoutCompraGiocatori.addItem(verticalSpacerHigh)
        layoutCompraGiocatori.addRow(labelCosto,self.inputCosto)

        self.compraButton=QPushButton('Acquista giocatore')
        self.compraButton.clicked.connect(self.acquisto)
        self.compraButton.setMinimumSize(100,40)
        verticalSpacerMedium=QSpacerItem(20,50,QSizePolicy.Minimum,QSizePolicy.Minimum)
        layoutCompraGiocatori.addItem(verticalSpacerMedium)
        layoutCompraGiocatori.addWidget(self.compraButton)


        self.layoutInfoGiocatoriSX.setAlignment(Qt.AlignLeft)
        self.layoutInfoGiocatoriDX.setAlignment(Qt.AlignLeft)


        layoutInfoGiocatori.addLayout(self.layoutInfoGiocatoriSX)
        layoutInfoGiocatori.addLayout(self.layoutInfoGiocatoriDX)
        layoutBaseGiocatori.addLayout(layoutInfoGiocatori)
        layoutBaseGiocatori.addWidget(boxAcquisto)
        verticalSpacerLow=QSpacerItem(20,100,QSizePolicy.Minimum,QSizePolicy.Minimum)
        layoutBaseGiocatori.addItem(verticalSpacerLow)
        layoutBaseGiocatori.addWidget(indietroButton1)
        self.stackGiocatori.setLayout(layoutBaseGiocatori)




    def stackUIbase(self):
        self.layoutBaseVertical=QVBoxLayout()
        self.groupBaseVertical=QGroupBox()
        self.layoutBaseHorizontal=QFormLayout()
        icon=QPixmap('logo.png')
        icon=icon.scaled(474,214,Qt.KeepAspectRatio)
        logo=QLabel()
        logo.setAlignment(Qt.AlignCenter)
        logo.setPixmap(icon)

        self.layoutBaseVertical.addWidget(logo)

        self.layoutBaseVertical.addWidget(self.groupBaseVertical)
        self.groupBaseVertical.setLayout(self.layoutBaseHorizontal)
        self.inputNome=QLineEdit(self)
        self.inputSquadra=QLineEdit(self)
        self.inputFM=QLineEdit(self)
        self.inputRuolo=QComboBox(self)



        self.inputRuolo.addItem('Tutti')
        self.inputRuolo.addItem('Portiere')
        self.inputRuolo.addItem('Difensore')
        self.inputRuolo.addItem('Centrocampista')
        self.inputRuolo.addItem('Attaccante')

        self.inputNome.setMinimumWidth(450)
        self.inputSquadra.setMinimumWidth(450)
        self.inputFM.setMinimumWidth(450)
        self.inputRuolo.setMinimumWidth(450)


        self.labelNome=QLabel('Nome')
        self.labelSquadra=QLabel('Squadra')
        self.labelFM=QLabel('FantaMedia')
        self.labelRuolo=QLabel('Ruolo')
        self.labelFM.setMinimumWidth(140)
        self.labelSquadra.setMinimumWidth(140)
        self.labelNome.setMinimumWidth(140)
        self.labelRuolo.setMinimumWidth(140)

        self.layoutBaseHorizontal.addRow(self.labelNome,self.inputNome)
        self.layoutBaseHorizontal.addRow(self.labelRuolo,self.inputRuolo)
        self.layoutBaseHorizontal.addRow(self.labelSquadra,self.inputSquadra)
        self.layoutBaseHorizontal.addRow(self.labelFM,self.inputFM)

        self.groupBaseVertical.setFixedHeight(300)

        self.buttonCerca=QPushButton('Cerca')
        self.buttonCerca.clicked.connect(self.cerca)
        verticalSpacer=QSpacerItem(20,70,QSizePolicy.Minimum,QSizePolicy.Minimum)
        self.layoutBaseVertical.addItem(verticalSpacer)
        self.layoutBaseVertical.addWidget(self.buttonCerca)


        self.stackBase.setLayout(self.layoutBaseVertical)


    def stackUIPartecipanti(self):
        layoutPartecipanti=QVBoxLayout()
        layoutAlto=QHBoxLayout()
        layoutBasso=QHBoxLayout()
        layoutAltoDati=QVBoxLayout()
        self.tableGiocatori=QTableWidget()
        self.tableGiocatori.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableGiocatori.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableGiocatori.setRowCount(9)
        self.tableGiocatori.setColumnCount(4)
        p=QTableWidgetItem('Portieri')
        d=QTableWidgetItem('Difensori')
        c=QTableWidgetItem('Centrocampisti')
        a=QTableWidgetItem('Attaccanti')
        font=QFont()
        font.setBold(True)

        self.indietroButton=QPushButton('Indietro')
        self.indietroButton.clicked.connect(self.back)
        self.indietroButton.setMinimumHeight(53)

        p.setTextAlignment(Qt.AlignCenter)
        d.setTextAlignment(Qt.AlignCenter)
        c.setTextAlignment(Qt.AlignCenter)
        a.setTextAlignment(Qt.AlignCenter)

        self.tableGiocatori.setItem(0,0,p)
        self.tableGiocatori.setItem(0,1,d)
        self.tableGiocatori.setItem(0,2,c)
        self.tableGiocatori.setItem(0,3,a)
        self.tableGiocatori.item(0,0).setFont(font)
        self.tableGiocatori.item(0,1).setFont(font)
        self.tableGiocatori.item(0,2).setFont(font)
        self.tableGiocatori.item(0,3).setFont(font)

        self.tableGiocatori.verticalHeader().setVisible(False)
        self.tableGiocatori.horizontalHeader().setVisible(False)


        header=self.tableGiocatori.horizontalHeader()
        header.setSectionResizeMode(0,QHeaderView.Stretch)
        header.setSectionResizeMode(1,QHeaderView.Stretch)
        header.setSectionResizeMode(2,QHeaderView.Stretch)
        header.setSectionResizeMode(3,QHeaderView.Stretch)

        self.labelNomePartecipante=QLabel()
        self.labelCreditiPartecipante=QLabel()
        self.labelRimastiPartecipante=QLabel()
        self.imagePartecipante=QLabel()

        layoutAltoDati.addWidget(self.labelNomePartecipante)
        layoutAltoDati.addWidget(self.labelCreditiPartecipante)
        layoutAltoDati.addWidget(self.labelRimastiPartecipante)

        layoutAlto.addWidget(self.imagePartecipante)
        layoutAlto.addLayout(layoutAltoDati)
        layoutBasso.addWidget(self.tableGiocatori)

        layoutPartecipanti.addLayout(layoutAlto)
        verticalSpacer1=QSpacerItem(20,70,QSizePolicy.Minimum,QSizePolicy.Minimum)
        layoutPartecipanti.addItem(verticalSpacer1)
        layoutPartecipanti.addLayout(layoutBasso)
        verticalSpacer2=QSpacerItem(20,90,QSizePolicy.Minimum,QSizePolicy.Minimum)

        layoutPartecipanti.addItem(verticalSpacer2)
        layoutPartecipanti.addWidget(self.indietroButton)

        self.stackPartecipanti.setLayout(layoutPartecipanti)

    def back(self):
        self.stack.setCurrentIndex(0)
        self.inputFM.setText('')
        self.inputNome.setText('')
        self.inputSquadra.setText('')


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

        #Select the filtered players
        for i in range(len(self.listaG)):
            if self.listaG[i].nome.startswith(self.inputNome.text().upper())==True and self.listaG[i].venduto==False and (self.inputRuolo.currentText()==self.ruoli[self.listaG[i].ruolo] or  self.inputRuolo.currentText()=='Tutti') and self.listaG[i].squadra.startswith(self.inputSquadra.text().title())==True and float(self.listaG[i].fv)>=float(inp):
                self.listPLayersParziale.append(QPushButton(self.listaG[i].nome + '    (' +self.listaG[i].squadra[:3] +')          FM: '+str(self.listaG[i].fv)))
                tmpList.append(self.listaG[i])

        #Add the correct players to the scroll list
        for i in range(len(self.listPLayersParziale)):
            self.listPLayersParziale[i].setFixedHeight(35)
            self.listPLayersParziale[i].clicked.connect(partial(self.showInfoPlayer, tmpList[i]))
            self.scrollLayout.addWidget(self.listPLayersParziale[i])


    def acquisto(self):
        try:
            int(self.inputCosto.text())
        except (ValueError,TypeError):
            intError=QMessageBox()
            intError.setWindowTitle('Error')
            intError.setText('Attenzione - Inserire un numero intero come costo!')
            intError.setIcon(QMessageBox.Critical)
            intError.setStandardButtons(QMessageBox.Close)
            intError.setDefaultButton(QMessageBox.Close)
            x=intError.exec()
            return

        if int(self.inputCosto.text())>476 or int(self.inputCosto.text())<=0:
            costoError=QMessageBox()
            costoError.setWindowTitle('Error')
            costoError.setText('Attenzione - Formato costo non accettabile!')
            costoError.setIcon(QMessageBox.Critical)
            costoError.setStandardButtons(QMessageBox.Close)
            costoError.setDefaultButton(QMessageBox.Close)
            x=costoError.exec()
            return


        if (self.comboAcquirente.currentText()!=''):
            self.selectedPlayer.venduto=True
            for i in range(len(self.listaP)):
                if self.listaP[i].nome==self.comboAcquirente.currentText():
                    if self.listaP[i].numeroRuolo(self.selectedPlayer.ruolo)<self.disp[self.selectedPlayer.ruolo]:
                        if len(self.listaP[i].listaAquisti)<25:
                            checkMsg=QMessageBox()
                            checkMsg.setWindowTitle('Error')
                            checkMsg.setText("Confermi l'acquisto di "+self.selectedPlayer.nome +' da parte di '+self.listaP[i].nome+'?')
                            checkMsg.setIcon(QMessageBox.Question)
                            checkMsg.setStandardButtons(QMessageBox.No|QMessageBox.Yes)
                            checkMsg.setDefaultButton(QMessageBox.Yes)
                            result=checkMsg.exec()

                            if result==QMessageBox.No:
                                return



                            self.selectedPlayer.costo=int(self.inputCosto.text())
                            self.listaP[i].addPlayer(self.selectedPlayer,int(self.inputCosto.text()))
                            completeMsg=QMessageBox()
                            completeMsg.setWindowTitle('Success')
                            completeMsg.setText('Aquisto effettuato!\n'+self.listaP[i].nome+' ha acquistato '+self.selectedPlayer.nome)
                            icon=QPixmap('success.png')
                            icon.scaled(100,100,Qt.KeepAspectRatio)
                            completeMsg.setIconPixmap(icon)
                            completeMsg.setStandardButtons(QMessageBox.Close)
                            completeMsg.setDefaultButton(QMessageBox.Close)

                            x=completeMsg.exec()
                            self.cerca()
                            self.inputFM.setText('')
                            self.compraButton.setEnabled(False)
                            self.comboAcquirente.setCurrentText('')
                            self.inputCosto.setText('')
                            self.inputProprietarioLabel.setText(self.listaP[i].nome)
                        else:
                            errorMsg=QMessageBox()
                            errorMsg.setWindowTitle('Error')
                            errorMsg.setText('Attenzione - Limite acquisti raggiunto!')
                            errorMsg.setIcon(QMessageBox.Critical)
                            errorMsg.setStandardButtons(QMessageBox.Close)
                            errorMsg.setDefaultButton(QMessageBox.Close)
                            x=errorMsg.exec()
                            return
                    else:
                        errorMsg=QMessageBox()
                        errorMsg.setWindowTitle('Error')
                        r=str(self.ruoli[self.selectedPlayer.ruolo]).lower()
                        r1=list(r)
                        r1[-1]='i'
                        r="".join(r1)
                        errorMsg.setText('Attenzione - Limite numero di '+r)
                        errorMsg.setIcon(QMessageBox.Critical)
                        errorMsg.setStandardButtons(QMessageBox.Close)
                        errorMsg.setDefaultButton(QMessageBox.Close)
                        x=errorMsg.exec()
                        return
        else:
            errorMsg=QMessageBox()
            errorMsg.setWindowTitle('Error')
            errorMsg.setText('Attenzione - Selezionare un acquirente!')
            errorMsg.setIcon(QMessageBox.Critical)
            errorMsg.setStandardButtons(QMessageBox.Close)
            errorMsg.setDefaultButton(QMessageBox.Close)
            x=errorMsg.exec()
            return
