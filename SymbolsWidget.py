from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QScrollArea, QHBoxLayout
from sympy import symbols

from ExpressionWidget import ExpressionWidget


class SymbolsWidget(QScrollArea):
    def __init__(self, parent=None):
        super(SymbolsWidget, self).__init__(parent)
        self.setFixedHeight(120)
        self.setWidgetResizable(True)
        self.widget_ = QWidget(self)
        layout = QHBoxLayout(self.widget_)
        self.contentLayout = QHBoxLayout(self.widget_)
        layout.addLayout(self.contentLayout)
        layout.addStretch()
        self.widget_.setLayout(layout)
        self.setWidget(self.widget_)
        self.symbolWidgets = []

    @classmethod
    def getSymbol(cls, index):
        return symbols(chr(ord('x') + index))

    def setSymbolsCount(self, count):
        if count == 0:
            self.hide()
            return
        for i in range(count, len(self.symbolWidgets)):
            symbolWidget = self.symbolWidgets[i]
            self.contentLayout.removeWidget(symbolWidget)
            symbolWidget.deleteLater()
        self.symbolWidgets = self.symbolWidgets[:count]
        for i in range(len(self.symbolWidgets), count):
            symbolWidget = ExpressionWidget(self)
            symbolWidget.setExpression(self.getSymbol(i))
            self.symbolWidgets.append(symbolWidget)
            self.contentLayout.addWidget(symbolWidget, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.show()
