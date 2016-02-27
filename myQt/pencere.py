import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * #QSize, QPoint
from PyQt5.QtGui import * #QIcon, QPixmap


class myWin(QWidget):

    uygulama = QApplication(sys.argv)

    def __int__(self):
        super().__int__()
        self.myWinApp()

    def myWinApp(self):
        return self

    #########################################################
    # SET METHODS
    #########################################################

    def winResize(self, en=640, boy=480):
        self.resize(QSize(en, boy))
        return self

    def winMove(self, x=300, y=300):
        self.move(QPoint(x, y))
        return self

    def winTitle(self, str='Form Name'):
        self.setWindowTitle(str)
        return self

    def winIcon(self,imgPath = None):
        if imgPath is None or os.path.exists(imgPath) != True or os.access(imgPath, os.R_OK):
            return self
        self.setWindowIcon(QIcon(imgPath))
        return self

    #########################################################
    # GET METHODS
    #########################################################

    def getWinResize(self, out='a'):
        if out == 'w' or out == 'width':
            return self.width()
        elif out == 'h' or out == 'height':
            return self.height()

        return [self.width(), self.height()]

    def getWinMove(self, out='a'):
        if out == 'x' or out == 'horizontal':
            return self.x()
        elif out == 'y' or out == 'vertical':
            return self.y()

        return [self.x(), self.y()]

    #########################################################
    # VİEWER METHODS
    #########################################################

    def winHeadText(self, str=''):
        QLabel('<p style="font-size: 22px">'+str+'</p>', self)
        return self

    #########################################################
    # EVENTS METHODS
    #########################################################

    def winShow(self):
        #before trigger
        self.show();
        #after trigger
        myWin.uygulama.exec_()
        return self

    def winClose(self):
        #before tirgger
        self.close()
        #after trigger
        return self