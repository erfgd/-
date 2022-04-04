import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineSettings, QWebEngineView

def preview_func(filename):
    class PDFPreview(QMainWindow):
        def __init__(self):
            super(QMainWindow, self).__init__()

            self.setWindowTitle("PDF Viewer")
            self.setGeometry(0, 28, 1000, 750)
            self.centralWidget = QWidget(self)

            self.webView = QWebEngineView()
            self.webView.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
            self.webView.settings().setAttribute(QWebEngineSettings.PdfViewerEnabled, True)
            self.setCentralWidget(self.webView)

        def url_changed(self):
            self.setWindowTitle(self.webView.title())

        def go_back(self):
            self.webView.back()

    app = QApplication(sys.argv)
    win = PDFPreview()
    win.show()
    if len(sys.argv) > 1:
        print("error")
    else:
        pdf = filename
        win.webView.setUrl(QUrl(filename))
    sys.exit(app.exec_())

