import camelot
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


def camelot_func(file):
    tables = camelot.read_pdf(file, pages = '1, 2-end', process_background=True)
    tables.export('filename.csv', f='csv', compress=True)
    print('HI')
    for i in range(len(tables)):
        tables[i].to_csv(f'filename{i}.csv')
        print('hi')


def filename_catch(file):
    global filename
    filename = file
    print(filename)

class ExportGui(QMainWindow):

    def __init__(self):
        super(ExportGui, self).__init__()

        custom_font = QtGui.QFont()
        custom_font.setWeight(5)
        custom_font.setPointSize(10)

        self.setWindowTitle("Export")
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setGeometry(480, 320, 320, 160)

        self.camelot_button = QtWidgets.QPushButton(self)
        self.camelot_button.setGeometry(0, 0, 80, 40)
        self.camelot_button.setFont(custom_font)
        self.camelot_button.setText('Camelot')
        self.camelot_export.setStyleSheet("background-color: lightgreen")
        self.camelot_button.clicked.connect(self.camelot_connect)

    def camelot_connect(self):
        camelot_func(filename)
