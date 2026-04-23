import io
import pickle

from PyQt6.QtCore import Qt, QMimeData, pyqtSignal
from PyQt6.QtGui import QDrag, QPixmap
from PyQt6.QtWidgets import QLabel, QHBoxLayout, QFrame
from sympy import latex
from sympy.physics.control.control_plots import plt

from ExpressionSlotWidget import ExpressionSlotWidget


class ExpressionWidget(QFrame):
    SIGNAL_MODIFIED = pyqtSignal()
    SIGNAL_DELETE_REQUESTED = pyqtSignal()

    def __init__(self, parent=None):
        super(ExpressionWidget, self).__init__(parent)
        self.interactable = False
        self.expression = None
        self.layout_ = QHBoxLayout(self)
        self.label = QLabel(self)
        self.layout_.addWidget(self.label)
        self.setLayout(self.layout_)
        self.argWidgets = []
        self.expressionSlotWidgets = {}

    def setExpression(self, expression):
        self.expression = expression
        self.refresh()

    def setInteractable(self, interactable):
        self.interactable = interactable
        self.refresh()

    @classmethod
    def latexToPixmap(cls, latex, fontSize=8, dpi=100):
        from LatexRenderer import latexRenderer
        return latexRenderer.latexToPixmap(latex, fontSize, dpi)

    def refresh(self):
        try:
            self.label.setPixmap(self.latexToPixmap(latex(self.expression), self.font().pointSize()))
        except:
            self.label.setText(str(self.expression))
        if self.expression.is_Symbol:
            symbolCount = -1
        else:
            symbolCount = len(self.expression.free_symbols)
        self.setProperty("symbolCount", symbolCount)
        self.clearArgWidgets()
        if symbolCount == 0 or not self.interactable:
            return
        self.addArgWidget(QLabel("|"))
        for symbol in sorted(self.expression.free_symbols, key=lambda x: x.name):
            label = QLabel(self)
            label.setPixmap(self.latexToPixmap(latex(symbol) + "=", self.font().pointSize()))
            self.addArgWidget(label)
            self.addExpressionSlotWidget(symbol, ExpressionSlotWidget(self))

    def clearArgWidgets(self):
        for widget in self.argWidgets:
            self.layout_.removeWidget(widget)
            widget.deleteLater()
        self.argWidgets.clear()
        self.expressionSlotWidgets.clear()

    def addExpressionSlotWidget(self, arg, expressionSlotWidget):
        self.expressionSlotWidgets[arg] = expressionSlotWidget
        self.addArgWidget(expressionSlotWidget)
        expressionSlotWidget.SIGNAL_MODIFIED.connect(self.SIGNAL_MODIFIED)

    def addArgWidget(self, widget):
        self.argWidgets.append(widget)
        self.layout_.addWidget(widget, alignment=Qt.AlignmentFlag.AlignCenter)

    def mouseMoveEvent(self, event):
        super(ExpressionWidget, self).mouseMoveEvent(event)
        if event.buttons() == Qt.MouseButton.LeftButton:
            drag = QDrag(self)
            mimeData = QMimeData()
            mimeData.setData("Expression", pickle.dumps(self.expression))
            drag.setMimeData(mimeData)
            pixmap = self.grab()
            drag.setPixmap(pixmap)
            hotSpot = event.pos() - self.rect().topLeft()
            drag.setHotSpot(hotSpot)
            drag.exec(Qt.DropAction.MoveAction)

    def isAllFilled(self):
        for widget in self.expressionSlotWidgets.values():
            if not widget.isAllFilled():
                return False
        return True

    def evaluate(self):
        args = {}
        for arg, expressionSlotWidget in self.expressionSlotWidgets.items():
            args[arg] = expressionSlotWidget.evaluate()
        return self.expression.subs(args)

    def getFreeSymbols(self):
        return self.expression.free_symbols

    def iterateExpressionWidgetsRecursively(self, callback):
        for expressionSlotWidget in self.expressionSlotWidgets.values():
            if not expressionSlotWidget.iterateExpressionWidgetsRecursively(callback):
                return False
        return True

    def mousePressEvent(self, event):
        if event.buttons() == Qt.MouseButton.RightButton:
            self.SIGNAL_DELETE_REQUESTED.emit()
