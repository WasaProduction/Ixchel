from PyQt6.QtWidgets import QTableView, QTableWidget
from UI.Frames.editing_area.tables.custom_test_delegate import CustomTableDelegate


class CustomTableExpandable(QTableWidget):
    def __init__(self, parent=None,  my_list=None):
        super().__init__(parent=parent)
        self.installEventFilter(self)
        self.setRowCount(len(my_list))
        self.setColumnCount(1)
        self.dictionary = my_list
        self.setItemDelegate(CustomTableDelegate(self, my_list))
        # Set UI
        self.tune()

    def set_ui(self):
        self.horizontalHeader().hide()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()

    def tune(self):
        for r in range(self.rowCount()):
            # use the default QTableView implementation, otherwise we would
            # need to create items for each cell; since QTableWidget
            # already does it on its own, let's make things simpler.
            QTableView.openPersistentEditor(self, self.model().index(r, 0))
        self.set_ui()

    def add_row(self):
        current_row_count = self.rowCount()
        print('insertado en ', current_row_count)
        self.insertRow(current_row_count)
        print('new count', self.rowCount())
        self.tune()

    def remove_row(self, index=-1):
        last_row = self.rowCount()
        # Prevent removal of empty columns
        if last_row > 1:
            if index < 0:
                self.removeRow(last_row-1)
            else:
                self.removeRow(index)

    def find_empty_rows(self):
        empty_rows = []
        for row in range(self.rowCount()):
            widget = self.cellWidget(row, 0)
            if widget.text().strip() == '':
                empty_rows.append(row)
        # Prevent complete deletion, leave at least 1 field to work with.
        if len(empty_rows) >= self.rowCount():
            empty_rows.pop(0)
        return empty_rows

    def remove_empty_rows(self):
        for row in self.find_empty_rows():
            # Close the editor
            self.cellWidget(row, 0).close()
            # Remove the row
            self.remove_row(row)

    def retrieve_data(self):
        resulting_list = []
        self.remove_empty_rows()
        for row in range(self.rowCount()):
            text_line = self.cellWidget(row, 0)
            resulting_list.append(text_line.text())
        return resulting_list

    def eventFilter(self, source, event):
        if event.type() == event.Type.KeyPress:
            if event.key() == 16777220:
                self.remove_empty_rows()
                current_row = self.currentRow()
                # QTBUG-102809
                if self.currentRow() < 0:
                    current_row = 0

                my_contents = self.cellWidget(current_row, 0).text()
                if current_row + 1 == self.rowCount() and my_contents.strip() != '':
                    self.add_row()
        return super().eventFilter(source, event)
