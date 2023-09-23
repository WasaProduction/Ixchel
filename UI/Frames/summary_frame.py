from PyQt6.QtWidgets import QWidget, QVBoxLayout,  QHBoxLayout, QLabel, QScrollArea
from PyQt6.QtGui import QFont
from UI.Widgets.status_widget_layout import StatusWidget
from UI.Widgets.tags.tag_container_widget import TagContainerWidget
from UI.Widgets.icons.sex_icon import SexIconWidget
from UI.Widgets.background import *
from PyQt6.QtCore import Qt
from UI.Widgets.patient_name import PatientName
from data_models.model_allergy import ModelAllergy
import random


class SummaryFrame(QWidget):
    def __init__(self, patient):
        super().__init__()
        self.patient = patient
        self.init_ui()

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
        patient_general_information_widget = GeneralInformation(0)
        # Hereditary background
        patient_hereditary_background_widget = HereditaryBackground(0)
        # Pathologic background
        patient_pathologic_background_widget = PathologicBackground(0)
        # Immunizations
        patient_immunizations_widget = Immunizations(0)
        # Allergies

        my_array = []
        for i in range(33):
            my_array.append(ModelAllergy('alergia', random.randrange(1, 5), random.randrange(1, 5)))
        patient_allergies_widget = Allergy(my_array)
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
        patient_general_info_layout.addWidget(patient_general_information_widget)
        patient_general_info_layout.addWidget(patient_hereditary_background_widget)
        patient_general_info_layout.addWidget(patient_pathologic_background_widget)
        patient_general_info_layout.addWidget(patient_immunizations_widget)
        patient_general_info_layout.addWidget(patient_allergies_widget)
        patient_general_info_layout.addWidget(tags_container_widget)
        patient_general_info_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        patient_general_info_widget = QWidget()
        patient_general_info_widget.setLayout(patient_general_info_layout)
        """     Patient statusbar   """
        patient_status_bar_widget = QWidget()
        patient_status_widget_layout = StatusWidget()
        patient_status_bar_widget.setLayout(patient_status_widget_layout)
        # For testing
        patient_status_bar_widget.setFixedWidth(50)

        """     3D Models   """
        three_d_models_bar_layout = QVBoxLayout()
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
