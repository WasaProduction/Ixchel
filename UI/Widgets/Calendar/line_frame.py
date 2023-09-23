from PyQt6.QtWidgets import QFrame


class LineFrame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        #   Set line
        self.setFrameShape(QFrame.Shape.HLine)
