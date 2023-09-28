from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QPainter, QIcon
from PyQt6.QtCore import QSize, Qt


class BoneButton(QPushButton):
    def __init__(self, pixmap, parent=None, text=None, color=None, opacity=0.5, width=30, height=30):
        super(BoneButton, self).__init__(parent)
        self.text = text
        self.color = color
        self.opacity = opacity
        self.width = width
        self.height = height
        self.pixmap = pixmap
        self.tinted_pixmap = pixmap
        self.init_ui()
        #   Action
        self.clicked.connect(self.button_clicked)

    def button_clicked(self):
        #   TODO Bone button: implement actions when clicked
        pass

    def sizeHint(self):
        return QSize(self.width, self.height)

    def update_button(self, color=None, opacity=0.5):
        #   Update color & opacity
        self.color = color
        self.opacity = opacity
        #   Toggle tint
        self.toggle_tint()

    def toggle_tint(self):
        #   Evaluate if a tint must be applied or removed
        if self.color is None:
            #   Set the original pixmap as the button's icon
            icon = QIcon(self.pixmap)
            # Toggle the tint state
        else:
            #   Tint to apply to the pixmap
            tint_color = self.color
            #   Modify opacity
            tint_color.setAlphaF(self.opacity)
            self.tinted_pixmap = self.apply_tint(tint_color)
            #   Set the tinted pixmap as the button's icon
            icon = QIcon(self.tinted_pixmap)
        #   Set icon
        self.setIcon(icon)

    def apply_tint(self, tint_color):
        #   Create a copy of the original pixmap
        new_pixmap = self.pixmap.copy()
        #   Create a QPainter to apply the tint only to non-transparent pixels
        painter = QPainter(new_pixmap)
        #   Traverse all pixels
        for x in range(new_pixmap.width()):
            for y in range(new_pixmap.height()):
                pixel_color = self.pixmap.toImage().pixelColor(x, y)
                #   Check if pixel is not transparent
                if pixel_color.alpha() > 0:
                    painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceOver)
                    painter.fillRect(x, y, 1, 1, tint_color)
        painter.end()
        return new_pixmap

    """     UI      """
    def init_ui(self):
        #   Set tooltip if there's text
        if self.text is not None:
            self.setToolTip(self.text)
        #   Pixmap size
        size = QSize(self.width, self.height)
        #   Scale pixmap
        bone_pixmap = self.pixmap.scaled(size, Qt.AspectRatioMode.KeepAspectRatio)
        #   Set image into button
        icon = QIcon(bone_pixmap)
        #   Icon size
        self.setIconSize(bone_pixmap.size())
        #   Set icon to self.
        self.setIcon(icon)
        #   Remove border
        self.setFlat(True)
        # Transparent background
        self.setStyleSheet("background-color: transparent; border: none;")
