from PyQt6.QtWidgets import QWidget, QSplitter, QVBoxLayout

from Archive import Archive
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
        self.inventoryWidget = InventoryWidget(self)
        self.splitter.addWidget(self.inventoryWidget)
        self.synthesis = SynthesisWidget(self)
        self.synthesis.SIGNAL_EXPRESSION_FOUND.connect(self.onExpressionFound)
        self.splitter.addWidget(self.synthesis)
        layout.addWidget(self.splitter)
        self.setLayout(layout)
        self.archive = Archive()
        self.archive.load(self.inventoryWidget, self.taskWidget)

    def onExpressionFound(self, expression):
        self.inventoryWidget.addExpression(expression)
        self.taskWidget.onExpressionFound(expression)
        self.dump()

    def dump(self):
        self.archive.dump(self.inventoryWidget, self.taskWidget)
