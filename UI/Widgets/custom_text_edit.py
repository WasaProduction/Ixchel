# For Text Edit
from PyQt6.QtWidgets import QPlainTextEdit
# For completer
from UI.Widgets.my_completor import MyCompleter
from PyQt6.QtWidgets import QCompleter
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QTextCursor
# For highlighter
from spell_check import SpellCheck
from UI.Widgets.affection_highlighter import AffectionHighlighter
from PyQt6.QtCore import pyqtSlot
# For saving file
from mongodb.write.create_diagnosis import CreateDiagnosis
#TODO https://stackoverflow.com/questions/35858340/clickable-hyperlink-in-qtextedit


class CustomTextEdit(QPlainTextEdit):
    def __init__(self, parent=None, chk_dict_path='', placeholder_str=None, contained_str=None):
        super(CustomTextEdit, self).__init__(parent)
        # Completer
        self.completer = MyCompleter(self)
        self.completer.setWidget(self)
        self.completer.insertText.connect(self.insert_completion)
        self.completer_dictionary = []
        self.checker = SpellCheck(chk_dict_path)
        # Highlighter
        self.highlighter = AffectionHighlighter()
        self.set_up_editor()
        if placeholder_str is not None:
            self.setPlaceholderText('Placeholder')
        else:
            self.setPlaceholderText('Placeholder is None')
        if contained_str is not None:
            self.insertPlainText(contained_str)
        self.tune_ui()

    """     Completer block     """
    def update_completer_model(self, new_dictionary):
        self.completer_dictionary = new_dictionary
        self.completer.update_dictionary(self.completer_dictionary)

    def insert_completion(self, completion):
        tc = self.textCursor()
        # Get the remaining characters missing of the word to complete
        extra = (len(completion) - len(self.completer.completionPrefix()))
        tc.movePosition(QTextCursor.MoveOperation.Left)
        tc.movePosition(QTextCursor.MoveOperation.EndOfWord)
        # Insert those characters at the end of the word
        tc.insertText(completion[-extra:])
        self.setTextCursor(tc)
        self.completer.popup().hide()

    def focusInEvent(self, event):
        if self.completer:
            self.completer.setWidget(self)
        QPlainTextEdit.focusInEvent(self, event)

    @pyqtSlot()
    def process_text(self):
        # Get the text inside widget and split at the spaces and dot
        words = self.toPlainText().split(" ")
        # Get last element of the array
        written_string = words[len(words) - 1]
        suggestions_array = self.checker.check_for_underscores(written_string)

        if suggestions_array:
            self.update_completer_model(suggestions_array)

    def keyPressEvent(self, event):
        tc = self.textCursor()
        if event.key() == Qt.Key.Key_Tab and self.completer.popup().isVisible():
            self.completer.insertText.emit(self.completer.get_selected())
            self.completer.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)
            return

        QPlainTextEdit.keyPressEvent(self, event)
        tc.select(QTextCursor.SelectionType.WordUnderCursor)
        cr = self.cursorRect()

        if len(tc.selectedText()) > 0:
            self.process_text()
            self.completer.setCompletionPrefix(tc.selectedText())
            popup = self.completer.popup()
            popup.setCurrentIndex(self.completer.completionModel().index(0, 0))

            cr.setWidth(self.completer.popup().sizeHintForColumn(0)
                        + self.completer.popup().verticalScrollBar().sizeHint().width())
            self.completer.complete(cr)
        else:
            self.completer.popup().hide()

    """     Highlighter Block       """
    def set_up_editor(self):
        self.highlighter.setDocument(self.document())

    """     Retrieve Data"""
    def retrieve_data(self):
        text = self.toPlainText()
        if len(text.strip()):
            return text
        else:
            return None

    """     Save into file      """
    def save_into_file(self):
        # Validate text
        text = self.toPlainText()
        if len(text.strip()):
            CreateDiagnosis(self.toPlainText())

    def tune_ui(self):
        # self.setMinimumWidth()
        # self.setMaximumWidth()
        self.setMinimumHeight(200)
        # self.setMaximumHeight()
