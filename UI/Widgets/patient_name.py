from PyQt6.QtWidgets import QWidget,  QHBoxLayout, QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class PatientName(QWidget):
    def __init__(self, name='', lastname_1=None, lastname_2=None):
        super().__init__()
        # Container layout
        my_layout = QHBoxLayout()
        # Add bigger name
        name_font = QFont('Arial', 30)
        name_font.setBold(True)
        patient_name_lbl = QLabel(name + ' ')
        patient_name_lbl.setFont(name_font)
        patient_name_lbl.setAlignment(Qt.AlignmentFlag.AlignLeft)
        patient_name_lbl.setAlignment(Qt.AlignmentFlag.AlignBottom)
        my_layout.addWidget(patient_name_lbl)
        my_layout.setSpacing(0)
        my_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        complete_last_name = ''
        if lastname_1 is not None:
            lastname_font = QFont('Arial', 25)
            complete_last_name += lastname_1
            if lastname_2 is not None:
                complete_last_name += ' '
                complete_last_name += lastname_2
            patient_lastname_lbl = QLabel(complete_last_name)
            patient_lastname_lbl.setFont(lastname_font)
            patient_lastname_lbl.setAlignment(Qt.AlignmentFlag.AlignLeft)
            patient_lastname_lbl.setAlignment(Qt.AlignmentFlag.AlignBottom)
            my_layout.addWidget(patient_lastname_lbl)
        my_layout.addStretch()
        self.setLayout(my_layout)

