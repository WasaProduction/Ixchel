from UI.Frames.frame import Frame
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout
from UI.Widgets.status_widget_layout import StatusWidget
from UI.Widgets.icons.sex_icon import SexIconWidget
from UI.Widgets.summary_scroll_area import SummaryScrollArea
from UI.Widgets.patient_name import PatientName
from UI.TwoD.graphic_view import GraphicView


class SummaryFrame(Frame):
    def __init__(self, parent=None, patient=None, button_paths=None, text_labels=None):
        super().__init__(parent, button_path=button_paths.summary, text_labels=text_labels)
        self.name = self.text_labels.summary_btn
        self.patient = patient
        self.init_ui()

    def update_summary(self):
        self.patient_status_bar_widget.update_statuses()
        # self.patient_general_information_widget.update_widget()
        pass
        # self.patient_allergies_widget.update_allergies()

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

        """     Section Container   """
        patient_general_info_layout = QVBoxLayout()
        self.summary_scroll_area = SummaryScrollArea(self, self.text_labels, self.patient)
        patient_general_info_layout.addWidget(patient_essential_data_widget)
        patient_general_info_layout.addWidget(self.summary_scroll_area)
        patient_general_info_layout.setContentsMargins(0, 0, 0, 0)
        #patient_general_info_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        section_container = QWidget()
        section_container.setLayout(patient_general_info_layout)

        """     Patient statusbar   """
        self.patient_status_bar_widget = StatusWidget()
        # For testing
        self.patient_status_bar_widget.setFixedWidth(50)

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
        container_layout.addWidget(section_container, 7)
        container_layout.addWidget(self.patient_status_bar_widget, 1)
        container_layout.addWidget(three_d_models_bar_widget, 2)
        self.setLayout(container_layout)
