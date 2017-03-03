from PyQt4.QtGui import  *
from PyQt4.QtCore import *
import sys

class FirstBox(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        layout = QGridLayout()
        self.label1 = QLabel("First Activity")
        self.line_edit1 = QLineEdit()
        self.label2 = QLabel("Second Activity")
        self.line_edit2 = QLineEdit()
        self.button = QPushButton("Close")

        layout.addWidget(self.label1, 0, 0)
        layout.addWidget(self.line_edit1, 0, 1)
        layout.addWidget(self.label2, 1, 0)
        layout.addWidget(self.line_edit2, 1, 1)
        layout.addWidget(self.button, 2, 1)

        self.setLayout(layout)


class SecondBox(QDialog):
    pass

app = QApplication(sys.argv)
dialog = FirstBox()
dialog.show()
app.exec_()