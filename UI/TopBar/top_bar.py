from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QGridLayout
from PyQt6.QtCore import QTimer, QDateTime, QTime, pyqtSignal
from mongodb.read.get_patient import GetPatient
from data_models.patient.model_patient import ModelPatient
from UI.Widgets.custom_search_bar import CustomSearchBar


class TopBar(QWidget):
    patient_signal = pyqtSignal(ModelPatient)

    def __init__(self, parent=None, text_labels=None):
        super().__init__(parent)
        self.text_labels = text_labels
        self.patient = GetPatient(parent)
        #   Connect signal to a handler
        self.patient_signal.connect(self.handle_patient_signal)
        """     Widgets     """
        #   Patient
        self.patient_name_label = QLabel('Grevious')
        #   Searchbar
        self.searchbar = CustomSearchBar(self, self.text_labels.search)
        #   Search button
        self.search_button = QPushButton(self.text_labels.search)
        self.search_button.clicked.connect(self.search_user)
        #   Doc
        self.greetings_str = 'Hello there'
        self.username = 'General Kenobi!'
        self.greetings_lbl = QLabel(self.greetings_str)
        """     Button group        """
        #   Notifications
        self.notifications_button = QPushButton(self.text_labels.notifications)
        self.notifications_button.clicked.connect(self.open_notifications)
        #   User
        self.user_details_button = QPushButton(self.text_labels.user)
        self.user_details_button.clicked.connect(self.open_user_details)
        #   Config
        self.config_button = QPushButton(self.text_labels.config)
        self.config_button.clicked.connect(self.open_config)
        """     UI      """
        #   Timer
        self.timer = QTimer(self)
        self.config_timer(60000)
        self.timer.timeout.connect(self.update_greetings)
        self.update_greetings()
        # Layout
        self.layout = QGridLayout()
        self.customize_grid()
        self.setLayout(self.layout)

    def open_notifications(self):
        pass

    def open_user_details(self):
        pass

    def open_config(self):
        pass

    def config_timer(self, time=3600000):
        #   Defaults to 1 hour (ms).
        self.timer.start(time)

    def update_greetings(self):
        # Update the label with the current time.
        self.greetings_lbl.setText(self.determine_greeting() + ' ' + self.username)

    def determine_greeting(self):
        #   Current time.
        now = QDateTime.currentDateTime().time()
        #   Tolerance to update greetings 10 s.
        tolerance = 10000
        #   Day parts.
        midnight = QTime(0, 0)
        sunrise = QTime(5, 0)
        noon = QTime(12, 0)
        sunset = QTime(17, 0)
        #   Morning.
        if sunrise < now < noon:
            self.config_timer((now.secsTo(noon) * 1000) + tolerance)
            return self.text_labels.morning
        #   Afternoon.
        elif noon < now < sunset:
            self.config_timer((now.secsTo(sunset) * 1000) + tolerance)
            return self.text_labels.afternoon
        #   Evening.
        elif sunset < now < midnight:
            self.config_timer((now.secsTo(midnight) * 1000) + tolerance)
            return self.text_labels.evening
        #   Night.
        elif midnight < now < sunrise:
            self.config_timer((now.secsTo(sunrise) * 1000) + tolerance)
            return self.text_labels.night

    def handle_patient_signal(self):
        return self.patient

    def search_user(self):
        #   Search for patient.
        self.patient.update_model(self.searchbar.text())
        #   Validate if patient is found.
        if self.patient.user_id:
            # Emit signal with data.
            self.patient_signal.emit(self.patient)
            #   Update patient label
            self.update_patient_lbl()
        else:
            #   User not found.
            self.searchbar.shake()

    def update_patient_lbl(self):
        full_name = self.patient.name + ' ' + self.patient.lastname_1 + ' ' + self.patient.lastname_2
        self.patient_name_label.setText(full_name)
        pass

    def customize_grid(self):
        self.layout.addWidget(self.patient_name_label, 0, 0, 1, 5)
        self.layout.addWidget(self.searchbar, 0, 6, 1, 5)
        self.layout.addWidget(self.search_button, 0, 11, 1, 1)
        self.layout.addWidget(self.greetings_lbl, 0, 17, 1, 5)
        self.layout.addWidget(self.notifications_button, 0, 23, 1, 1)
        self.layout.addWidget(self.user_details_button, 0, 25, 1, 1)
        self.layout.addWidget(self.config_button, 0, 27, 1, 1)
