from UI.Frames.frame import Frame
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QComboBox
from PyQt6.QtCore import pyqtSlot
from UI.Frames.editing_area.editingarea import EditingArea


class PrescriptionFrame(Frame):
    def __init__(self, parent=None, button_paths=None):
        super().__init__(parent, button_path=button_paths.diagnosis)
        self.name = 'Diagnosis'
        # Stacked view
        self.my_editing_area = EditingArea(self)
        # Button
        save_button = QPushButton("Save")
        save_button.clicked.connect(lambda: self.retrieve_data())
        # Combobox
        self.my_options = QComboBox()
        # Add items to the combobox
        self.my_options.addItems(list(self.my_editing_area.containing_frames.keys()))
        # Change frame when an option is selected
        self.my_options.activated.connect(self.change_frame)

        # Button Combobox container layout
        options_layout = QHBoxLayout()
        options_layout.addWidget(self.my_options)
        options_layout.addWidget(save_button)
        # Button Combobox container widget
        options_container_widget = QWidget()
        options_container_widget.setLayout(options_layout)
        # Stacked view, Button, Combobox container layout
        vertical_container_layout = QVBoxLayout()
        vertical_container_layout.addWidget(options_container_widget)
        vertical_container_layout.addWidget(self.my_editing_area)
        # Setting the layout of this widget
        self.setLayout(vertical_container_layout)

    @pyqtSlot()
    def change_frame(self):
        #   Change index of current frame
        self.my_editing_area.setCurrentIndex(self.my_editing_area.containing_frames[self.my_options.currentText()])

    @pyqtSlot()
    def retrieve_data(self):
        print('Container recieved', self.my_editing_area.retrieve_data())
        return self.my_editing_area.retrieve_data()
