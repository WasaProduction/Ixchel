from PyQt6.QtWidgets import QWidget, QVBoxLayout
from UI.Frames.editing_area.section_widget import SectionWidget
from UI.Frames.editing_area.tables.custom_formulary_table import CustomFormularyTable
from UI.Widgets.custom_treeview import CustomTreeview
from data_models.external_habitus import HabitusFullDict


class PhysicalExamination(QWidget):
    def __init__(self, parent=None, text_labels=None):
        super(PhysicalExamination, self).__init__(parent)
        self.text_labels = text_labels

        """     Exterior Habitus        """
        habitus_lbl_str = self.text_labels.habitus
        self.habitus_dict = HabitusFullDict().my_dict
        self.habitus_widget = CustomFormularyTable(self, self.habitus_dict)
        systems_section = SectionWidget(self, habitus_lbl_str, [self.habitus_widget])

        """     History      """
        history_lbl_str = self.text_labels.history_log
        historic_widget = CustomTreeview()
        examination_section = SectionWidget(self, history_lbl_str, [historic_widget])

        """     Tune widget     """
        #   All sections contained in the interrogatory
        self.containing_widgets = []
        #   Add sections
        self.containing_widgets.append(systems_section)
        self.containing_widgets.append(examination_section)
        # Layout of Interrogatory class
        self.examination_lyt = QVBoxLayout()
        #   Tune UI
        self.tune_ui()

    def tune_ui(self):
        # Pull each section from the array and add it to the layout
        for section in self.containing_widgets:
            self.examination_lyt.addWidget(section)
        # Set the layout to the Interrogatory widget
        self.setLayout(self.examination_lyt)

    def update_data(self, habitus):
        # Reset all data models
        self.habitus_dict = habitus
        # Reset UI
        self.tune_ui()

    def retrieve_data(self):
        #   None value if empty
        return [{'habitus': self.habitus_widget.retrieve_data()}]
