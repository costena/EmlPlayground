from PyQt6.QtWidgets import QWidget, QSplitter, QVBoxLayout

from InventoryWidget import InventoryWidget
from SynthesisWidget import SynthesisWidget
from TaskWidget import TaskWidget


class EmlPlaygroundWidget(QWidget):
    def __init__(self, parent=None):
        super(EmlPlaygroundWidget, self).__init__(parent)
        layout = QVBoxLayout(self)
        self.taskWidget = TaskWidget(self)
        layout.addWidget(self.taskWidget)
        self.splitter = QSplitter(self)
        self.inventory = InventoryWidget(self)
        self.splitter.addWidget(self.inventory)
        self.synthesis = SynthesisWidget(self)
        self.synthesis.SIGNAL_EXPRESSION_FOUND.connect(self.onExpressionFound)
        self.splitter.addWidget(self.synthesis)
        layout.addWidget(self.splitter)
        self.setLayout(layout)

    def onExpressionFound(self, expression):
        self.inventory.addExpression(expression)
        self.taskWidget.onExpressionFound(expression)
