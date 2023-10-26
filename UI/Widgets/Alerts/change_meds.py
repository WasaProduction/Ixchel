from PyQt6.QtWidgets import QDialog, QGridLayout, QWidget, QLabel, QHBoxLayout, QPushButton
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class ChangeMeds(QDialog):
    def __init__(self, parent=None, text_labels=None, instructions=None):
        super().__init__(parent)
        self.text_labels = text_labels
        self.title = self.text_labels.update_medication
        #   Layout
        self.layout = QGridLayout()
        self.instructions_arr = [] if instructions is None else instructions
        self.displayed_instructions = []
        #   Set spacing
        self.layout.setVerticalSpacing(2)
        #   Place instructions.
        self.update_instructions()
        #   UI
        self.init_ui()

    def update_instructions(self, instructions=None):
        #   Update instructions to be placed.
        self.instructions_arr = [] if instructions is None else instructions
        #   Remove current displayed instructions if any.
        self.remove_instructions()
        #   Place new instructions.
        self.place_instructions()

    def place_instructions(self):
        for i, instruction in enumerate(self.instructions_arr):
            my_instruction = InstructionObj(self, self.text_labels, instruction)
            self.layout.addWidget(my_instruction, i + 1, 0, Qt.AlignmentFlag.AlignRight)
            #   Keep track of displayed instructions.
            self.displayed_instructions.append(my_instruction)

    def remove_instructions(self):
        for instruction in self.displayed_instructions:
            instruction.deleteLater()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setLayout(self.layout)


class InstructionObj(QWidget):
    def __init__(self, parent=None, text_labels=None, instruction=None):
        super().__init__(parent)
        self.text_labels = text_labels
        self.layout = QHBoxLayout()
        self.instruction = instruction
        self.instruction_lbl = QLabel(self.instruction['raw_text'])

        self.instruction_details = QWidget()
        grid_lyt = QGridLayout(self.instruction_details)
        grid_lyt.setContentsMargins(0, 0, 0, 0)
        grid_lyt.addWidget(self.instruction_lbl, 0, 0, 1, 2)
        #   Display start
        if self.instruction['start_date'] is not None:
            #   Cast date
            start = QLabel(self.instruction['start_date'].strftime("%m/%d/%Y"))
            #   Place date
            grid_lyt.addWidget(start, 1, 0, 1, 1, Qt.AlignmentFlag.AlignCenter)

        #   Display end
        if self.instruction['to_deactivate'] is not None:
            #   Cast date
            end = QLabel(self.instruction['to_deactivate'].strftime("%m/%d/%Y"))
            #   Place date
            grid_lyt.addWidget(end, 1, 1, 1, 1, Qt.AlignmentFlag.AlignCenter)

        self.trash_btn = QPushButton()
        self.trash_btn.setText(self.text_labels.remove)
        self.trash_btn.setToolTip(self.text_labels.remove)
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
        self.layout.addWidget(self.instruction_details)
        self.layout.addWidget(self.trash_btn)
        self.setLayout(self.layout)
