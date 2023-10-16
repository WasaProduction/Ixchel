from PyQt6.QtWidgets import QStackedWidget
from UI.Frames.editing_area.physical_examination import PhysicalExamination
from UI.Frames.editing_area.diagnosis_prescription import DiagnosisPrescription
from UI.Frames.editing_area.interrogatory import Interrogatory


class EditingArea(QStackedWidget):
    def __init__(self, parent=None, text_labels=None):
        self.text_labels = text_labels
        super(EditingArea, self).__init__(parent)
        # Match frames contained
        self.containing_frames = {}
        self.init_ui()

    def init_ui(self):
        """Frames"""
        #   Frames coupled with widgets
        #   Diagnosis
        diagnosis_prescription = DiagnosisPrescription(self, self.text_labels)
        self.containing_frames[self.text_labels.diagnosis_prescription] = 0
        #   Physical Examination
        physical_examination = PhysicalExamination(self, self.text_labels)
        self.containing_frames[self.text_labels.physical_examination] = 1
        #   Interrogatory
        interrogatory = Interrogatory(self, self.text_labels)
        self.containing_frames[self.text_labels.interrogatory] = 2

        """     Stack       """
        #   Frames added to the stack in the same order as before
        self.addWidget(diagnosis_prescription)
        self.addWidget(physical_examination)
        self.addWidget(interrogatory)

    def retrieve_data(self):
        #   Retrieve data of the current frame
        return self.currentWidget().retrieve_data()
