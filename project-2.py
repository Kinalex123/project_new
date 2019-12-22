# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtCore import Qt

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)
    
    
class MyWindow(QtWidgets, QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Project1.ui', self)
        self.pushButton.clicked.connect(self.show_answer)
        
    def show_answer(self):
        self.cost = int(self.text_cena.text())
        self.discount = int(self.text_skidka.text())
        self.text_itog.setPlainText(str(self.cost * (100 -(self.discount)) / 100))   
        
sys.excepthook = except_hook
        
app = QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_)