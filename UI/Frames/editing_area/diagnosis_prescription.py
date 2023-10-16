from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QScrollArea
from UI.Widgets.custom_text_edit import CustomTextEdit
from UI.Widgets.prescription_txt_edit.prescription_text_edit import PrescriptionTextEdit
from UI.Widgets.vitals_grid import VitalsGrid
from UI.Widgets.collapsible_box import CollapsibleBox
from UI.Frames.editing_area.tables.custom_formulary_table import CustomFormularyTable
from data_models.systems_aparatus import SystemsAparatus
from data_models.physical_examination import PhysicalExamination
# https://stackoverflow.com/questions/28956693/pyqt5-qtextedit-auto-completion


class DiagnosisPrescription(QScrollArea):
    def __init__(self, parent=None, text_labels=None):
        super(DiagnosisPrescription, self).__init__(parent)
        self.text_labels = text_labels

        self.scroll_content_layout = QVBoxLayout()
        #   Interrogatory
        self.my_interrogatory = CustomFormularyTable(self, SystemsAparatus())
        my_collapsible_interrogatory = CollapsibleBox(self, self.text_labels.interrogatory, self.my_interrogatory)

        #   Examination
        self.my_physical_examination = CustomFormularyTable(self, PhysicalExamination())
        my_collapsible_examination = CollapsibleBox(self, self.text_labels.examination, self.my_physical_examination)

        #   Create label & Text Area
        diagnosis_label = QLabel(self.text_labels.diagnosis)
        self.my_diagnosis = CustomTextEdit(self, '/Users/jaimegonzalezquirarte/Desktop/App/vocabulario.txt')
        prescription_label = QLabel(self.text_labels.prescription)
        self.my_prescription = PrescriptionTextEdit(self, '/Users/jaimegonzalezquirarte/Desktop/App/vocabulario.txt')
        #   Container widget layout
        self.vitals_widget = VitalsGrid(self.text_labels)
        #   Adding elements to layouts
        self.scroll_content_layout.addWidget(self.vitals_widget)
        self.scroll_content_layout.addWidget(my_collapsible_interrogatory)
        self.scroll_content_layout.addWidget(my_collapsible_examination)
        self.scroll_content_layout.addWidget(diagnosis_label)
        self.scroll_content_layout.addWidget(self.my_diagnosis)
        self.scroll_content_layout.addWidget(prescription_label)
        self.scroll_content_layout.addWidget(self.my_prescription)
        #   Container widget
        my_container_widget = QWidget()
        #   Setting container widget layout
        my_container_widget.setLayout(self.scroll_content_layout)
        #   Getting container widget inside scroll area
        self.setWidget(my_container_widget)
        #   Tune UI
        self.tune_ui()

    def retrieve_data(self):
        #   Null value , if all parameters are empty
        vitals = {'vitals': self.vitals_widget.retrieve_data()}
        interrogatory = {'interrogatory': self.my_interrogatory.retrieve_data()}
        examination = {'examination': self.my_physical_examination.retrieve_data()}
        diagnosis = {'diagnosis': self.my_diagnosis.retrieve_data()}
        prescription = {'prescription': self.my_prescription.retrieve_data()}
        #   Group all data
        contained_data = [vitals, interrogatory, examination, diagnosis, prescription]
        #   Return contained data
        return contained_data

    def tune_ui(self):
        #   Prevent widgets from squashing or colliding with each other
        self.setWidgetResizable(True)
