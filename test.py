#"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QScrollArea
from PyQt6.QtCore import Qt
from UI.Frames.editing_area.tables.custom_table_hereditary import *
from UI.Widgets.tags.tag_container_widget import TagsContainer
from UI.Frames.summary_frame import SummaryFrame
from assets.icons.buttons.button_paths import ButtonPaths
from mongodb.read.get_patient import GetPatient
from mongodb.read.get_text_labels import GetTextLabels
from UI.Widgets.background import Allergy
from UI.Widgets.Alerts.diagnosis_info import DiagnosisInfo


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setGeometry(100, 600, 1000, 500)
        self.patient = GetPatient()
        button_paths = ButtonPaths()
        # QRcode()
        self.text_labels = GetTextLabels()
        my_layout = QVBoxLayout()
        #my_test_obj = SummaryFrame(self, patient, button_paths, text_labels)
        my_test_obj = QWidget()#Allergy(self, self.text_labels, self.patient.allergies)
        #child = my_test_obj.allergies_container


        """     Tags Section    """

        def pusheado():
            DiagnosisInfo()
            #self.patient = GetPatient('JaimeGQ')
            #my_test_obj.update_allergies(self.patient.allergies)
            pass
            #my_test_obj.update_summary()
            #throttle = ThrottleDebounce(pusheado)


#"""
#        """----------------------"""
#"""


        pushme = QPushButton('test')
        pushme.setAutoRepeat(False)
        pushme.clicked.connect(lambda: pusheado())

        my_layout.addWidget(pushme)
        my_layout.addWidget(my_test_obj)
        #my_layout.addWidget(child)

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
