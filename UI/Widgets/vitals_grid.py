from PyQt6.QtWidgets import QGridLayout, QWidget, QLineEdit, QLabel
from PyQt6.QtCore import Qt
from data_models.model_vital_signs import ModelVitalSigns
# https://www.pythontutorial.net/pyqt/pyqt-qgridlayout/


class VitalsGrid(QWidget):
    def __init__(self, text_labels=None):
        super().__init__()
        self.text_labels = text_labels
        # Labels
        self.labels = []
        pulse_label = QLabel(self.text_labels.pulse)
        self.labels.append(pulse_label)
        temperature_label = QLabel(self.text_labels.temperature)
        self.labels.append(temperature_label)
        blood_pressure_label = QLabel(self.text_labels.pressure)
        self.labels.append(blood_pressure_label)
        heart_rate_label = QLabel(self.text_labels.heart_rate)
        self.labels.append(heart_rate_label)
        respiratory_rate_label = QLabel(self.text_labels.respiratory_rate)
        self.labels.append(respiratory_rate_label)
        peripheral_oxygen_saturation_label = QLabel(self.text_labels.o2_saturation)
        self.labels.append(peripheral_oxygen_saturation_label)
        # Line edits
        self.line_edits = []
        pulse_line = QLineEdit()
        self.line_edits.append(pulse_line)
        temperature_line = QLineEdit()
        self.line_edits.append(temperature_line)
        blood_pressure_line = QLineEdit()
        self.line_edits.append(blood_pressure_line)
        heart_rate_line = QLineEdit()
        self.line_edits.append(heart_rate_line)
        respiratory_rate_line = QLineEdit()
        self.line_edits.append(respiratory_rate_line)
        peripheral_oxygen_saturation_line = QLineEdit()
        self.line_edits.append(peripheral_oxygen_saturation_line)

        #   Tune layout
        self.tune_ui()

    def tune_ui(self):
        #   Setup layout
        my_layout = QGridLayout()
        row_span = 1
        column_span = 1
        alignment = Qt.AlignmentFlag.AlignLeft
        #   Add widgets
        for column in range(len(self.labels)):
            my_layout.addWidget(self.labels[column], 0, column, row_span, column_span, alignment)
            my_layout.addWidget(self.line_edits[column], 1, column, row_span, column_span, alignment)
        #   Testing
        # self.setStyleSheet("background-color: cyan;")
        #   Apply layout
        self.setLayout(my_layout)

    def retrieve_data(self):
        empty_counter = 0
        for line_edit in self.line_edits:
            empty_counter += 0 if line_edit.text().strip() else 1
        if empty_counter == len(self.line_edits):
            return None
        else:
            #   Return None if no value is given
            pulse = self.line_edits[0].text().strip() if self.line_edits[0].text().strip() else None
            temperature = self.line_edits[1].text().strip() if self.line_edits[1].text().strip() else None
            blood_pressure = self.line_edits[2].text().strip() if self.line_edits[2].text().strip() else None
            heart_rate = self.line_edits[3].text().strip() if self.line_edits[3].text().strip() else None
            respiratory_rate = self.line_edits[4].text().strip() if self.line_edits[4].text().strip() else None
            oxygen_saturation = self.line_edits[5].text().strip() if self.line_edits[5].text().strip() else None
            return ModelVitalSigns(pulse, temperature, blood_pressure, heart_rate, respiratory_rate, oxygen_saturation)
