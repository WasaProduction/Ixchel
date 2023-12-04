from PyQt6.QtWidgets import QVBoxLayout, QWidget
from UI.Widgets.image_button import ImageButton
from UI.Widgets.custom_qimage import CustomQImage
from UI.Widgets.Alerts.change_meds import ChangeMeds
from PyQt6.QtCore import pyqtSlot
from mongodb.read.get_affection_is_chronic import GetAffectionIsChronic
import random


class StatusBarWidget(QWidget):
    def __init__(self, parent=None, text_labels=None, patient=None):
        super().__init__(parent)
        #   Multilingual obj.
        self.text_labels = text_labels
        #   Patient obj.
        self.patient = patient
        #   Medication widget
        self.meds_btn = UnderMedication(self, self.text_labels, self.patient.prescriptions)
        #   Statuses widget
        self.statuses_widget = StatusesContainer(self, self.patient)
        #   Layout
        self.layout = QVBoxLayout(self)
        self.init_ui()

    def update_statuses(self, patient=None):
        #   Update patient.
        self.patient = patient
        #   Update medication.
        self.meds_btn.update_medication(self.patient.prescriptions)
        #   Update statuses.
        self.statuses_widget.update_statuses(self.patient)

    def init_ui(self):
        #   Place medication button.
        self.layout.addWidget(self.meds_btn)
        #   Place statuses placeholder.
        self.layout.addWidget(self.statuses_widget)
        #   Customize layout.
        self.layout.setSpacing(2)
        # Intended to stack all the widgets at the top
        self.layout.addStretch()


class StatusesContainer(QWidget):
    def __init__(self, parent=None, patient=None):
        super().__init__(parent)
        self.patient = patient
        #   Disease array.
        self.statuses = []
        #   Keep track of what's being displayed.
        self.displayed_statuses = []
        #   Layout.
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(2)
        self.setLayout(self.layout)

    def update_statuses(self, patient=None):
        #   Update patient model.
        self.patient = patient
        #   Remove presented statuses.
        self.remove_statuses()
        #   Update statuses.
        self.extract_chronic_diseases()
        #   Place statuses.
        self.place_statuses()

    def extract_chronic_diseases(self):
        #   Tp avoid duplicates
        tags_contained = []
        #   Traverse all diagnoses.
        for diagnosis in self.patient.diagnosis_entries:
            #   Traverse all tags within the diagnoses.
            for tag in diagnosis.tags_contained:
                #   Avoid duplicates.
                if tag not in tags_contained:
                    #   Extract disease from tag.
                    my_disease = GetAffectionIsChronic(tag)
                else:
                    continue
                if my_disease.chronic:
                    #   Add status
                    self.statuses.append(my_disease)
                    #   Keep track of already displayed tags.
                    tags_contained.append(tag)

    def place_statuses(self):
        for status in self.statuses:
            #   Create icon.
            icon = ImageButton(CustomQImage(random.choice(range(1, 5))))
            icon.setToolTip(status.name)
            #   Keep track of displayed icons.
            self.displayed_statuses.append(icon)
            #   Add icon.
            self.layout.addWidget(icon)

    def remove_statuses(self):
        #   Remove treatments
        if len(self.displayed_statuses):
            #   Remove displayed statuses
            for index, displayed_status in enumerate(self.displayed_statuses):
                displayed_status.deleteLater()
        #   Update arrays
        self.displayed_statuses = []
        self.statuses = []


class UnderMedication(QWidget):
    def __init__(self, parent=None, text_labels=None, prescriptions=None):
        super().__init__(parent)
        self.text_labels = text_labels
        #   All prescriptions.
        self.prescriptions = prescriptions
        #   Keep track of editable instructions.
        self.active_instructions = []
        #   Button icon.
        self.icon = ImageButton(CustomQImage(0))
        self.icon.clicked.connect(lambda: self.modify_meds())
        #   Initialize dialog.
        self.dialog = ChangeMeds(self, self.text_labels)
        #   Layout
        self.layout = QVBoxLayout()
        #   UI
        self.init_ui()
        self.update_medication()

    #@pyqtSlot
    def modify_meds(self):
        #   Update dialog.
        self.dialog.update_instructions(self.active_instructions)
        #   Shoe dialog.
        self.dialog.exec()

    def button_enabling(self, enabled=True):
        #   Disable button.
        self.setEnabled(enabled)
        #   TODO Change button appearance.

    def extract_active_instructions(self):
        #   Clear active_instructions contents.
        self.active_instructions = []

        for prescription in self.prescriptions:
            #   Discard disabled prescriptions.
            if prescription.active:
                for instruction in prescription.instructions:
                    self.active_instructions.append(instruction)

    def update_medication(self, prescriptions=None):
        #   Validate if there are prescriptions to work with.
        if prescriptions is None:
            return
        #   Restore
        self.prescriptions = prescriptions
        #   Retrieve active instructions.
        self.extract_active_instructions()
        #   Validate if there are active instructions.
        if self.active_instructions:
            self.button_enabling(True)
        else:
            self.button_enabling(False)

    def init_ui(self):
        #   Customize margins
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.icon)
        self.setLayout(self.layout)
