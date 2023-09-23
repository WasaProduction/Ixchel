from PyQt6.QtWidgets import QCompleter
from PyQt6.QtCore import QStringListModel, pyqtSignal, Qt
import unicodedata


class DrugCompleter(QCompleter):
    insertText = pyqtSignal(str)

    def __init__(self, parent=None):
        self.contents = []
        QCompleter.__init__(self, self.contents, parent)
        # self.setFilterMode(Qt.MatchFlag.MatchContains)
        self.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)
        self.highlighted.connect(self.set_highlighted)
        # Initialize variable
        self.lastSelected = ""
        self.setMaxVisibleItems(7)
        self.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)

    def strip_accents(self, s):
        return ''.join(c for c in unicodedata.normalize('NFD', s)
                       if unicodedata.category(c) != 'Mn')

    def splitPath(self, path):
        return [self.strip_accents(path).lower()]

    def pathFromIndex(self, index):
        return index.data()

    def set_highlighted(self, text):
        self.lastSelected = text

    def get_selected(self):
        return self.lastSelected

    # Updating completer contents
    def update_dictionary(self, suggestion_dictionary):
        # Model needs to be a QStringListModel
        new_dictionary = QStringListModel()
        # Dictionary passed is transformed into QStringListModel
        new_dictionary.setStringList(suggestion_dictionary)
        # Setting the model
        self.setModel(new_dictionary)
