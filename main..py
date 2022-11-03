from PyQt5.QtWidgets import QApplication, QPushButton, QWidget
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
import sys
from random import randint
from UI import Ui_Form


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.draw_btn.clicked.connect(self.run)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_circles(qp)
        qp.end()

    def run(self):
        self.repaint()

    def draw_circles(self, qp):
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        radius = randint(1, 200)
        radius2 = randint(1, 200)
        qp.drawEllipse(QPoint(250, 300), radius, radius)
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        qp.drawEllipse(QPoint(650, 300), radius2, radius2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_widget = MainWindow()
    my_widget.show()
    sys.exit(app.exec())