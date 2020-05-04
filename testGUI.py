# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../fantApp/x.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import *
from PyQt5.QtWidgets import *

class Window1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitWindow1()

    def InitWindow1(self):
        self.button=QPushButton(self)
        self.button.setText('Ok')
        self.button.move(200,200)
        self.button.clicked.connect(self.continue2)
        self.setGeometry(100,100,1000,1300)
        self.show()

    def continue2(self):
        self.close()
        self.next=Window2()

class Window2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title="Cazzo"

        self.initWindow()

    def initWindow(self):
        self.button=QPushButton(self)
        self.button.setText('Next')
        self.button.move(100,400)
        self.button.clicked.connect(self.ok)
        self.setGeometry(100,100,1000,1300)


        self.setWindowTitle(self.title)
        self.show()

    def ok(self):
        print('close clicked')
        self.close()
        self.origin=Window1()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Window1()

    #MainWindow.show()
    sys.exit(app.exec_())
