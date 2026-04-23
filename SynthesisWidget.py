from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QScrollArea, QSizePolicy
from sympy import expand

from ExpressionSlotWidget import ExpressionSlotWidget
from ExpressionWidget import ExpressionWidget
from SymbolsWidget import SymbolsWidget


class SynthesisWidget(QWidget):
    SIGNAL_EXPRESSION_FOUND = pyqtSignal(object)

    def __init__(self, parent=None):
        super(SynthesisWidget, self).__init__(parent)
        layout = QVBoxLayout(self)
        self.symbolsWidget = SymbolsWidget(self)
        self.symbolsWidget.hide()
        layout.addWidget(self.symbolsWidget)
        layout.addStretch()
        self.expressionSlotWidget = ExpressionSlotWidget(self)
        self.expressionSlotWidget.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        self.expressionSlotWidget.SIGNAL_MODIFIED.connect(self.onExpressionSlotWidgetModified)
        layout.addWidget(self.expressionSlotWidget, alignment=Qt.AlignmentFlag.AlignCenter)
        self.synthesizeButton = QPushButton("Synthesize")
        self.synthesizeButton.setEnabled(False)
        self.synthesizeButton.clicked.connect(self.onSynthesizeButtonClicked)
        layout.addWidget(self.synthesizeButton)
        self.resultExpressionWidget = ExpressionWidget(self)
        layout.addWidget(self.resultExpressionWidget, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch()

    def onExpressionSlotWidgetModified(self):
        allFilled = self.expressionSlotWidget.isAllFilled()
        self.synthesizeButton.setEnabled(allFilled)
        hasEmptySlot = False
        detectedSymbols = set()

        def callback(expressionSlotWidget, expressionWidget):
            if expressionSlotWidget is self.expressionSlotWidget:
                return True
            nonlocal hasEmptySlot
            if expressionWidget is None:
                hasEmptySlot = True
                return True
            expression = expressionWidget.expression
            if expression.is_Symbol:
                detectedSymbols.add(expression)
            return True

        self.expressionSlotWidget.iterateExpressionWidgetsRecursively(callback)
        if not hasEmptySlot:
            self.symbolsWidget.setSymbolsCount(0)
            return
        for i in range(4):
            symbol = self.symbolsWidget.getSymbol(i)
            if symbol not in detectedSymbols:
                self.symbolsWidget.setSymbolsCount(i + 1)
                break

    def onSynthesizeButtonClicked(self):
        expression = self.expressionSlotWidget.evaluate()
        expression = expand(expression, force=True)
        self.resultExpressionWidget.setExpression(expression)
        if expression.is_Symbol:
            return
        self.SIGNAL_EXPRESSION_FOUND.emit(expression)
