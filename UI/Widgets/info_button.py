from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import pyqtSignal


class InfoButton(QPushButton):
    clicked_signal = pyqtSignal()

    def __init__(self, parent=None, tooltip='Info'):
        super().__init__(parent)
        #   Emit signal when clicked.
        self.clicked.connect(lambda: self.clicked_signal.emit())
        self.folder = '/Users/jaimegonzalezquirarte/PycharmProjects/Ixchel/assets/icons/buttons/'
        #   Set tool tip
        self.setToolTip('Info')
        #   Set custom icon.
        self.setIcon(QIcon(self.folder + "info_icon.png"))
        #   Remove border
        self.setStyleSheet('border-style: none;')
        #   Tooltip
        self.setToolTip(tooltip)
