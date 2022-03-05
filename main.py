import sys
from PyQt5 import QtGui, QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow

class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()

        custom_font = QtGui.QFont()
        custom_font.setWeight(5)
        custom_font.setPointSize(10)

        self.setWindowTitle("Table Extraction")
        self.setGeometry(640, 480, 640, 480)
        self.line = QtWidgets.QGroupBox(self)
        self.line.setGeometry(QtCore.QRect(0, 0, 1920, 40))

        self.button_import = QtWidgets.QPushButton(self) # вот эта кнопка
        self.button_import.setGeometry(0, 0, 80, 40)
        self.button_import.setText("Import")
        self.button_import.setFont(custom_font)
        self.button_import.clicked.connect(self.import_function) # вот эта функция

        self.button_settings = QtWidgets.QPushButton(self)
        self.button_settings.setGeometry(80, 0, 80, 40)
        self.button_settings.setText("Settings")
        self.button_settings.setFont(custom_font)

        self.button_export = QtWidgets.QPushButton(self)
        self.button_export.setGeometry(160, 0, 80, 40)
        self.button_export.setText("Export")
        self.button_export.setFont(custom_font)

        self.button_clear = QtWidgets.QPushButton(self)
        self.button_clear.setGeometry(560, 400, 40, 40)
        self.button_clear.setStyleSheet("border-radius : 20; border : 2px solid black")
        self.button_clear.setText("X")
        self.button_clear.setFont(custom_font)

    def import_function():
        # код здесь писать (а лучше сразу создать новый .py файл и написать эту функцию там)
        # функция должна позволять челам загружать .pdf файл (типо открывается проводник и там выбираешь файл)
        pass

def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()
