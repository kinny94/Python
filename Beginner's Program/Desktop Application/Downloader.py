from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import urllib.request

class Downloader(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        layout = QVBoxLayout()

        self.url = QLineEdit()
        self.save_location = QLineEdit()
        self.progress = QProgressBar()
        download = QPushButton("Download")
        browser = QPushButton("Browse")

        self.url.setPlaceholderText("URL")                           # placeholder for the url lineEdit
        self.save_location.setPlaceholderText("File Save Location")  # placeholder for the save location lineEdit

        self.progress.setValue(0)                                    # Sets the progress bar value to 0
        self.progress.setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.url)                                   # adding widgets to th layout
        layout.addWidget(self.save_location)
        layout.addWidget(browser)
        layout.addWidget(self.progress)
        layout.addWidget(download)

        self.setLayout(layout)
        self.setWindowTitle("My Downloader")                    # setting the name of the window
        self.setFocus()                                         # does not focus on anything.

        download.clicked.connect(self.download)                 # button click listener
        browser.clicked.connect(self.browse_file)


    def browse_file(self):
        save_file = QFileDialog.getSaveFileName(self, caption="Save File as", directory=".", filter="All Files(*.*)")
        self.save_location.setText(QDir.toNativeSeparators(save_file))

    def download(self):
        url = self.url.text()                                   # getting url text
        save_location = self.save_location.text()               # getting save location text

        if(url == "" or save_location == ""):
            QMessageBox.warning(self, "Warning", "Fields cannot be Empty")
        else:
            try:
                urllib.request.urlretrieve(url, save_location, reporthook=self.report)
            except Exception:
                QMessageBox.warning(self, "Warning", "Download Failed!")
                return

            QMessageBox.information(self, "Information", "The Download is complete")
            self.progress.setValue(0)
            self.url.setText("")
            self.save_location.setText("")

    def report(self, blocknum, blocksize, totalsize):
        readsofar = blocknum * blocksize
        if totalsize > 0:
            percentage = readsofar * 100 / totalsize
            self.progress.setValue(int(percentage))

app = QApplication(sys.argv)
dialog = Downloader()
dialog.show()
app.exec_()