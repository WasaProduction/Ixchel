from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout
from PySide6.QtCore import Slot
from PyQt6.QtGui import QPixmap
from os import listdir


class SideBar(QWidget):
    def __init__(self, frame_stack):
        super().__init__()
        self.frame_stack = frame_stack
        self.sidebar_layout = QVBoxLayout()
        self.add_buttons()
        self.set_layout_properties()

    def create_buttons(self):
        images_folder_dir = "/Users/jaimegonzalezquirarte/PycharmProjects/Ixchel/assets/icons/buttons"
        button_images_dict = {}
        for index, image in enumerate(listdir(images_folder_dir)):
            # check if the image ends with png
            if image.endswith(".png"):
                button_images_dict[index] = (image.split('.')[0], QPixmap(image))

        button_arr = []
        # One per frame
        frames_folder_dir = "/Users/jaimegonzalezquirarte/PycharmProjects/Ixchel/UI/Frame"
        listdir(images_folder_dir)
        for index in range(self.frame_stack.count()):
            new_button = QPushButton('button {}'.format(index))
            new_button.clicked.connect(lambda _, l_index=index: self.frame_stack_change(self.frame_stack, l_index))
            button_arr.append(new_button)
            del new_button
        return button_arr

    @Slot()
    def frame_stack_change(self, stack, destination):
        stack.setCurrentIndex(destination)

    def add_buttons(self):
        for button in self.create_buttons():
            self.sidebar_layout.addWidget(button)

    def set_layout_properties(self):
        self.sidebar_layout.addStretch(5)
        self.sidebar_layout.setSpacing(20)
        self.setLayout(self.sidebar_layout)
