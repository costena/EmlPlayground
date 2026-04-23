import pickle

from PyQt6.QtCore import pyqtSignal, Qt, QSize
from PyQt6.QtWidgets import QFrame, QHBoxLayout, QSizePolicy


class ExpressionSlotWidget(QFrame):
    SIGNAL_MODIFIED = pyqtSignal()

    def __init__(self, parent=None):
        super(ExpressionSlotWidget, self).__init__(parent)
        self.setMinimumSize(40, 40)
        self.setAcceptDrops(True)
        self.layout_ = QHBoxLayout(self)
        self.layout_.setContentsMargins(0, 0, 0, 0)
        self.expressionWidget = None
        self.setLayout(self.layout_)

    def dragEnterEvent(self, event):
        mimeData = event.mimeData()
        if mimeData.hasFormat("Expression"):
            event.accept()

    def dropEvent(self, event):
        mimeData = event.mimeData()
        if not mimeData.hasFormat("Expression"):
            return
        expression = pickle.loads(mimeData.data("Expression"))
        from ExpressionWidget import ExpressionWidget
        expressionWidget = ExpressionWidget(self)
        expressionWidget.setExpression(expression)
        if not expression.is_Symbol:
            expressionWidget.setInteractable(True)
        self.setExpressionWidget(expressionWidget)

    def setExpressionWidget(self, expressionWidget):
        if self.expressionWidget is not None:
            self.layout_.removeWidget(self.expressionWidget)
            self.expressionWidget.deleteLater()
        self.expressionWidget = expressionWidget
        if self.expressionWidget is not None:
            self.layout_.addWidget(self.expressionWidget)
            self.expressionWidget.SIGNAL_MODIFIED.connect(self.SIGNAL_MODIFIED)
            self.expressionWidget.SIGNAL_DELETE_REQUESTED.connect(lambda: self.setExpressionWidget(None))
        self.SIGNAL_MODIFIED.emit()

    def isAllFilled(self):
        if self.expressionWidget is None:
            return False
        return self.expressionWidget.isAllFilled()

    def evaluate(self):
        if self.expressionWidget is None:
            return None
        return self.expressionWidget.evaluate()

    def iterateExpressionWidgetsRecursively(self, callback):
        if not callback(self, self.expressionWidget):
            return True
        if self.expressionWidget is not None:
            return self.expressionWidget.iterateExpressionWidgetsRecursively(callback)
        return True
