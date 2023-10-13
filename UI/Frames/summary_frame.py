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
        #   Name
        self.patient_name_label = PatientName(self, name=self.patient.name, lastname_1=self.patient.lastname_1,
                                              lastname_2=self.patient.lastname_2)
        print('test', self.patient.immutables.birthday)
        self.patient_age_label = QLabel(self.patient.immutables.birthday)
        self.customize_age_lbl()
        #
        self.patient_blood_label = QLabel("O+")
        self.customize_blood_lbl()
        #   Summary scroll area
        self.summary_scroll_area = SummaryScrollArea(self, self.text_labels, self.patient)
        #   Status bar
        self.patient_status_bar_widget = StatusWidget()
        self.customize_status_bar()
        #   Models
        self.skeleton_view = GraphicView(self)
        self.init_ui()

    def update_summary(self, patient=None):
        #   Update patient obj
        self.patient = patient
        """     Update widgets      """
        #   Update name
        self.patient_name_label.update_text(self.patient.name, self.patient.lastname_1, self.patient.lastname_2)
        #   Update status bar
        self.patient_status_bar_widget.update_statuses()
        # self.patient_general_information_widget.update_widget()
        # self.patient_allergies_widget.update_allergies()
        pass

    def update_blood_type(self):
        self.patient_blood_label.setText()

    def customize_status_bar(self):
        self.patient_status_bar_widget.setFixedWidth(50)

    def customize_age_lbl(self):
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
