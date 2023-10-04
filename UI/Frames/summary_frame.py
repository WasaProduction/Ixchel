from UI.Frames.frame import Frame
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QScrollArea, QHBoxLayout, QVBoxLayout
from UI.Widgets.status_widget_layout import StatusWidget
from UI.Widgets.tags.tag_container_widget import TagContainerWidget
from UI.Widgets.icons.sex_icon import SexIconWidget
from UI.Widgets.background import GeneralInformation, HereditaryBackground, PathologicBackground, Immunizations, Allergy
from UI.Widgets.patient_name import PatientName
from data_models.model_allergy import ModelAllergy
from UI.TwoD.graphic_view import GraphicView
from UI.Widgets.collapsible_box import CollapsibleBox
import random


class SummaryFrame(Frame):
    def __init__(self, parent=None, patient=None, button_paths=None, text_labels=None):
        super().__init__(parent, button_path=button_paths.summary, text_labels=text_labels)
        self.name = self.text_labels.summary_btn
        self.patient = patient
        self.init_ui()

    def update_summary(self):
        # self.patient_general_information_widget.update_widget()
        self.patient_allergies_widget.update_allergies()


    def init_ui(self):
        """General data"""
        # Essential data
        # First row name, blood type, sex = patient_essential_data_h_layout
        # Second row age
        patient_name_label = PatientName(name=self.patient.name, lastname_1=self.patient.lastname_1,
                                         lastname_2=self.patient.lastname_2)
        patient_age_label = QLabel("Age:")
        patient_age_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        blood_label_font = QFont('Arial', 30)
        blood_label_font.setBold(True)
        patient_blood_label = QLabel("O+")
        patient_blood_label.setFont(blood_label_font)

        # First row
        patient_essential_data_h_layout = QHBoxLayout()
        patient_essential_data_h_layout.addWidget(patient_name_label)
        patient_essential_data_h_layout.addWidget(patient_blood_label)
        patient_essential_data_h_layout.addWidget(SexIconWidget(2))
        patient_essential_data_h_widget = QWidget()
        patient_essential_data_h_widget.setLayout(patient_essential_data_h_layout)
        patient_essential_data_h_widget.setFixedHeight(80)

        # First second row
        patient_essential_data_v_layout = QVBoxLayout()
        patient_essential_data_v_layout.addWidget(patient_essential_data_h_widget)
        patient_essential_data_v_layout.addWidget(patient_age_label)
        patient_essential_data_widget = QWidget()
        patient_essential_data_widget.setLayout(patient_essential_data_v_layout)
        patient_essential_data_widget.setFixedHeight(100)

        # General information
        self.patient_general_information_widget = GeneralInformation(self, self.text_labels)
        # Hereditary background
        patient_hereditary_background_widget = HereditaryBackground(self, self.text_labels, 0)
        # Pathologic background
        patient_pathologic_background_widget = PathologicBackground(self, self.text_labels, 0)
        # Immunizations
        patient_immunizations_widget = Immunizations(self, self.text_labels, 0)
        # Allergies

        my_array = []
        for i in range(100):
            my_array.append(ModelAllergy('alergia', random.randrange(1, 5), random.randrange(1, 5)))
        self.patient_allergies_widget = Allergy(self, self.text_labels, my_array)
        """     Tags Section    """
        tags_container_widget = QScrollArea()
        tags_container_widget.setFixedHeight(150)
        tags_container_widget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        tags_container_layout = QVBoxLayout()
        # Tags will be displayed in a yearly manner
        year_diagnoses_dict = {}
        for diagnosis in self.patient.diagnosis_entries:
            # List all years with existing records
            if diagnosis.creation_date.year not in year_diagnoses_dict:
                year_diagnoses_dict[diagnosis.creation_date.year] = [diagnosis]
            else:
                year_diagnoses_dict[diagnosis.creation_date.year].append(diagnosis)
        # Sort dict
        years_list = list(year_diagnoses_dict.keys())
        years_list.sort(reverse=True)
        year_diagnoses_dict = {key: year_diagnoses_dict[key] for key in years_list}
        # Add a CollapsibleBox per Year into scroll area
        for year in year_diagnoses_dict:
            tags_container_layout.addWidget(CollapsibleBox(self, title=str(year),
                                                           content=TagContainerWidget(year_diagnoses_dict[year])))
        tags_container_widget.setAlignment(Qt.AlignmentFlag.AlignLeft)
        tags_container_widget.setLayout(tags_container_layout)
        # tags_container_widget.setStyleSheet('background-color: cyan;')
        """     Section Container   """
        patient_general_info_layout = QVBoxLayout()
        patient_general_info_layout.addWidget(patient_essential_data_widget)
        patient_general_info_layout.setStretch(0, 1)
        patient_general_info_layout.addWidget(self.patient_general_information_widget)
        patient_general_info_layout.setStretch(1, 1)
        patient_general_info_layout.addWidget(patient_hereditary_background_widget)
        patient_general_info_layout.setStretch(2, 1)
        patient_general_info_layout.addWidget(patient_pathologic_background_widget)
        patient_general_info_layout.setStretch(3, 1)
        patient_general_info_layout.addWidget(patient_immunizations_widget)
        patient_general_info_layout.setStretch(4, 1)
        patient_general_info_layout.addWidget(self.patient_allergies_widget)
        patient_general_info_layout.setStretch(5, 1)
        patient_general_info_layout.addWidget(tags_container_widget)
        patient_general_info_layout.setStretch(6, 4)
        patient_general_info_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        patient_general_info_layout.setSpacing(1)
        patient_general_info_widget = QWidget()
        patient_general_info_widget.setLayout(patient_general_info_layout)
        """     Patient statusbar   """
        patient_status_bar_widget = QWidget()
        patient_status_widget_layout = StatusWidget()
        patient_status_bar_widget.setLayout(patient_status_widget_layout)
        # For testing
        patient_status_bar_widget.setFixedWidth(50)

        """     Models   """
        #   Skeleton
        skeleton_view = GraphicView(self)
        three_d_models_bar_layout = QVBoxLayout()
        three_d_models_bar_layout.addWidget(skeleton_view)
        three_d_models_bar_layout.addStretch()
        three_d_models_bar_widget = QWidget()
        three_d_models_bar_widget.setLayout(three_d_models_bar_layout)

        # For testing
        three_d_models_bar_widget.setFixedWidth(200)

        """Add main widgets to the containers"""
        container_layout = QHBoxLayout()
        container_layout.addWidget(patient_general_info_widget)
        container_layout.addWidget(patient_status_bar_widget)
        container_layout.addWidget(three_d_models_bar_widget)
        self.setLayout(container_layout)
