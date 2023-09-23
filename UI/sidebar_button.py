from PyQt6.QtWidgets import QAbstractButton
from PyQt6.QtGui import QPainter
from PyQt6.QtCore import QSize


class SideBarButton(QAbstractButton):
    def __init__(self, pixmap, tooltip, parent=None):
        super(SideBarButton, self).__init__(parent)
        self.pixmap = pixmap
        self.setToolTip(tooltip)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(event.rect(), self.pixmap)
        if self.isDown():
            print("pico")

    def sizeHint(self):
        return QSize(30, 30)
