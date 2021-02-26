import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QFrame, QMainWindow
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QPainter, QColor
from random import randint
from UI import Ui_Frame


class MyWidget(QMainWindow, Ui_Frame):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.t = False
        self.r = []
        self.pushButton.clicked.connect(self.run)
        self.show()

    def run(self):
        self.t = True
        self.update()
    
    def paintEvent(self, event):
        if self.t:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
        
    def draw(self, qp):
        x = randint(0, 100)
        self.r.append([QColor(randint(0, 255), randint(0, 255), randint(0, 255)), randint(0, 380), randint(0, 320), x, x])
        for i in self.r:
            qp.setBrush(i[0])
            s = i[1:]
            qp.drawEllipse(*s)
        self.t = False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())