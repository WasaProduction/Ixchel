from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPixmap, QIcon
from assets.icons.buttons.button_paths import ButtonPaths


class Frame(QWidget):
    def __init__(self, parent=None, name=None, button_path=None, text_labels=None):
        super().__init__(parent)
        self.name = name
        if button_path is None:
            path = ButtonPaths().default
        else:
            path = button_path
        self.icon = QIcon(QPixmap(path))
        self.text_labels = text_labels
