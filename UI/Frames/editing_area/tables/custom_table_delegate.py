from PyQt6.QtWidgets import QStyledItemDelegate
from PyQt6.QtCore import Qt
from UI.Frames.editing_area.tables.custom_line_edit import CustomLineEdit


class CustomTableDelegate(QStyledItemDelegate):
    def __init__(self, parent=None, dictionary=None):
        super(CustomTableDelegate, self).__init__(parent)
        if dictionary is None:
            self.dictionary = {}
        self.dictionary = dictionary
        self.list_keys = ['']
        self.setup_complete = False
        self.counter = 0
        for key in dictionary:
            self.list_keys.append(key)

    def createEditor(self, parent, opt, index):
        self.counter += 1
        if self.counter == len(self.dictionary):
            self.setup_complete = True
        return CustomLineEdit(parent, self.list_keys[self.counter], self.dictionary[self.list_keys[self.counter]])

    def setEditorData(self, editor, index):
        if self.dictionary[self.list_keys[self.counter]] is not None and self.counter < len(self.dictionary):
            editor.setText(self.dictionary[self.list_keys[self.counter]])
        # Only used for last item
        elif self.setup_complete:
            editor.setText(self.dictionary[self.list_keys[self.counter]])
            self.setup_complete = False
        else:
            super(CustomTableDelegate, self).setEditorData(editor, index)

    def setModelData(self, editor, model, index):
        model.setData(index, editor.text(), Qt.ItemDataRole.EditRole)

    def eventFilter(self, editor, event):
        if event.type() == event.Type.KeyPress:
            """
            # Up arrow 16777235
            # Down arrow 16777237
            # Left arrow 16777234
            # Right arrow 16777236
            # Backspace 16777219
            # Enter 16777220
            """
            # Either up or down arrows will get the data into our model
            if event.key() == 16777235:
                # Up arrow
                self.commitData.emit(editor)
                self.closeEditor.emit(editor, self.EndEditHint.EditPreviousItem)
            elif event.key() == 16777237:
                # Down arrow
                print('enter')
                self.commitData.emit(editor)
                self.closeEditor.emit(editor, self.EndEditHint.EditNextItem)
                return True
        return super().eventFilter(editor, event)
