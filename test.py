import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton
from UI.Frames.editing_area.tables.custom_table_hereditary import *
from UI.Frames.summary_frame import SummaryFrame
from assets.icons.buttons.button_paths import ButtonPaths
from mongodb.read.get_patient import GetPatient
from mongodb.read.get_text_labels import GetTextLabels


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setGeometry(100, 600, 1000, 500)
        button_paths = ButtonPaths()
        # QRcode()
        text_labels = GetTextLabels()
        my_layout = QVBoxLayout()
        my_test_obj = SummaryFrame(self, GetPatient('JaimeGq'), button_paths, text_labels)

#        """----------------------"""
        def pusheado():
            print('pusheado')
            my_test_obj.update_frame()

        pushme = QPushButton('test')
        pushme.clicked.connect(lambda: pusheado())

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
