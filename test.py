#"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from UI.Frames.editing_area.tables.custom_table_hereditary import *
from UI.Frames.summary_frame import SummaryFrame
from assets.icons.buttons.button_paths import ButtonPaths
from mongodb.read.get_patient import GetPatient
from mongodb.read.get_text_labels import GetTextLabels
from throttle_debounce import ThrottleDebounce
from UI.Widgets.background import GeneralInformation, HereditaryBackground, PathologicBackground, Immunizations, Allergy


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setGeometry(100, 600, 1000, 500)
        button_paths = ButtonPaths()
        # QRcode()
        text_labels = GetTextLabels()
        my_layout = QVBoxLayout()
        my_test_obj = GeneralInformation(self, text_labels) #SummaryFrame(self, GetPatient('JaimeGq'), button_paths, text_labels)
        def pusheado():
            print('pusheado')
            my_test_obj.update_frame()
        throttle = ThrottleDebounce(pusheado)
#"""
#        """----------------------"""
#"""


        pushme = QPushButton('test')
        pushme.setAutoRepeat(False)
        pushme.clicked.connect(lambda: throttle.throttle())

        my_layout.addWidget(pushme)
        my_layout.addWidget(my_test_obj)

        my_widget = QWidget()
        my_widget.setLayout(my_layout)
        #my_widget.setFixedWidth(500)
        #my_widget.setFixedHeight(400)
        # Set the central widget of the Window.
        self.setCentralWidget(my_widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
#"""