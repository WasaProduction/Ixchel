import re
from PyQt6.QtGui import QColor, QSyntaxHighlighter, QTextCharFormat


class DrugHighlighter (QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)

    def set_format(self, text_block):
        #   Font object
        pattern_format = QTextCharFormat()
        pattern_format.setFontItalic(True)
        pattern_format.setForeground(QColor('#FFBA26'))
        #   Paint
        for match in re.finditer(r"\S*(?=\s*\-)", text_block, re.IGNORECASE):
            start, end = match.span()
            self.setFormat(start, end - start, pattern_format)

    def highlightBlock(self, text_block):
        if '-' in text_block:
            self.set_format(text_block)
