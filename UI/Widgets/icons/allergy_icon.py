from PyQt6.QtWidgets import QVBoxLayout, QGraphicsColorizeEffect, QAbstractButton
from PyQt6.QtGui import QPixmap, QColor, QPainter


class AllergyIcon(QAbstractButton):
    def __init__(self, allergy):
        super().__init__()
        my_layout = QVBoxLayout()
        effect = QGraphicsColorizeEffect()
        # Pick category/icon
        if allergy.category == 1:
            # Drugs
            self.pixmap = QPixmap("/Users/jaimegonzalezquirarte/Desktop/App/Allergy_icons/Drug.png")
        elif allergy.category == 2:
            # Food
            self.pixmap = QPixmap("/Users/jaimegonzalezquirarte/Desktop/App/Allergy_icons/Food.png")
        elif allergy.category == 3:
            # Fauna
            self.pixmap = QPixmap("/Users/jaimegonzalezquirarte/Desktop/App/Allergy_icons/Fauna.png")
        else:
            # Default
            self.pixmap = QPixmap("/Users/jaimegonzalezquirarte/Desktop/App/Allergy_icons/Default.png")
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
