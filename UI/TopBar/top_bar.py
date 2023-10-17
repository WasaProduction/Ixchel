from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QHBoxLayout, QLineEdit
from UI.Widgets.Alerts.error import Error
from mongodb.read.get_patient import GetPatient


class TopBar(QWidget):
    def __init__(self):
        super().__init__()
        self.patient = GetPatient()
        # Search bar
        self.searchbar = QLineEdit()
        self.searchbar.setPlaceholderText('Search')
        self.search_button = QPushButton('SearchGlass')
        self.search_button.clicked.connect(self.search_user)
        searchbar_container_layout = QHBoxLayout()
        searchbar_container_layout.addWidget(self.searchbar)
        searchbar_container_layout.addWidget(self.search_button)
        searchbar_container_widget = QWidget()
        searchbar_container_widget.setLayout(searchbar_container_layout)
        # Button group
        notifications_button = QPushButton('Notifications')
        user_details_button = QPushButton('User')
        config_button = QPushButton('Config')
        button_container_layout = QHBoxLayout()
        button_container_layout.addWidget(notifications_button)
        button_container_layout.addWidget(user_details_button)
        button_container_layout.addWidget(config_button)
        button_container_widget = QWidget()
        button_container_widget.setLayout(button_container_layout)
        # Top bar whole
        self.patient_name_label = QLabel('')
        self.username_label = QLabel('Hello you')
        general_container_layout = QHBoxLayout()
        general_container_layout.addWidget(self.patient_name_label)
        general_container_layout.addStretch(5)
        general_container_layout.addWidget(searchbar_container_widget)
        general_container_layout.addStretch(5)
        general_container_layout.addWidget(self.username_label)
        general_container_layout.addWidget(button_container_widget)
        # Set layout
        self.setLayout(general_container_layout)

    def search_user(self):
        #   Search for patient.
        print(self.searchbar.text())
        self.patient.update_model(self.searchbar.text())
        if self.patient.user_id:
            #   Update user
            self.update_patient_lbl()
            self.update_doc_lbl()
            #   https://www.pythonguis.com/tutorials/pyqt6-signals-slots-events/
        else:
            #   User not found.
            Error(self, 'Error', 'User not found')
        pass

    def update_patient_lbl(self):
        self.patient_name_label.setText('Gonzalez Quirarte Jaime')
        pass

    def update_doc_lbl(self):
        self.username_label.setText('Ciao voçe')
        pass


