from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtCore import Qt


class CustomLineEdit(QLineEdit):
    # Built to ignore key events based on the key
    def __init__(self, parent=None, key='Insert key value', value=None):
        super().__init__(parent)
        self.setFrame(True)
        #  Set the tooltip to provide some visual aid for complete fields
        self.setToolTip(key)
        # Set placeholder in case of a None value
        if value is None:
            self.setPlaceholderText(key)
        else:
            self.setPlaceholderText(key)

    def keyPressEvent(self, event):
        if (
                (event.key() in (Qt.Key.Key_Right, Qt.Key.Key_Home)
                    and self.cursorPosition() == len(self.text()))
                or
                (event.key() in (Qt.Key.Key_Left, Qt.Key.Key_End) and self.cursorPosition() == 0)
        ):
            event.ignore()
            return
        super().keyPressEvent(event)
