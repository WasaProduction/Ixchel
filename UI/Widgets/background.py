from PyQt6.QtWidgets import QWidget, QVBoxLayout,  QHBoxLayout, QLabel, QScrollArea, QTreeWidgetItem, QTreeWidget,\
    QSizePolicy, QFrame, QGridLayout
from PyQt6.QtCore import Qt
from UI.Widgets.icons.allergy_icon import AllergyIcon
from UI.Widgets.collapsible_box import CollapsibleBox


class GeneralInformation(QWidget):
    def __init__(self, parent=None, text_labels=None, general_information=None):
        super().__init__(parent)
        self.text_labels = text_labels
        self.tittle = self.text_labels.general_info_lbl
        self.dict = {'Age': 28, 'Weight': 70, 'Height': 1.76, 'Sex': 'M'}
        #   Layout
        self.general_layout = QVBoxLayout()
        #   Tree widget
        self.tree = QTreeWidget(self)
        #   Set tree header
        self.tree.setHeaderLabels([self.tittle])
        #   Hide header
        self.tree.setHeaderHidden(True)
        #   Populate tree
        self.populate_tree()
        #   Adjust tree height
        self.adjust_tree_widget_height()
        #   Collapsible height
        self.collapsible_widget = CollapsibleBox(self, self.tittle, self.tree)
        self.init_ui()

    def populate_tree(self):
        #   Traverse self.dict keys and values.
        for key in self.dict:
            item = QTreeWidgetItem(self.tree)
            #   Insert item "Key: Value" format
            item.setText(0, key + ': ' + str(self.dict[key]))

    def adjust_tree_widget_height(self):
        #   Calculate height
        total_height = self.tree.sizeHintForRow(0) * (len(self.dict)) #+ self.tree.sizeHintForRow(0)
        #   Set height
        self.tree.setMinimumHeight(total_height)
        self.tree.setMaximumHeight(total_height + 1)

    def update_widget(self, general_information=None):
        if general_information is None:
            self.dict = {}
        else:
            self.dict = general_information
        #   Clear tree
        self.tree.clear()
        #   Repopulate tree
        self.populate_tree()

    def init_ui(self):
        #   Add expandable widget to layout
        self.general_layout.addWidget(self.collapsible_widget)
        #   Set layout
        self.setLayout(self.general_layout)


class HereditaryBackground(QWidget):
    def __init__(self, parent=None, text_labels=None, hereditary_information=None):
        super().__init__(parent)
        self.text_labels = text_labels
        hereditary_layout = QVBoxLayout()
        self.widget = QWidget()
        self.collapsible_widget = CollapsibleBox(self, self.text_labels.hereditary_lbl, self.widget)
        hereditary_layout.addWidget(self.collapsible_widget)
        self.setLayout(hereditary_layout)


class PathologicBackground(QWidget):
    def __init__(self, parent=None, text_labels=None, pathologic_information=None):
        super().__init__(parent)
        self.text_labels = text_labels
        pathologic_layout = QVBoxLayout()
        self.widget = QWidget()
        #self.collapsible_widget = CollapsibleBox(self, self.text_labels.pathologic_lbl, self.widget)
        #pathologic_layout.addWidget(self.collapsible_widget)
        self.setLayout(pathologic_layout)


class Immunizations(QWidget):
    def __init__(self, parent=None, text_labels=None, immunizations_information=None):
        super().__init__(parent)
        self.text_labels = text_labels
        immunizations_layout = QVBoxLayout()
        self.widget = QWidget()
        self.collapsible_widget = CollapsibleBox(self, self.text_labels.immunizations_lbl, self.widget)
        immunizations_layout.addWidget(self.collapsible_widget)
        self.setLayout(immunizations_layout)


class Allergy (QWidget):
    def __init__(self, parent=None, text_labels=None, allergies_information=None):
        super().__init__(parent)
        self.text_labels = text_labels
        allergies_layout = QVBoxLayout()
        self.widget = QWidget()
        self.collapsible_widget = CollapsibleBox(self, self.text_labels.allergies_lbl, self.widget)
        allergies_layout.addWidget(self.widget)
        # Grid containing allergies
        grid_layout = QGridLayout()
        # Columns of the Grid (Rows will be added as needed)
        grid_columns = 6
        # Variables to navigate Grid
        column_counter = 0
        row_counter = 0
        for allergy in allergies_information:
            # Icon/label into widget
            allergy_layout = QHBoxLayout()
            allergy_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
            allergy_icon = AllergyIcon(allergy)
            allergy_label = QLabel(allergy.allergen)
            allergy_layout.addWidget(allergy_icon)
            allergy_layout.addWidget(allergy_label)
            allergy_layout.addStretch()
            allergy_widget = QWidget()
            allergy_widget.setLayout(allergy_layout)
            # Add Icon/label widget into the Grid
            grid_layout.addWidget(allergy_widget, row_counter, column_counter)
            if column_counter == grid_columns - 1:
                row_counter += 1
                column_counter = 0
            else:
                column_counter += 1
        # Grid into Widget
        content_scroll_widget = QWidget()
        content_scroll_widget.setLayout(grid_layout)
        # Widget into scroll
        allergies_scroll = QScrollArea()
        allergies_scroll.setWidget(content_scroll_widget)
        allergies_scroll.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        allergies_scroll.setFrameShape(QFrame.Shape.NoFrame)
        allergies_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        # Scroll into our layout
        allergies_layout.addWidget(allergies_scroll)
        allergies_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.setFixedHeight(150)
        # Layout into widget
        self.setLayout(allergies_layout)
