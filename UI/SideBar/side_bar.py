from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout
from PySide6.QtCore import Slot


class SideBar(QWidget):
    def __init__(self, frame_stack):
        super().__init__()
        self.frame_stack = frame_stack
        self.sidebar_layout = QVBoxLayout()
        #   Add buttons into layout
        self.add_buttons()
        self.init_ui()

    def create_buttons(self):
        #   Buttons array
        button_arr = []
        #   Create a button per frame.
        for index in range(self.frame_stack.count()):
            #   Change widget atop
            self.frame_stack_change(index)
            #   Button
            new_button = QPushButton()
            #   Button text
            new_button.setText(self.frame_stack.widget(index).name)
            #   Button tooltip
            new_button.setToolTip(self.frame_stack.widget(index).name)
            #   Button icon
            new_button.setIcon(self.frame_stack.widget(index).icon)
            #   Button action
            new_button.clicked.connect(lambda _, l_index=index: self.frame_stack_change(l_index))
            #   Add button to array
            button_arr.append(new_button)
            #   Delete button
            del new_button
        #   Return first widget atop the stack
        self.frame_stack_change(0)
        #   Return buttons array
        return button_arr

    @Slot()
    def frame_stack_change(self, destination):
        self.frame_stack.setCurrentIndex(destination)

    def add_buttons(self):
        for button in self.create_buttons():
            self.sidebar_layout.addWidget(button)

    """     UI      """

    def init_ui(self):
        self.sidebar_layout.addStretch(5)
        self.sidebar_layout.setSpacing(20)
        self.setLayout(self.sidebar_layout)
