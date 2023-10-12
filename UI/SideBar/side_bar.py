from PyQt6.QtWidgets import QWidget, QVBoxLayout, QToolButton, QSizePolicy
from PyQt6.QtCore import Qt


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
            new_button = QToolButton()
            #   Button text
            new_button.setText(self.frame_stack.widget(index).name)
            #   Button tooltip
            new_button.setToolTip(self.frame_stack.widget(index).name)
            #   Button icon
            new_button.setIcon(self.frame_stack.widget(index).icon)
            #   Icon atop
            new_button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
            #   Button action
            new_button.clicked.connect(lambda _, l_index=index: self.frame_stack_change(l_index))
            #   Use horizontal space while keeping the preferred vertical size
            new_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
            #   Remove border
            # new_button.setStyleSheet("border: none;")
            #   Add button to array
            button_arr.append(new_button)
        #   Return first widget atop the stack
        self.frame_stack_change(0)
        #   Return buttons array
        return button_arr

    def frame_stack_change(self, destination):
        self.frame_stack.setCurrentIndex(destination)

    def add_buttons(self):
        #   Add buttons to layout
        for button in self.create_buttons():
            self.sidebar_layout.setStretchFactor(button, 1)
            self.sidebar_layout.addWidget(button)

    """     UI      """

    def init_ui(self):
        self.sidebar_layout.setContentsMargins(0, 0, 0, 0)
        self.sidebar_layout.addStretch()
        self.sidebar_layout.setSpacing(10)
        self.setLayout(self.sidebar_layout)
