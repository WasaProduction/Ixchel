from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea, QTreeWidgetItem, QTreeWidget,\
    QGridLayout
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
        self.hereditary_layout = QVBoxLayout()
        self.widget = QWidget()
        self.collapsible_widget = CollapsibleBox(self, self.text_labels.hereditary_lbl, self.widget)
        #   UI
        self.init_ui()

    def init_ui(self):
        #   Add expandable widget to layout
        self.hereditary_layout.addWidget(self.collapsible_widget)
        #   Set layout
        self.setLayout(self.hereditary_layout)


class PathologicBackground(QWidget):
    def __init__(self, parent=None, text_labels=None, pathologic_information=None):
        super().__init__(parent)
        self.text_labels = text_labels
        self.pathologic_layout = QVBoxLayout()
        self.widget = QWidget()
        self.collapsible_widget = CollapsibleBox(self, self.text_labels.pathologic_lbl, self.widget)
        #   UI
        self.init_ui()

    def init_ui(self):
        #   Add expandable widget to layout
        self.pathologic_layout.addWidget(self.collapsible_widget)
        #   Set layout
        self.setLayout(self.pathologic_layout)


class Immunizations(QWidget):
    def __init__(self, parent=None, text_labels=None, immunizations_information=None):
        super().__init__(parent)
        self.text_labels = text_labels
        self.immunizations_layout = QVBoxLayout()
        self.widget = QWidget()
        self.collapsible_widget = CollapsibleBox(self, self.text_labels.immunizations_lbl, self.widget)
        #   UI
        self.init_ui()

    def init_ui(self):
        #   Add expandable widget to layout
        self.immunizations_layout.addWidget(self.collapsible_widget)
        #   Set layout
        self.setLayout(self.immunizations_layout)

from data_models.model_allergy import ModelAllergy
import random

class Allergy (QWidget):
    def __init__(self, parent=None, text_labels=None, allergies_information=None):
        super().__init__(parent)
        #   Layout
        self.allergies_layout = QVBoxLayout()
        self.text_labels = text_labels
        #   Contain individual tags.
        self.allergy_widgets = []
        #   Widget containing all tags.
        self.widget = self.allergies_into_widget(allergies_information)
        self.scroll_widget = QScrollArea()
        self.scroll_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_widget.setStyleSheet("border: none;")
        self.scroll_widget.setWidget(self.widget)
        self.collapsible_widget = CollapsibleBox(self, self.text_labels.allergies_lbl)
        #   UI
        self.init_ui()

    def update_allergies(self, allergies=None):
        allergies = []
        #   Remove self.widget contents
        self.remove_allergies()
        #   Remove self.widget
        for i in range(10):
            allergies.append(ModelAllergy('Alergia', random.randrange(1, 5), random.randrange(1, 5)))
        #   Create new self.widget with new contents
        self.widget = self.allergies_into_widget(allergies)
        self.scroll_widget.setWidget(self.widget)
        #   Update content inside collapsible widget
        self.collapsible_widget.update_content(self.scroll_widget)

    def remove_allergies(self):
        for widget in self.allergy_widgets:
            del widget

    def allergies_into_widget(self, allergies=None):
        #   Widget to be returned.
        widget = QWidget()
        #   Grid layout.
        grid_layout = QGridLayout()
        #   Columns of the Grid (Rows will be added as needed).
        grid_columns = 4
        # Variables to navigate Grid.
        column_counter = 0
        row_counter = 0
        #   Traverse grid.
        for allergy in allergies:
            #   Layout to contain Icon + Label.
            allergy_layout = QHBoxLayout()
            allergy_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
            #   Icon.
            allergy_icon = AllergyIcon(allergy)
            #   Label.
            allergy_label = QLabel(allergy.allergen)
            allergy_layout.addWidget(allergy_icon)
            allergy_layout.addWidget(allergy_label)
            allergy_layout.addStretch()
            #   Container widget.
            allergy_widget = QWidget()
            allergy_widget.setLayout(allergy_layout)
            #   Place widget into Grid Layout.
            grid_layout.addWidget(allergy_widget, row_counter, column_counter, Qt.AlignmentFlag.AlignLeft)
            #   Keep track of widgets added.
            self.allergy_widgets.append(allergy_widget)
            #   Implement column/row order.
            if column_counter < grid_columns:
                column_counter += 1
            else:
                column_counter = 0
                row_counter += 1
        #   Set grid into widget.
        widget.setLayout(grid_layout)
        return widget

    def init_ui(self):
        #   Add expandable widget to layout
        self.allergies_layout.addWidget(self.collapsible_widget)
        #   Set layout
        self.setLayout(self.allergies_layout)
