# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtCore import Qt


class MyWindow(QtWidgets, QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('Project1.ui', self)

class MainWindow(QMainWindow, MyMainWindow):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.start_cost = 0
        self.sale = 0
        self.end_cost = 0
        self.connect(self.MypushButton, SIGNAL('clicked()'), self.show_answer)
        
    def show_answer(self):
        self.start_cost.input = self.text_cena.toPlainText(self)
        self.sale.input = self.text_skidka.toPlainText(self)
        self.text_itog.SetText(str(self.start_cost / 100 * self.sale))   
        
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.arvg)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
        
def main():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_)