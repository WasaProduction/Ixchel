from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QColor, QIcon, QPainter


class AllergyIcon(QPushButton):
    def __init__(self, allergy):
        super().__init__()
        folder = '/Users/jaimegonzalezquirarte/PycharmProjects/Ixchel/assets/icons/allergies/'
        # Pick category/icon
        if allergy.category == 0:
            # Flora
            self.my_icon = QIcon(folder + "Flora.png")
        elif allergy.category == 1:
            # Fauna
            self.my_icon = QIcon(folder + "Fauna.png")
        elif allergy.category == 2:
            # Ambient
            self.my_icon = QIcon(folder + "Default.png")
        elif allergy.category == 3:
            # Substances
            self.my_icon = QIcon(folder + "Drug.png")
        elif allergy.category == 4:
            # Food
            self.my_icon = QIcon(folder + "Food.png")
        else:
            # Other
            self.my_icon = QIcon(folder + "Default.png")
        # Pick color
        if allergy.severity == 1:
            # Green
            self.my_color = QColor(13, 135, 0)
        elif allergy.severity == 2:
            # Yellow
            self.my_color = QColor(250, 250, 0)
        elif allergy.severity == 3:
            # Orange
            self.my_color = QColor(229, 98, 0)
        elif allergy.severity == 4:
            # Red
            self.my_color = QColor(173, 0, 0)
        else:
            # Red
            self.my_color = QColor(173, 0, 0)
        #   Tint icon.
        self.my_icon = self.color_overlay_icon(self.my_icon)
        #   Set icon.
        self.setIcon(self.my_icon)
        #   Remove border
        self.setStyleSheet('border: None')

    def color_overlay_icon(self, icon):
        pixmap = icon.pixmap(icon.actualSize(self.iconSize()))
        painter = QPainter(pixmap)
        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceIn)
        painter.fillRect(pixmap.rect(), self.my_color)
        painter.end()
        return QIcon(pixmap)
