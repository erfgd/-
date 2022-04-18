import camelot
import tabula
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


def camelot_func(file):
    tables = camelot.read_pdf(file, pages = '1, 2-end', process_background=True)
    tables.export('filename.csv', f='csv', compress=True)
    print('HI')
    for i in range(len(tables)):
        tables[i].to_csv(f'filename{i}.csv')
        print('hi')

def tabula_func(file):
    # PDF = tabula.read_pdf(file, pages='all', multiple_tables=True)

    # if you want view the result before saving - delete "#" from next string:
    # print ('\nTables from PDF file\n'+str(PDF))

    pdf_out_csv = "C:/Users/Roman/-"
    tabula.convert_into(file, f'{pdf_out_csv}{"/"}tabula_conversion.csv',
                        output_format="csv", pages='all')
    print("Done")


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
        self.camelot_button.setStyleSheet("background-color: lightgreen")
        self.camelot_button.clicked.connect(self.camelot_connect)

        self.tabula_button = QtWidgets.QPushButton(self)
        self.tabula_button.setGeometry(80,0,80,40)
        self.tabula_button.setFont(custom_font)
        self.tabula_button.setText('Tabula')
        self.tabula_button.setStyleSheet("background-color: lightgreen")
        self.tabula_button.clicked.connect(self.tabula_connect)

    def camelot_connect(self):
        camelot_func(filename)

    def tabula_connect(self):
        tabula_func(filename)
