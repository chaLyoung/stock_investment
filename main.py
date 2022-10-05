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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = StockStart()
    myWindow.show()
    app.exec_()
