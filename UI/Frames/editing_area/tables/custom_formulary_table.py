from PyQt6.QtWidgets import QTableWidget, QStyle, QTableView, QHeaderView
from UI.Frames.editing_area.tables.custom_test_delegate import CustomTableDelegate


class CustomFormularyTable(QTableWidget):
    def __init__(self, parent=None, dictionary=None):
        super(CustomFormularyTable, self).__init__(parent)
        self.setColumnCount(1)
        self.setRowCount(len(dictionary))
        # super().__init__(len(dictionary), 1)
        if dictionary is None:
            self.dictionary = None
        else:
            self.dictionary = dictionary
        self.setItemDelegate(CustomTableDelegate(self, dictionary))
        self.tune()
        """     Table size      """
        fm = self.fontMetrics()
        min_width = 500
        # for l in range(10):
        #    min_width = max(min_width, fm.boundingRect(l).width())
        margin = self.style().pixelMetric(QStyle.PixelMetric.PM_HeaderMargin, None, self) * 2
        self.horizontalHeader().setDefaultSectionSize(min_width + margin)
        # self.verticalHeader().setDefaultSectionSize(fm.height() + margin)

        for r in range(len(dictionary)):
            # use the default QTableView implementation, otherwise we would
            # need to create items for each cell; since QTableWidget
            # already does it on its own, let's make things simpler.
            QTableView.openPersistentEditor(self, self.model().index(r, 0))

    def retrieve_data(self):
        empty_counter = 0
        for index, key in enumerate(self.dictionary.keys()):
            widget = self.cellWidget(index, 0)
            if widget.text().strip():
                #   Get QLineEdit text into our data model
                self.dictionary[widget.placeholderText()] = widget.text().strip()
            else:
                #   Keep track of empty fields
                empty_counter += 1
                self.dictionary[key] = None
        #   Return None if empty
        if empty_counter == len(self.dictionary):
            return None
        else:
            return self.dictionary

    def tune(self):
        self.tune_ui()

    def tune_ui(self):
        # Remove table UI elements to make it feel more like a document
        self.setShowGrid(False)
        self.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.horizontalHeader().hide()
        self.verticalHeader().hide()
        self.setMinimumHeight(self.sizeHintForRow(0) * 8)
