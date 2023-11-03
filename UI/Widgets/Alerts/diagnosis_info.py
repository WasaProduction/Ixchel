from PyQt6.QtWidgets import QDialog, QDialogButtonBox, QTextEdit, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt
from UI.Widgets.documents.diagnosis_info_doc import DiagnosisInfoDoc


class DiagnosisInfo(QDialog):
    def __init__(self, parent=None, title='Info'):
        super().__init__(parent)
        #   Variables
        self.title = title
        #   Button
        self.ok = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        self.ok.accepted.connect(self.accept)
        #   Document to be inserted inside text edit.
        text_document = DiagnosisInfoDoc()

        """     Text edit       """
        self.text_edit = QTextEdit()
        #   Disable edition.
        self.text_edit.setReadOnly(True)
        #   Remove background
        self.text_edit.viewport().setAutoFillBackground(False)
        #   Remove border
        self.text_edit.setStyleSheet("border: none;")
        #   Set the document with styles to the QTextEdit.
        self.text_edit.setDocument(text_document)
        #   Exit button.
        button = QPushButton("Ciao")
        button.clicked.connect(self.accept)
        #   Layout to be used.
        self.other_layout = QVBoxLayout()
        self.other_layout.addWidget(self.text_edit)
        self.other_layout.addWidget(button)

        self.init_ui()
        #   Show message
        self.exec()

    """     UI      """
    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setMinimumHeight(600)
        self.setMinimumWidth(750)
        self.setLayout(self.other_layout)
        self.text_edit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.text_edit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
