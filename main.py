import sys

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineSettings, QWebEngineView
from PyQt5.QtCore import QUrl

from functions.export_fucntion import export_func


class PDFPreview(QMainWindow):
    def __init__(self):
        super(PDFPreview, self).__init__()

        self.setWindowTitle("PDF Viewer")
        self.setGeometry(0, 28, 1000, 750)
        self.centralWidget = QWidget(self)

        self.webView = QWebEngineView()
        self.webView.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.webView.settings().setAttribute(QWebEngineSettings.PdfViewerEnabled, True)
        self.webView.setUrl(QUrl(filename))
        self.setCentralWidget(self.webView)

class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()

        self.init_gui()

    def init_gui(self):
        custom_font = QtGui.QFont()
        custom_font.setWeight(5)
        custom_font.setPointSize(10)

        self.setWindowTitle("Table Extraction")
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setGeometry(640, 480, 320, 160)
        self.line = QtWidgets.QGroupBox(self)
        self.line.setGeometry(QtCore.QRect(0, 0, 1920, 40))

        self.button_import = QtWidgets.QPushButton(self)  # вот эта кнопка
        self.button_import.setGeometry(0, 0, 80, 40)
        self.button_import.setText("Import")
        self.button_import.setFont(custom_font)
        self.button_import.clicked.connect(self.showDialog)

        self.button_preview = QtWidgets.QPushButton(self)
        self.button_preview.setGeometry(160, 0, 80, 40)
        self.button_preview.setText("Preview")
        self.button_preview.setFont(custom_font)

        self.button_export = QtWidgets.QPushButton(self)
        self.button_export.setGeometry(80, 0, 80, 40)
        self.button_export.setText("Export")
        self.button_export.setFont(custom_font)

    def showDialog(self):
        custom_font = QtGui.QFont()
        custom_font.setWeight(5)
        custom_font.setPointSize(10)
        global filename
        filename = QFileDialog.getOpenFileName(self, 'Open pdf file', '')[0]
        self.button_export.clicked.connect(self.export_function)
        self.button_preview.clicked.connect(self.preview_function)

    def export_function(self):
        export_func(filename)

    def preview_function(self):
        self.pdf = PDFPreview()
        self.pdf.show()

def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()
