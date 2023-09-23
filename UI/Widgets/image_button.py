from PyQt6.QtWidgets import QAbstractButton
from PyQt6.QtGui import QPainter, QColor, QPixmap
from PyQt6.QtCore import QSize, Qt


class ImageButton(QAbstractButton):
    def __init__(self, pixmap, parent=None, text=None, color=None, opacity=None, width=30, height=30):
        self.width = width
        self.height = height
        super(ImageButton, self).__init__(parent)
        if color is None:
            self.pixmap = pixmap
        else:
            self.pixmap = self.apply_tint(pixmap, color, opacity)

        #   Set tooltip if there's text
        if text is not None:
            self.setToolTip(text)
        # self.pressed.connect(self.update)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(event.rect(), self.pixmap)
        if self.isDown():
            print("pico")

    def enterEvent(self, event):
        # Hover enter
        print("In")

    def leaveEvent(self, event):
        # Hover exit
        print("Out")

    def sizeHint(self):
        return QSize(self.width, self.height)

    def update_button_tint(self, button, tint_color, opacity):
        print('image_button aqui')
        # Get the current icon from the button
        current_icon = button.icon()

        # If the button is currently tinted, remove the tint
        if current_icon.isNull():
            return
        print('image_button aca')
        # Apply the tint to the current icon
        pixmap = current_icon.pixmap(current_icon.availableSizes()[0])
        tinted_pixmap = self.apply_tint(pixmap, tint_color, opacity)

        # Set the tinted pixmap as the button's icon
        button.setIcon(tinted_pixmap)

    @staticmethod
    def apply_tint(pixmap, tint_color, opacity):
        # Adjust opacity (0.0 to 1.0)
        # Convert the QPixmap to a QImage
        image = pixmap.toImage()

        # Get the size of the image
        width, height = image.width(), image.height()

        # Iterate over each pixel and apply the tint color with opacity
        for x in range(width):
            for y in range(height):
                # Get the original pixel color
                pixel_color = image.pixelColor(x, y)

                # Blend the pixel color with the tint color and adjust opacity
                r = int(pixel_color.red() * (1 - opacity) + tint_color.red() * opacity)
                g = int(pixel_color.green() * (1 - opacity) + tint_color.green() * opacity)
                b = int(pixel_color.blue() * (1 - opacity) + tint_color.blue() * opacity)

                # Set the modified pixel color in the image
                image.setPixelColor(x, y, QColor(r, g, b))

        # Convert the modified QImage back to a QPixmap
        tinted_pixmap = QPixmap.fromImage(image)

        return tinted_pixmap
