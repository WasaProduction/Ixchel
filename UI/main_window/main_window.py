from PyQt6.QtWidgets import QWidget, QMainWindow, QStackedWidget, QVBoxLayout,  QHBoxLayout
from UI.Frames.summary_frame import SummaryFrame
from UI.Frames.prescription_frame import PrescriptionFrame
from UI.Frames.schedule_frame import ScheduleFrame
from config_files.startup_check import StartupCheck
from UI.TopBar.top_bar import TopBar
from UI.SideBar.side_bar import SideBar
from mongodb.read.get_patient import GetPatient
from assets.icons.buttons.button_paths import ButtonPaths
from mongodb.read.get_text_labels import GetTextLabels


class MainWindow(QMainWindow):
    def __init__(self):
        # Look for all required files
        StartupCheck()
        super().__init__()
        #   Setting window title
        self.setWindowTitle("Ixchel")
        #   Setting window properties
        self.Width = 800
        self.height = int(0.618 * self.Width)
        self.resize(self.Width, self.height)
        self.patient = GetPatient('JaimeGQ')

        #   EN = 0
        #   ES = 1
        self.text_labels = GetTextLabels(0)
        self.top_bar = TopBar(self, self.text_labels)

        button_paths = ButtonPaths()

        """     Frames      """
        self.frame_prescription = PrescriptionFrame(self, button_paths, self.text_labels)
        self.frame_agenda = ScheduleFrame(self, button_paths, self.text_labels)
        self.frame_summary = SummaryFrame(self, self.patient, button_paths, self.text_labels)

        self.init_ui()

    def init_ui(self):
        """Stack"""
        stacked_frames = QStackedWidget()
        stacked_frames.addWidget(self.frame_summary)
        stacked_frames.addWidget(self.frame_prescription)
        stacked_frames.addWidget(self.frame_agenda)
        # Main horizontal widgets
        main_h_layout = QHBoxLayout()
        # main_h_layout.addWidget(sidebar_widget)
        main_h_layout.addWidget(SideBar(stacked_frames), 1)
        main_h_layout.addWidget(stacked_frames, 9)
        main_h_layout.setSpacing(0)
        main_h_layout.setContentsMargins(0, 0, 0, 0)
        main_h_widget = QWidget()
        main_h_widget.setLayout(main_h_layout)
        # Main vertical widgets
        main_v_layout = QVBoxLayout()
        self.top_bar.patient_signal.connect(self.update_patient)
        main_v_layout.addWidget(self.top_bar, 1)

        main_v_layout.addWidget(main_h_widget, 9)

        main_widget = QWidget()
        main_widget.setLayout(main_v_layout)

        self.setCentralWidget(main_widget)
        #   Prevent any widget from being the focus.
        self.setFocus()

    def update_patient(self):
        self.patient = self.top_bar.patient
        self.frame_summary.update_summary(self.patient)
