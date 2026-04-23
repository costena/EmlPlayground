from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QScrollArea, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QSizePolicy, QFrame
from sympy import symbols
from sympy.core.numbers import One

from Eml import eml
from ExpressionWidget import ExpressionWidget


class InventoryWidget(QScrollArea):
    def __init__(self, parent=None):
        super(InventoryWidget, self).__init__(parent)
        self.setWidgetResizable(True)
        self.widget_ = QWidget()
        layout = QVBoxLayout(self.widget_)
        self.contentLayout = QVBoxLayout(self.widget_)
        layout.addLayout(self.contentLayout)
        layout.addStretch()
        self.widget_.setLayout(layout)
        self.setWidget(self.widget_)
        self.expressions = set()
        self.initExpressionWidgets()

    def initExpressionWidgets(self):
        self.addExpression(One())
        x, y = symbols("x, y")
        self.addExpression(eml(x, y))

    def addExpression(self, expression):
        if expression in self.expressions:
            return
        self.expressions.add(expression)
        expressionWidget = ExpressionWidget(self)
        expressionWidget.setExpression(expression)
        self.addExpressionWidget(expressionWidget)

    def addExpressionWidget(self, expressionWidget):
        self.contentLayout.addWidget(expressionWidget, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
