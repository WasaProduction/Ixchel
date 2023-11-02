from PyQt6.QtWidgets import QMessageBox, QDialogButtonBox
from UI.Widgets.custom_qimage import CustomQImage


class DiagnosisInfo(QMessageBox):
    def __init__(self, parent=None, title=None):
        super().__init__(parent)
        #   Variables
        self.title = title
        #   Button
        self.ok = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        self.ok.accepted.connect(self.accept)
        self.init_ui()
        #   Show message
        self.exec()

    """     UI      """
    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setIconPixmap(CustomQImage(0))
