from PyQt6.QtWidgets import QVBoxLayout, QWidget
from UI.Widgets.image_button import ImageButton
from UI.Widgets.custom_qimage import CustomQImage
from UI.Widgets.Alerts.change_meds import ChangeMeds
from PySide6.QtCore import Slot
import random


class StatusBarWidget(QWidget):
    def __init__(self, parent=None, patient=None, statuses=None):
        super().__init__(parent)
        self.patient = patient
        #   Medication widget
        self.meds_btn = UnderMedication(self, self.patient.prescriptions)
        #
        self.statuses = statuses
        self.displayed_statuses = []
        self.layout = QVBoxLayout(self)
        #   Place meds
        self.layout.addWidget(self.meds_btn)
        #   Place statuses
        self.place_statuses()
        self.init_ui()

    def place_statuses(self):
        #   Place treatment
        if self.patient.prescriptions:
            pass
        #   Place statuses
        for status in range(0, 10): #self.statuses:
            #   Create icon.
            icon = ImageButton(CustomQImage(random.choice(range(1, 5))))
            #   Keep track of displayed icons.
            self.displayed_statuses.append(icon)
            #   Add icon.
            self.layout.addWidget(icon)
        pass

    def remove_statuses(self):
        #   Remove treatments
        if len(self.displayed_statuses):
            #   Remove displayed statuses
            for index, displayed_status in enumerate(self.displayed_statuses):
                displayed_status.deleteLater()
            #   Update array
            self.displayed_statuses = []

    def update_statuses(self, statuses=None):
        #   Remove previously displayed information
        self.remove_statuses()
        """
        if under_treatment:
            # Update if there's a treatment
            self.meds_btn.update_medication()
        elif not under_treatment and self.meds_btn.medicated:
            #   Update if previously there was a treatment
            self.meds_btn.update_medication()
        """
        #   Update variables
        self.statuses = statuses
        #   Place new statuses
        if statuses is not None:
            self.place_statuses()

    def init_ui(self):
        self.layout.setSpacing(2)
        # Intended to stack all the widgets at the top
        self.layout.addStretch()


class UnderMedication(QWidget):
    def __init__(self, parent=None, prescriptions=None):
        super().__init__(parent)
        #   All prescriptions.
        self.prescriptions = prescriptions
        #   Keep track of edittable instructions.
        self.active_instructions = []
        #   Button icon.
        self.icon = ImageButton(CustomQImage(0))
        self.icon.clicked.connect(lambda: self.modify_meds())
        #   Initialize dialog.
        self.dialog = ChangeMeds()
        #   Layout
        self.layout = QVBoxLayout()
        #   UI
        self.init_ui()
        self.update_medication()

    @Slot()
    def modify_meds(self):
        #   Setup dialog.
        self.dialog = ChangeMeds()
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
        """
        #   Validate if there are prescriptions to work with.
        if prescriptions is None:
            return
        #   Restore
        self.prescriptions = prescriptions
        """
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
