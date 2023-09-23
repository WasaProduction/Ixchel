from PyQt6.QtWidgets import QVBoxLayout
from UI.Widgets.image_button import ImageButton
from UI.Widgets.custom_qimage import CustomQImage


class StatusWidget(QVBoxLayout):
    def __init__(self):
        super().__init__()
        for x in range(0, 10):
            icon = ImageButton(CustomQImage(1))
            self.addWidget(icon)
        # Intended to stack all the widgets at the top
        self.addStretch()
