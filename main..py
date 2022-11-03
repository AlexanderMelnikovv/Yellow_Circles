from PyQt5.QtWidgets import QApplication, QPushButton, QWidget
import sys
from random import randint
from UI import Ui_Form



class Main_Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.draw_btn.clicked.connect(self.run)

    def run(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_widget = Main_Window()
    my_widget.show()
    sys.exit(app.exec())