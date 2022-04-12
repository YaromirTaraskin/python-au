import sys

from PyQt6 import QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMessageBox

import main_window
from core import *


class MyResultWindow(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon("qt-logo.svg"))


class MyMainWindow(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.convertButton.clicked.connect(self.execute_conversion)
        self.clearButton.clicked.connect(self.reset_clicked)
        self.convertButton.setEnabled(False)
        self.expressionEdit.textChanged.connect(self.post_text_changed)
        self.setWindowIcon(QIcon("qt-logo.svg"))

    def post_text_changed(self):
        if self.expressionEdit.toPlainText() == "":
            self.convertButton.setEnabled(False)
        else:
            self.convertButton.setEnabled(True)

    def show_conversion_result(self, result):
        result_message_box = QMessageBox(parent=self)
        result_message_box.setFont(self.font())
        result_message_box.setWindowTitle("Result")
        result_message_box.setText("The conversion was made.")
        result_message_box.setInformativeText("Look to the details to see the result.")
        '''result_message_box.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextBrowserInteraction | Qt.TextInteractionFlag.LinksAccessibleByMouse
        )'''
        result_message_box.setIcon(QMessageBox.Icon.Information)
        result_message_box.setStandardButtons(QMessageBox.StandardButton.Close)
        result_message_box.setDetailedText(result)
        result_message_box.exec()

    def show_exception_message_box(self, e):
        exception_message_box = QMessageBox(parent=self)
        exception_message_box.setFont(self.font())
        exception_message_box.setWindowIcon("Error")
        exception_message_box.setText("An error occurred.")
        exception_message_box.setInformativeText("The input was probably invalid. Check it before submitting it.")
        exception_message_box.setDetailedText(e)
        exception_message_box.setIcon(QMessageBox.Icon.Critical)

    def execute_conversion(self):
        try:
            s = self.expressionEdit.toPlainText()
            res = " ".join(solve(str_to_symbols(s)))
            self.show_conversion_result(res)
        except Exception as e:
            self.show_exception_message_box(e)

    def reset_clicked(self):
        self.expressionEdit.clear()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
