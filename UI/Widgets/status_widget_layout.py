from PyQt6.QtWidgets import QVBoxLayout, QWidget
from UI.Widgets.image_button import ImageButton
from UI.Widgets.custom_qimage import CustomQImage
from UI.Widgets.Alerts.change_meds import ChangeMeds
from PySide6.QtCore import Slot
import random


class StatusWidget(QWidget):
    def __init__(self, parent=None, under_treatment=True, statuses=None):
        super().__init__(parent)
        #   Keep track of medication
        self.under_treatment = under_treatment
        #   Medication widget
        self.meds_btn = UnderMedication()
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
        if self.under_treatment:
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

    def update_statuses(self, under_treatment=False, statuses=None):
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
        self.under_treatment = under_treatment
        self.statuses = statuses
        #   Place new statuses
        if statuses is not None:
            self.place_statuses()

    def init_ui(self):
        self.layout.setSpacing(2)
        # Intended to stack all the widgets at the top
        self.layout.addStretch()


class UnderMedication(QWidget):
    def __init__(self, parent=None, under_treatment=False, meds=None):
        super().__init__(parent)
        self.medicated = under_treatment
        self.icon = ImageButton(CustomQImage(0))
        self.icon.clicked.connect(lambda: self.modify_meds())
        self.dialog = ChangeMeds()
        #   Layout
        self.layout = QVBoxLayout()
        #   UI
        self.init_ui()

    @Slot()
    def modify_meds(self):
        self.dialog.exec()

    def button_active(self, active=True):
        if active:
            #   Back to normal color
            pass
        else:
            #   Grey out
            pass
        #   Keep track of status
        self.medicated = active

    def remove_medication(self):
        pass

    def add_medication(self):
        pass

    def update_medication(self, under_treatment=False, meds=None):
        if under_treatment:
            #   Medication active
            self.add_medication()
            self.button_active(under_treatment)
        else:
            #   No medication active
            self.remove_medication()
            self.button_active(under_treatment)

    def init_ui(self):
        #   Customize margins
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.icon)
        self.setLayout(self.layout)
