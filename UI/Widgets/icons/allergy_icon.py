from PyQt6.QtWidgets import QVBoxLayout, QGraphicsColorizeEffect, QAbstractButton
from PyQt6.QtGui import QPixmap, QColor, QPainter


class AllergyIcon(QAbstractButton):
    def __init__(self, allergy):
        super().__init__()
        my_layout = QVBoxLayout()
        effect = QGraphicsColorizeEffect()
        folder = '/Users/jaimegonzalezquirarte/PycharmProjects/Ixchel/assets/icons/allergies/'
        # Pick category/icon
        if allergy.category == 0:
            # Flora
            self.pixmap = QPixmap(folder + "Flora.png")
        elif allergy.category == 1:
            # Fauna
            self.pixmap = QPixmap(folder + "Fauna.png")
        elif allergy.category == 2:
            # Ambient
            self.pixmap = QPixmap(folder + "Default.png")
        elif allergy.category == 3:
            # Substances
            self.pixmap = QPixmap(folder + "Drug.png")
        elif allergy.category == 4:
            # Food
            self.pixmap = QPixmap(folder + "Food.png")
        else:
            # Other
            self.pixmap = QPixmap(folder + "Default.png")
        # Pick color
        if allergy.severity == 1:
            # Green
            effect.setColor(QColor(13, 135, 0))
        elif allergy.severity == 2:
            # Yellow
            effect.setColor(QColor(250, 250, 0))
        elif allergy.severity == 3:
            # Orange
            effect.setColor(QColor(229, 98, 0))
        elif allergy.severity == 4:
            # Red
            effect.setColor(QColor(173, 0, 0))
        else:
            # Red
            effect.setColor(QColor(173, 0, 0))

        self.setGraphicsEffect(effect)
        self.setLayout(my_layout)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(event.rect(), self.pixmap)
        if self.isDown():
            print("pico")
