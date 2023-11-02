from PyQt6.QtWidgets import QDialog, QDialogButtonBox, QTextEdit, QVBoxLayout
from PyQt6.QtCore import Qt
from UI.Widgets.documents.prescription_info_doc import PrescriptionInfoDoc


class PrescriptionInfo(QDialog):
    def __init__(self, parent=None, title=None):
        super().__init__(parent)
        #   Variables
        self.title = title
        #   Button
        self.ok = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        self.ok.accepted.connect(self.accept)
        #   Document to be inserted inside text edit.
        text_document = PrescriptionInfoDoc()

        """     Text edit       """
        self.text_edit = QTextEdit()
        #   Disable edition.
        self.text_edit.setReadOnly(True)
        #   Remove background
        self.text_edit.viewport().setAutoFillBackground(False)
        #   Remove border
        self.text_edit.setStyleSheet("border: none;")
        #   Set the documen with styles to the QTextEdit.
        self.text_edit.setDocument(text_document)
        #   Layout to be used.
        self.other_layout = QVBoxLayout()
        self.other_layout.addWidget(self.text_edit)

        self.init_ui()
        #   Show message
        self.exec()

    """     UI      """
    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setMinimumHeight(560)
        self.setMinimumWidth(700)
        self.setLayout(self.other_layout)
        self.text_edit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.text_edit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
