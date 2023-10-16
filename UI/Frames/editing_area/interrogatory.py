from PyQt6.QtWidgets import QScrollArea, QVBoxLayout, QWidget, QSizePolicy, QPlainTextEdit
from PyQt6.QtCore import Qt
from UI.Frames.editing_area.section_widget import SectionWidget
from UI.Frames.editing_area.tables.custom_table_hereditary import WidgetTableButtons
from UI.Frames.editing_area.tables.custom_formulary_table import CustomFormularyTable
from UI.Widgets.custom_text_edit import CustomTextEdit
from data_models.patient.general_info import GeneralInfo


class Interrogatory(QScrollArea):
    def __init__(self, parent=None, text_labels=None):
        super(Interrogatory, self).__init__(parent)
        self.text_labels = text_labels

        """     Data models for sections        """
        self.anamnesis_dict = {}
        self.hereditary_background = {}
        self.personal_background = {}
        self.pathologic_background = {}
        self.non_pathologic_background = {}
        self.systems = {}

        """     Anamnesis     """
        anamnesis_lbl_str = self.text_labels.id_card
        self.anamnesis_dict = GeneralInfo()
        self.anamnesis_widget = CustomFormularyTable(self, self.anamnesis_dict)
        anamnesis_section = SectionWidget(self, anamnesis_lbl_str, [self.anamnesis_widget])

        """     Hereditary background       """
        hereditary_lbl_str = self.text_labels.hereditary_background
        my_test_dict_2 = {'abuela_materna': 'diabetes_mellitus_tipo_1', 'abuelo_materno':
            'carcinoma_de_células_escamosas_de_la_encía', 'papa': 'hiperesplenismo', 'mama': 'anisometropía'}
        self.hereditary_widget = WidgetTableButtons(self, my_test_dict_2, True)
        hereditary_section = SectionWidget(self, hereditary_lbl_str, [self.hereditary_widget])

        """     Personal background        """
        # Pathologic
        pathologic_lbl_str = self.text_labels.pathologic_background
        my_pathologic_placeholder = 'Enter pathologic background'
        self.pathologic_formulary = CustomTextEdit(self, '/Users/jaimegonzalezquirarte/Desktop/App/vocabulario.txt',
                                              placeholder_str=my_pathologic_placeholder)
        pathologic_section = SectionWidget(self, pathologic_lbl_str, [self.pathologic_formulary])
        # Non-pathologic
        non_pathologic_lbl_str = self.text_labels.non_path_background
        self.non_pathologic_formulary = QPlainTextEdit()
        non_pathologic_section = SectionWidget(self, non_pathologic_lbl_str, [self.non_pathologic_formulary])

        """     Tune widget     """
        # All sections contained in the interrogatory
        self.containing_widgets = []
        # Add all sections
        self.containing_widgets.append(anamnesis_section)
        self.containing_widgets.append(hereditary_section)
        self.containing_widgets.append(pathologic_section)
        self.containing_widgets.append(non_pathologic_section)
        # Layout of Interrogatory class
        self.interrogatory_lyt = QVBoxLayout()
        # Call tune_ui function
        self.tune_ui()

    def tune_ui(self):
        #   Enabling/Disabling scroll bars
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed))
        # Pull each section from the array and add it to the layout
        for section in self.containing_widgets:
            self.interrogatory_lyt.addWidget(section)
        # Set the layout to the Interrogatory widget
        interrogatory_widget = QWidget()
        interrogatory_widget.setLayout(self.interrogatory_lyt)
        self.setWidget(interrogatory_widget)

    def update_data(self, background_data):
        # Reset all data models
        self.hereditary_background = background_data
        self.personal_background = {}
        self.pathologic_background = {}
        self.non_pathologic_background = {}
        self.systems = {}
        # Reset UI
        self.tune_ui()

    def retrieve_data(self):
        anamnesis = {'anamnesis': self.anamnesis_widget.retrieve_data()}
        hereditary = {'hereditary': self.hereditary_widget.retrieve_data()}
        pathologic = {'pathologic': self.pathologic_formulary.retrieve_data()}

        contained_data = [anamnesis, hereditary, pathologic]
        return contained_data
