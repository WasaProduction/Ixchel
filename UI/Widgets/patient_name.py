from PyQt6.QtWidgets import QWidget,  QHBoxLayout, QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class PatientName(QWidget):
    def __init__(self, parent=None, name='', lastname_1='', lastname_2=''):
        super().__init__(parent)
        #   Variables
        self.name = name
        self.lastname_1 = lastname_1
        self.lastname_2 = lastname_2
        #   Container layout
        self.my_layout = QHBoxLayout()
        #   Labels
        self.patient_name_lbl = QLabel()
        self.patient_lastname_lbl = QLabel()
        #   Tune labels
        self.customize_name_labels()
        #   Fill labels
        self.update_name_lbl()
        """     UI      """
        self.customize_layout()
        self.init_ui()

    def customize_layout(self):
        self.my_layout.setSpacing(0)
        self.my_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.my_layout.addStretch()

    def update_name_lbl(self):
        self.patient_name_lbl.setText(self.name + ' ')
        self.patient_lastname_lbl.setText(self.lastname_1 + ' ' + self.lastname_2)

    def customize_name_labels(self):
        """     Name        """
        #   Font
        name_font = QFont('Arial', 30)
        name_font.setBold(True)
        self.patient_name_lbl.setFont(name_font)

        self.patient_name_lbl.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.patient_name_lbl.setAlignment(Qt.AlignmentFlag.AlignBottom)
        #   Add label to layout.
        self.my_layout.addWidget(self.patient_name_lbl)

        """     Lastnames       """
        #   Font
        lastname_font = QFont('Arial', 25)
        self.patient_lastname_lbl.setFont(lastname_font)

        self.patient_lastname_lbl.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.patient_lastname_lbl.setAlignment(Qt.AlignmentFlag.AlignBottom)
        #   Add label to layout.
        self.my_layout.addWidget(self.patient_lastname_lbl)

    def update_text(self, name='', lastname_1='', lastname_2=''):
        #   Update variables.
        self.name = name
        self.lastname_1 = lastname_1
        self.lastname_2 = lastname_2
        #   Update labels.
        self.update_name_lbl()

    """     UI      """
    def init_ui(self):
        self.setLayout(self.my_layout)

