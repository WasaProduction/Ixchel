from PyQt6.QtWidgets import QMessageBox, QDialogButtonBox
from UI.Widgets.custom_qimage import CustomQImage


class Error(QMessageBox):
    def __init__(self, parent=None, title='title', message='message'):
        super().__init__(parent)
        #   Variables
        self.title = title
        self.message = message
        #   Button
        self.ok = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        self.ok.accepted.connect(self.accept)
        self.init_ui()
        #   Show message
        self.exec()

    """     UI      """
    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setText(self.message)
        self.setIconPixmap(CustomQImage(0))
