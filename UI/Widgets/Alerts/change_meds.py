from PyQt6.QtWidgets import QDialog, QGridLayout, QWidget, QLabel, QHBoxLayout, QPushButton
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class ChangeMeds(QDialog):
    def __init__(self, parent=None, meds=None):
        super().__init__(parent)
        self.layout = QGridLayout()
        self.title = "Kawai º-º"
        self.message = "Update "
        self.message_label = QLabel(self.message)
        self.instructions_arr = []
        self.meds = meds
        #   Set grid
        self.set_grid()
        #   UI
        self.init_ui()

    def set_grid(self):
        self.layout.setVerticalSpacing(2)
        self.layout.addWidget(self.message_label, 0, 0, Qt.AlignmentFlag.AlignCenter)
        for index in range(1, 5):
            my_instruction = InstructionObj(self, index)
            self.layout.addWidget(my_instruction, index, 0, Qt.AlignmentFlag.AlignRight)
            self.instructions_arr.append(my_instruction)

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setLayout(self.layout)


class InstructionObj(QWidget):
    def __init__(self, parent=None, meds=None):
        super().__init__(parent)
        self.layout = QHBoxLayout()
        self.instruction = 'Advil'
        self.instruction_lbl = QLabel(self.instruction)
        self.trash_btn = QPushButton()
        self.trash_btn.setToolTip('Delete')
        self.trash_btn.clicked.connect(lambda: self.abort_instruction())
        #   UI
        self.init_ui()

    def abort_instruction(self):
        #   Cancel instruction in db.
        #   Customize font for visual feedback.
        aborted_text = QFont()
        aborted_text.setItalic(True)
        aborted_text.setStrikeOut(True)
        #   Red tint (wine like).
        self.instruction_lbl.setStyleSheet('color : #C60D25;')
        self.instruction_lbl.setFont(aborted_text)

    def init_ui(self):
        #   Instruction
        self.layout.addWidget(self.instruction_lbl)
        self.layout.addWidget(self.trash_btn)
        self.setLayout(self.layout)
