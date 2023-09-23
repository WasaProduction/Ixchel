# QT modules
from PyQt6.QtWidgets import QApplication
from UI.main_window.main_window import MainWindow
# Module for processing command line arguments
import sys

app = QApplication(sys.argv)
myWindow = MainWindow()

myWindow.show()
app.exec()
