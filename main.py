# -*- coding: utf-8 -*-
import logging
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
import sys
from logging.handlers import TimedRotatingFileHandler
import time

getCodeListBtn = ''
codeNameList = []
perList = []


class StockStart(QWidget):
    def __init__(self):
        super().__init__()
        self.start()

    def start(self):
        global getCodeListBtn

    def start(self):
        global getCodeListBtn

        self.setWindowTitle('Kiwoom Stock Investment')
        self.setFixedSize(400, 250)
        self.setFocusPolicy(Qt.StrongFocus)

        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")

        self.kiwoom.OnReceiveTrData.connect(self.receive_trdata)

        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        getCodeListBtn = QtWidgets.QPushButton('Get Code List')
        layout.addWidget(getCodeListBtn)

        self.setLayout(layout)
        self.show()

        self.kiwoom.OnEventConnect.connect(self.checkStatus)

    def checkStatus(self, err_code):
        global getCodeListBtn

        if err_code == 0:
            getCodeListBtn.clicked.connect(self.getCodeList)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = StockStart()
    myWindow.show()
    app.exec_()
