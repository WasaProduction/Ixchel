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
        # Setting window title
        self.setWindowTitle("Ixchel")
        # Setting window properties
        self.Width = 800
        self.height = int(0.618 * self.Width)
        self.resize(self.Width, self.height)
        self.init_ui()

    def init_ui(self):
        button_paths = ButtonPaths()
        text_labels = GetTextLabels()
        patient = GetPatient('JaimeGq')
        """     Frames      """
        frame_prescription = PrescriptionFrame(self, button_paths, text_labels)
        frame_agenda = ScheduleFrame(self, button_paths, text_labels)
        frame_summary = SummaryFrame(self, patient, button_paths, text_labels)

        """Stack"""
        stacked_frames = QStackedWidget()
        stacked_frames.addWidget(frame_summary)
        stacked_frames.addWidget(frame_prescription)
        stacked_frames.addWidget(frame_agenda)

        # Main horizontal widgets
        main_h_layout = QHBoxLayout()
        # main_h_layout.addWidget(sidebar_widget)
        main_h_layout.addWidget(SideBar(stacked_frames))
        main_h_layout.addWidget(stacked_frames)
        main_h_widget = QWidget()
        main_h_widget.setLayout(main_h_layout)
        # Main vertical widgets
        main_v_layout = QVBoxLayout()
        main_v_layout.addWidget(TopBar())
        main_v_layout.addWidget(main_h_widget)

        main_widget = QWidget()
        main_widget.setLayout(main_v_layout)

        self.setCentralWidget(main_widget)
