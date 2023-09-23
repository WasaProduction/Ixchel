from PyQt6.QtWidgets import QStyledItemDelegate
from PyQt6.QtCore import Qt
from UI.Frames.editing_area.tables.custom_line_edit import CustomLineEdit


class CustomTableDelegate(QStyledItemDelegate):
    def __init__(self, parent=None, list_or_dict=None):
        super(CustomTableDelegate, self).__init__(parent)
        self.counter = -1
        self.setup_complete = False
        if isinstance(list_or_dict, list):
            self.my_list = list_or_dict
            self.is_list = True
        else:
            self.is_list = False
            self.my_dict = list_or_dict
            self.key_list = list(self.my_dict.keys())

    def createEditor(self, parent, opt, index):
        if self.is_list:
            if self.counter < len(self.my_list):
                # Value as text
                return CustomLineEdit(parent, 'Add disease', self.my_list[self.counter])
            else:
                # Value as text
                return CustomLineEdit(parent, 'Add disease')
        else:
            # Key as placeholder Value as text
            return CustomLineEdit(parent, self.key_list[self.counter], self.my_dict[self.key_list[self.counter]])

    def setEditorData(self, editor, index):
        self.counter += 1
        if self.is_list:
            if self.counter == len(self.my_list):
                self.setup_complete = True
        else:
            if self.counter == len(self.my_dict):
                self.setup_complete = True

        if self.is_list and not self.setup_complete:
            editor.setText(self.my_list[self.counter])
        elif not self.is_list and not self.setup_complete:
            editor.setText(self.my_dict[self.key_list[self.counter]])
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
                self.commitData.emit(editor)
                self.closeEditor.emit(editor, self.EndEditHint.EditNextItem)
                return True
        return super().eventFilter(editor, event)
