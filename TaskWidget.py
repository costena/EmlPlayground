from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel
from sympy import E, exp, log, latex, symbols, sqrt, cosh, sinh, tanh, cos, sin, tan, asinh, acosh, acos, atanh, asin, \
    atan, simplify
from sympy.core.numbers import One, pi, Zero

from Sigmoid import sigmoid


class TaskWidget(QWidget):
    X, Y = symbols('x, y')
    TASKS = [
        E,
        exp(X),
        log(X),
        Zero(),
        X - Y,
        -One(),
        2 * One(),
        -X,
        X + Y,
        1 / X,
        X * Y,
        X ** 2,
        X / Y,
        X / 2,
        (X + Y) / 2,
        sqrt(X),
        X ** Y,
        log(X, Y),
        pi,
        sqrt(X ** 2 + Y ** 2),
        sigmoid(X),
        cosh(X),
        sinh(X),
        tanh(X),
        cos(X),
        sin(X),
        tan(X),

        asinh(X),
        acosh(X),
        acos(X),
        atanh(X),
        asin(X),
        atan(X),
    ]

    def __init__(self, parent=None):
        super(TaskWidget, self).__init__(parent)
        self.setFixedHeight(120)
        layout = QHBoxLayout(self)
        label = QLabel(self)
        from LatexRenderer import latexRenderer
        label.setPixmap(latexRenderer.latexToPixmap("eml(x, y) = e^x - \log(y)", 40))
        layout.addWidget(label)
        layout.addStretch()
        label = QLabel("Now try to create", self)
        layout.addWidget(label)
        self.currentTaskIndex = 0
        self.taskLabel = QLabel(self)
        self.updateTask()
        layout.addWidget(self.taskLabel)
        layout.addStretch()
        self.setLayout(layout)

    def onExpressionFound(self, expression):
        task = self.TASKS[self.currentTaskIndex]
        if expression == task:
            self.currentTaskIndex += 1
        self.updateTask()

    def updateTask(self):
        from LatexRenderer import latexRenderer
        task = self.TASKS[self.currentTaskIndex]
        try:
            self.taskLabel.setPixmap(latexRenderer.latexToPixmap(latex(task), 40))
        except:
            self.taskLabel.setText(str(task))

    def setCurrentTaskIndex(self, currentTaskIndex):
        self.currentTaskIndex = currentTaskIndex
        self.updateTask()

    def dump(self):
        return {
            'currentTaskIndex': self.currentTaskIndex,
        }

    def load(self, data):
        currentTaskIndex = data['currentTaskIndex']
        self.setCurrentTaskIndex(currentTaskIndex)
