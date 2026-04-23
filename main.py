import sys

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication

from EmlPlaygroundWidget import EmlPlaygroundWidget


def main():
    app = QApplication(sys.argv)
    app.setFont(QFont('Times', 20))
    app.setApplicationName("Eml Playground")
    with open("style.qss", "r") as f:
        qss = f.read()
        app.setStyleSheet(qss)
    emlPlayground = EmlPlaygroundWidget()
    emlPlayground.show()
    app.exec()


if __name__ == '__main__':
    main()
