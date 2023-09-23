from PyQt6.QtWidgets import QComboBox


class CustomComboBox(QComboBox):
    # Built to ignore key events based on the key
    def __init__(self, parent=None, my_list=None, my_current_text=None):
        super().__init__(parent)
        self.addItems(my_list)
        if my_current_text is not None:
            self.setCurrentText(my_current_text)
        else:
            self.setCurrentIndex(-1)
            self.setPlaceholderText('Please select an option')
