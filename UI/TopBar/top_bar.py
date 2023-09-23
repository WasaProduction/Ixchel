from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QHBoxLayout, QLineEdit


class TopBar(QWidget):
    def __init__(self):
        super().__init__()
        # Search bar
        searchbar = QLineEdit()
        searchbar.setPlaceholderText('Search')
        search_button = QPushButton('SearchGlass')
        searchbar_container_layout = QHBoxLayout()
        searchbar_container_layout.addWidget(searchbar)
        searchbar_container_layout.addWidget(search_button)
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
        patient_name_label = QLabel('LastName1 LastName2 Name')
        username_label = QLabel('Hello you')
        general_container_layout = QHBoxLayout()
        general_container_layout.addWidget(patient_name_label)
        general_container_layout.addStretch(5)
        general_container_layout.addWidget(searchbar_container_widget)
        general_container_layout.addStretch(5)
        general_container_layout.addWidget(username_label)
        general_container_layout.addWidget(button_container_widget)
        # Set layout
        self.setLayout(general_container_layout)
