from UI.Frames.frame import Frame
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import datetime
from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout
from UI.Widgets.status_bar_widget import StatusBarWidget
from UI.Widgets.icons.sex_icon import SexIconWidget
from UI.Widgets.summary_scroll_area import SummaryScrollArea
from UI.Widgets.patient_name import PatientName
from UI.TwoD.graphic_view import GraphicView


class SummaryFrame(Frame):
    def __init__(self, parent=None, patient=None, button_paths=None, text_labels=None):
        super().__init__(parent, button_path=button_paths.summary, text_labels=text_labels)
        self.name = self.text_labels.summary_btn
        self.patient = patient
        #   Name
        self.patient_name_label = PatientName(self, name=self.patient.name, lastname_1=self.patient.lastname_1,
                                              lastname_2=self.patient.lastname_2)
        #   Age
        self.patient_age_label = QLabel(str(self.calculate_age(self.patient.immutables.birthday)))
        self.customize_age_lbl()
        #
        self.patient_blood_label = QLabel(self.patient.immutables.blood_type)
        self.customize_blood_lbl()
        #   Summary scroll area
        self.summary_scroll_area = SummaryScrollArea(self, self.text_labels, self.patient)
        #   Status bar
        self.patient_status_bar_widget = StatusBarWidget(self, self.patient)
        self.customize_status_bar()
        #   Models
        self.skeleton_view = GraphicView(self)
        self.init_ui()

    @staticmethod
    def calculate_age(birthdate):
        current_date = datetime.datetime.now()
        age = current_date.year - birthdate.year - ((current_date.month, current_date.day) <
                                                    (birthdate.month, birthdate.day))
        return age

    def update_summary(self, patient=None):
        #   Update patient obj
        self.patient = patient
        """     Update widgets      """
        #   Update name
        self.patient_name_label.update_text(self.patient.name, self.patient.lastname_1, self.patient.lastname_2)
        #   Update age
        self.patient_age_label.setText(str(self.calculate_age(self.patient.immutables.birthday)))
        #   Update blood type
        self.patient_blood_label.setText(self.patient.immutables.blood_type)
        #   Update status bar
        self.patient_status_bar_widget.update_statuses()
        #   Update scroll area
        self.summary_scroll_area.update_summary_scroll_area(self.patient)
        """     Update models       """
        #   Update skeleton

    def customize_status_bar(self):
        self.patient_status_bar_widget.setFixedWidth(50)

    def customize_age_lbl(self):
        age_label_font = QFont('Arial', 20)
        age_label_font.setBold(True)
        self.patient_age_label.setFont(age_label_font)
        self.patient_age_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

    def customize_blood_lbl(self):
        blood_label_font = QFont('Arial', 30)
        blood_label_font.setBold(True)
        self.patient_blood_label.setFont(blood_label_font)

    def init_ui(self):
        """General data"""
        # First row
        patient_essential_data_h_layout = QHBoxLayout()
        patient_essential_data_h_layout.setContentsMargins(0, 0, 0, 0)
        patient_essential_data_h_layout.addWidget(self.patient_name_label)
        patient_essential_data_h_layout.addWidget(self.patient_blood_label)
        patient_essential_data_h_layout.addWidget(SexIconWidget(2))
        patient_essential_data_h_widget = QWidget()
        patient_essential_data_h_widget.setLayout(patient_essential_data_h_layout)
        patient_essential_data_h_widget.setFixedHeight(80)

        # First second row
        patient_essential_data_v_layout = QVBoxLayout()
        patient_essential_data_v_layout.setContentsMargins(0, 0, 0, 0)
        patient_essential_data_v_layout.addWidget(patient_essential_data_h_widget)
        patient_essential_data_v_layout.addWidget(self.patient_age_label)
        patient_essential_data_widget = QWidget()
        patient_essential_data_widget.setLayout(patient_essential_data_v_layout)
        patient_essential_data_widget.setFixedHeight(100)

        """     Section Container   """
        patient_general_info_layout = QVBoxLayout()
        patient_general_info_layout.addWidget(patient_essential_data_widget)
        patient_general_info_layout.addWidget(self.summary_scroll_area)
        patient_general_info_layout.setContentsMargins(0, 0, 0, 0)
        section_container = QWidget()
        section_container.setLayout(patient_general_info_layout)

        """     Models   """
        #   Models container
        three_d_models_bar_layout = QVBoxLayout()
        #   Skeleton
        three_d_models_bar_layout.addWidget(self.skeleton_view)
        #   Organs
        #   Muscles
        #   Stack up
        three_d_models_bar_layout.addStretch()
        three_d_models_bar_widget = QWidget()
        three_d_models_bar_widget.setLayout(three_d_models_bar_layout)

        """     Add main widgets to the container        """
        container_layout = QHBoxLayout()
        container_layout.addWidget(section_container, 7)
        container_layout.addWidget(self.patient_status_bar_widget, 1)
        container_layout.addWidget(three_d_models_bar_widget, 2)
        self.setLayout(container_layout)
