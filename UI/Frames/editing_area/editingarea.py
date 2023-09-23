from PyQt6.QtWidgets import QStackedWidget
from UI.Frames.editing_area.physical_examination import PhysicalExamination
from UI.Frames.editing_area.diagnosis_prescription import DiagnosisPrescription
from UI.Frames.editing_area.interrogatory import Interrogatory


class EditingArea(QStackedWidget):
    def __init__(self, parent=None):
        super(EditingArea, self).__init__(parent)
        # Match frames contained
        self.containing_frames = {}
        self.init_ui()

    def init_ui(self):
        """Frames"""
        #   Frames coupled with widgets
        #   Diagnosis
        diagnosis_prescription = DiagnosisPrescription(self)
        self.containing_frames['Diagnosis Prescription'] = 0
        #   Physical Examination
        physical_examination = PhysicalExamination(self)
        self.containing_frames['Physical Examination'] = 1
        #   Interrogatory
        interrogatory = Interrogatory(self)
        self.containing_frames['Interrogatory'] = 2

        """     Stack       """
        #   Frames added to the stack in the same order as before
        self.addWidget(diagnosis_prescription)
        self.addWidget(physical_examination)
        self.addWidget(interrogatory)

    def retrieve_data(self):
        #   Retrieve data of the current frame
        return self.currentWidget().retrieve_data()
