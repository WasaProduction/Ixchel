from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class DayHeader(QWidget):
    def __init__(self, parent=None, number=None, day_name=None):
        super().__init__(parent)
        day_names = ['Monday', 'Tuesday', 'Thursday', 'Wednesday', 'Friday', 'Saturday', 'Sunday']
        #   Create labels single digits preceded by 0
        self.number_label = QLabel(str(number) if number > 10 else '0'.join(str(number)))
        self.string_label = QLabel(day_names[day_name])
        #   Set labels UI
        self.set_labels_ui()
        #   Create my layout
        self.my_layout = QVBoxLayout()
        #   Set Layout
        self.init_ui()

    """     UI      """

    def init_ui(self):
        #   Add widgets
        self.my_layout.addWidget(self.number_label)
        self.my_layout.addWidget(self.string_label)
        self.my_layout.addStretch()
        """     Customize UI        """
        self.my_layout.setSpacing(0)
        self.my_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #   Apply layout
        self.setLayout(self.my_layout)
        #   Custom self
        self.setMinimumSize(120, 80)
        self.setMaximumSize(130, 90)


    def update_number_text(self, number=None, text=None):
        #   Change day number
        if number is not None:
            self.number_label.setText(str(number))
        #   Change day name
        if text is not None:
            self.string_label.setText(text)

    def set_labels_ui(self):
        #   Font
        my_font = QFont('Arial', 30)
        my_font.setBold(True)
        """     Number      """
        self.number_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.number_label.resize(100, 200)
        self.number_label.setFont(my_font)
        """     String      """
        #   Modify font
        name_font = QFont('Arial', 5)
        name_font.setBold(True)
        self.string_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.string_label.resize(20, 40)
        self.number_label.setFont(my_font)
