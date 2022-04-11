import sys
from PyQt6.QtCore import Qt
from PyQt6 import QtWidgets
from PyQt6.QtGui import QIcon
import main_window
import os
import sys
from core import *


class MyMainWindow(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.convertButton.clicked.connect(self.execute_conversion)
        self.clearButton.clicked.connect(self.reset_clicked)
        self.setWindowIcon(QIcon("qt-logo.svg"))

    def execute_conversion(self):
        s = self.expressionEdit.toPlainText()
        res = " ".join(solve(str_to_symbols(s)))
        print(f"Your expression in postfix notation:\n {res}")

    def reset_clicked(self):
        self.expressionEdit.setText("")


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
