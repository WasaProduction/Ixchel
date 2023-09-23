from PyQt6.QtWidgets import QAbstractButton, QSizePolicy
from PyQt6.QtGui import QPainter, QPixmap
from PyQt6.QtCore import QSize


class SexIconWidget(QAbstractButton):
    def __init__(self, sex, parent=None):
        super(SexIconWidget, self).__init__(parent)
        if sex == 1:
            self.pixmap = QPixmap("/Users/jaimegonzalezquirarte/Desktop/App/Gender-Symbol_Female.png")
            self.setToolTip("Man")
        elif sex == 2:
            self.pixmap = QPixmap("/Users/jaimegonzalezquirarte/Desktop/App/Gender-Symbol_Male.png")
            self.setToolTip("Woman")
        elif sex == 3:
            self.pixmap = QPixmap("/Users/jaimegonzalezquirarte/Desktop/App/Gender-Symbol_Female.png")
            self.setToolTip("Trans-Woman")
        elif sex == 4:
            self.pixmap = QPixmap("/Users/jaimegonzalezquirarte/Desktop/App/Gender-Symbol_Male.png")
            self.setToolTip("Trans-Man")
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        # self.pressed.connect(self.update)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(event.rect(), self.pixmap)
        if self.isDown():
            print("pico")

    def enterEvent(self, event):
        # Hover enter
        print("Entro")

    def leaveEvent(self, event):
        # Hover exit
        print("Salio")

    def sizeHint(self):
        return QSize(30, 30)
