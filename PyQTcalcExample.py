# This is a simple calculator example using PyQt6 and Python 3.10

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QGridLayout


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(300, 300)
        self.generalLayout = QVBoxLayout()
        self._createDisplay()
        self._createButtons()
        self.setLayout(self.generalLayout)

    def _createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)

    # use QgridLayout to create a grid of buttons
    def _createButtons(self):
        self.buttons = {}
        buttonsLayout = QGridLayout()
        buttons = {
            "7": (0, 0),
            "8": (0, 1),
            "9": (0, 2),
            "/": (0, 3),
            "C": (0, 4),
            "4": (1, 0),
            "5": (1, 1),
            "6": (1, 2),
            "*": (1, 3),
            "(": (1, 4),
            "1": (2, 0),
            "2": (2, 1),
            "3": (2, 2),
            "-": (2, 3),
            ")": (2, 4),
            "0": (3, 0),
            "00": (3, 1),
            ".": (3, 2),
            "+": (3, 3),
            "=": (3, 4),
        }
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40, 40)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        self.generalLayout.addLayout(buttonsLayout)

        # connect buttons to events
        self.buttons["1"].clicked.connect(self._addDigit)
        self.buttons["2"].clicked.connect(self._addDigit)
        self.buttons["3"].clicked.connect(self._addDigit)
        self.buttons["4"].clicked.connect(self._addDigit)
        self.buttons["5"].clicked.connect(self._addDigit)
        self.buttons["6"].clicked.connect(self._addDigit)
        self.buttons["7"].clicked.connect(self._addDigit)
        self.buttons["8"].clicked.connect(self._addDigit)
        self.buttons["9"].clicked.connect(self._addDigit)
        self.buttons["0"].clicked.connect(self._addDigit)
        self.buttons["00"].clicked.connect(self._addDigit)
        self.buttons["."].clicked.connect(self._addDigit)
        self.buttons["/"].clicked.connect(self._addDigit)
        self.buttons["*"].clicked.connect(self._addDigit)
        self.buttons["-"].clicked.connect(self._addDigit)
        self.buttons["+"].clicked.connect(self._addDigit)
        self.buttons["("].clicked.connect(self._addDigit)
        self.buttons[")"].clicked.connect(self._addDigit)
        self.buttons["C"].clicked.connect(self._clearDisplay)
        self.buttons["="].clicked.connect(self._calculateResult)

    def _addDigit(self):
        button = self.sender()
        digitValue = button.text()
        self.display.setText(self.display.text() + digitValue)

    def _clearDisplay(self):
        self.display.clear()

    def _calculateResult(self):
        result = eval(self.display.text())
        self.display.setText(str(result))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec())
