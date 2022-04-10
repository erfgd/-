import sys

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineSettings, QWebEngineView
from PyQt5.QtCore import QUrl

from functions.export_fucntion import ExportGui, filename_catch



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
        self.button_import.setStyleSheet("background-color: lightgreen")
        self.button_import.clicked.connect(self.showDialog)

        self.button_preview = QtWidgets.QPushButton(self)
        self.button_preview.setGeometry(160, 0, 80, 40)
        self.button_preview.setText("Preview")
        self.button_preview.setFont(custom_font)
        self.button_preview.setStyleSheet("background-color: red")

        self.button_export = QtWidgets.QPushButton(self)
        self.button_export.setGeometry(80, 0, 80, 40)
        self.button_export.setText("Export")
        self.button_export.setFont(custom_font)
        self.button_export.setStyleSheet("background-color: red")

        self.button_help = QtWidgets.QPushButton(self)
        self.button_help.setGeometry(240,0,80,40)
        self.button_help.setText("Help")
        self.button_help.setFont(custom_font)
        self.button_help.setStyleSheet("background-color: yellow")

    def showDialog(self):
        custom_font = QtGui.QFont()
        custom_font.setWeight(5)
        custom_font.setPointSize(10)
        global filename
        filename = QFileDialog.getOpenFileName(self, 'Open pdf file', '')[0]
        if filename[-4:] == '.pdf':
            filename_catch(filename)
            self.button_export.clicked.connect(self.export_function)
            self.button_preview.clicked.connect(self.preview_function)
            self.button_export.setStyleSheet("background-color: lightgreen")
            self.button_preview.setStyleSheet("background-color: lightgreen")

    def export_function(self):
        self.Export = ExportGui()
        self.Export.show()

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
