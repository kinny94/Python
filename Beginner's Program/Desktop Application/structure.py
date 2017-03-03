from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class HelloWorld(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        layout = QGridLayout()
        self.label = QLabel("Hello World!!")
        line_edit = QLineEdit()
        button = QPushButton("Close")

        layout.addWidget(self.label, 0, 0)
        layout.addWidget(line_edit, 0, 1)
        layout.addWidget(button, 1, 1)

        self.setLayout(layout)

        button.clicked.connect(self.close)
        line_edit.textChanged.connect(self.changeTextLabel)

        #self.connect(line_edit, SIGNAL("textChanged(QString)"), self.changeTextLabel) OLD SYNTAX

    def changeTextLabel(self, text):
        self.label.setText(text)

app = QApplication(sys.argv)  #QApplication is a unique object, as it says that you should only have one QApllication instance, even if application has multiple Windows
dialog = HelloWorld()         #QDialog is kind of a window
dialog.show()                 #Show the Dialog on the Screen
app.exec_()                   #execue the Application