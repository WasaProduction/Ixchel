from PyQt6.QtWidgets import QStyledItemDelegate, QComboBox
from PyQt6.QtCore import Qt
from UI.Widgets.custom_text_edit import CustomTextEdit
from UI.Frames.editing_area.tables.custom_combobox import CustomComboBox


class CustomHereditaryDelegate(QStyledItemDelegate):
    def __init__(self, parent=None, familiar_conditions_dict=None, relationships=None):
        super(CustomHereditaryDelegate, self).__init__(parent)
        # Used to populate the CustomTextEdit
        self.my_placeholder = 'Placeholder'
        self.my_keys = []
        self.my_dictionary = familiar_conditions_dict
        self.update_data(familiar_conditions_dict)
        # Used to populate the ComboBox
        self.relationships = relationships
        # Used to traverse rows & columns
        self.column_counter = 0
        self.row_counter = 0
        # self.setup_not_complete = True

    def update_data(self, familiar_conditions_dict=None):
        if familiar_conditions_dict is None:
            self.my_dictionary = {}
        else:
            self.my_dictionary = familiar_conditions_dict
            self.extrac_keys()

    def extrac_keys(self):
        self.my_keys = [key for key in self.my_dictionary]

    def createEditor(self, parent, opt, index):
        # Column 0 will contain a table that lists all known affections of the familiar
        if index.column() == 0:
            # ComboBox with the relationships and current selection
            if len(self.my_dictionary) > 0:
                # Add default combobox after dictionary entries are covered
                if index.row() > len(self.my_dictionary) - 1:
                    return CustomComboBox(parent, self.relationships)
                return CustomComboBox(parent, self.relationships, self.my_keys[self.row_counter])
            else:
                # Default combobox
                return CustomComboBox(parent, self.relationships)
        # Column 1 will contain a combobox containing the relationship with the patient
        elif index.column() == 1:
            # Table with the affection list
            if len(self.my_dictionary) > 0:
                # Add default CustomTextEdit after dictionary entries are covered
                if index.row() > len(self.my_dictionary) - 1:
                    return CustomTextEdit(parent, '/Users/jaimegonzalezquirarte/Desktop/App/vocabulario.txt',
                                          placeholder_str=self.my_placeholder)
                return CustomTextEdit(parent, '/Users/jaimegonzalezquirarte/Desktop/App/vocabulario.txt',
                                      contained_str=self.my_dictionary[self.my_keys[self.row_counter]])
            else:
                # Default CustomTextEdit
                return CustomTextEdit(parent, '/Users/jaimegonzalezquirarte/Desktop/App/vocabulario.txt',
                                      placeholder_str=self.my_placeholder)

    def setEditorData(self, editor, index):
        if self.column_counter == 1:
            self.column_counter = -1
            self.row_counter += 1
        self.column_counter += 1

    def setModelData(self, editor, model, index):
        if isinstance(editor, QComboBox):
            model.setData(index, editor.currentText(), Qt.ItemDataRole.EditRole)
        else:
            print(type(editor))
            model.setData(index, editor.retrieve_data(), Qt.ItemDataRole.EditRole)

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
