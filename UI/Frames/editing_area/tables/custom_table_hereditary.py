from PyQt6.QtWidgets import QTableWidget, QTableView, QComboBox, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, \
    QHeaderView
from PyQt6.QtCore import pyqtSlot
from UI.Widgets.custom_text_edit import CustomTextEdit
from UI.Frames.editing_area.tables.custom_hereditary_delegate import CustomHereditaryDelegate
from mongodb.read.get_relationships import GetRelationships


class WidgetTableButtons(QWidget):
    def __init__(self, parent=None,  dictionary=None, add=False, remove=False, save=False):
        super().__init__(parent)
        # Table above Add/Remove buttons
        my_layout = QVBoxLayout()
        my_layout.setContentsMargins(0, 0, 0, 0)
        self.my_table = CustomTableHereditary(self, dictionary)
        my_layout.addWidget(self.my_table)
        # Check if buttons are needed
        if add or remove or save:
            # Add/Remove buttons beside each other
            buttons_layout = QHBoxLayout()
            if add:
                add_button = QPushButton('Add')
                # Call add function
                add_button.clicked.connect(lambda: self.add_row())
                buttons_layout.addWidget(add_button)
            if remove:
                remove_button = QPushButton('Remove')
                # Call remove function
                remove_button.clicked.connect(lambda: self.remove_row())
                buttons_layout.addWidget(remove_button)
            if save:
                save_button = QPushButton('Remove')
                # Call save function
                save_button.clicked.connect(lambda: self.save_row())
                buttons_layout.addWidget(save_button)
            # Widget containing Buttons
            buttons_widget = QWidget()
            buttons_widget.setLayout(buttons_layout)
        else:
            buttons_widget = None
        # Add buttons if required
        if buttons_widget is not None:
            my_layout.addWidget(buttons_widget)
        # Set the widget
        self.setLayout(my_layout)

    def retrieve_data(self):
        # Call retrieve_data table function
        return self.my_table.retrieve_data()

    @pyqtSlot()
    def add_row(self):
        # Call add_row table function
        self.my_table.add_row()
        return

    @pyqtSlot()
    def remove_row(self):
        # Call remove_row table function
        self.my_table.remove_row()
        return

    @pyqtSlot()
    def save_row(self):
        # Call save table function
        self.my_table.retrieve_data()
        return


class CustomTableHereditary(QTableWidget):
    def __init__(self, parent=None, dictionary=None):
        super().__init__(parent)
        if dictionary is None:
            super().__init__(1, 2)
        else:
            super().__init__(len(dictionary), 2)
        self.dictionary = dictionary
        # Retrieve relationships from DB
        self.relationships = GetRelationships().relationships_dict
        self.tune_ui()

    def set_ui(self):
        self.horizontalHeader().hide()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()

    def re_tune_widget(self, dictionary=None):
        # To update widget
        self.setRowCount(len(dictionary))
        self.dictionary = dictionary
        self.tune_ui()

    def tune_ui(self):
        self.setMinimumHeight(300)
        self.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
        self.verticalHeader().setDefaultSectionSize(15)
        #   Remove column number
        self.horizontalHeader().hide()
        #   Second column is expandable
        self.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        #   Set delegate
        self.setItemDelegate(CustomHereditaryDelegate(self, self.dictionary, self.relationships))
        for r in range(self.rowCount()):
            # use the default QTableView implementation, otherwise we would
            # need to create items for each cell; since QTableWidget
            # already does it on its own, let's make things simpler.
            QTableView.openPersistentEditor(self, self.model().index(r, 0))
            QTableView.openPersistentEditor(self, self.model().index(r, 1))
        self.set_ui()

    def add_row(self):
        current_row_count = self.rowCount()
        self.insertRow(current_row_count)
        self.tune_ui()
        return

    # Be mindful of the difference between remove_row() and removeRow()
    def remove_row(self, index=-1):
        last_row = self.rowCount()
        # Prevent total removal of rows
        if last_row > 1:
            # Remove last row if not specified (pop)
            if index < 0:
                self.removeRow(last_row-1)
            else:
                # Remove specified row
                self.removeRow(index)
        else:
            self.removeRow(last_row-1)
            self.add_row()
        return

    def get_empty(self):
        empty_rows = []
        # Emptiness flag
        empty_field = {'combobox': False, 'custom_text_edit': False}
        for row in range(self.rowCount()):
            # Get containing data
            custom_text_edit = self.cellWidget(row, 1)
            combobox = self.cellWidget(row, 0)
            # Finds empty text
            if custom_text_edit.retrieve_data() is None:
                empty_field['combobox'] = True
            # Finds empty option
            if combobox.currentText() == '' and row not in empty_rows:
                empty_field['custom_text_edit'] = True

            # Which field is empty
            if empty_field['custom_text_edit'] and empty_field['combobox']:
                # Both Empty
                empty_rows.append(row)
            """
            # Implement further functionality when needed
            elif  empty_field['custom_text_edit'] and not empty_field['combobox']:
                # Custom_text_edit empty
            elif not empty_field['custom_text_edit'] and  empty_field['combobox']:
                # combobox empty
            """
        return empty_rows

    def remove_empty(self):
        for empty_row_index in self.get_empty():
            self.remove_row(empty_row_index)
        return

    def retrieve_data(self):
        resulting_dict = {}
        for row in range(self.rowCount()):
            combobox = self.cellWidget(row, 0)
            custom_text_edit = self.cellWidget(row, 1)
            if isinstance(combobox, QComboBox) and isinstance(custom_text_edit, CustomTextEdit):
                resulting_dict[combobox.currentText()] = custom_text_edit.retrieve_data()
        return resulting_dict
