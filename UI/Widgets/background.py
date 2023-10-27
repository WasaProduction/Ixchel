from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea, QTreeWidgetItem, QTreeWidget,\
    QGridLayout, QSizePolicy
from PyQt6.QtCore import Qt
from UI.Frames.editing_area.tables.custom_table_hereditary import WidgetTableButtons
from UI.Widgets.icons.allergy_icon import AllergyIcon
from UI.Widgets.collapsible_box import CollapsibleBox


class GeneralInformation(QWidget):
    def __init__(self, parent=None, text_labels=None, general_information=None):
        super().__init__(parent)
        self.text_labels = text_labels
        self.tittle = self.text_labels.general_info_lbl
        self.content_dict = general_information
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
        for key in self.content_dict:
            item = QTreeWidgetItem(self.tree)
            #   Insert item "Key: Value" format
            item.setText(0, key + ': ' + str(self.content_dict[key]))

    def adjust_tree_widget_height(self):
        #   Calculate height
        total_height = self.tree.sizeHintForRow(0) * (len(self.content_dict))
        #   Set height
        self.tree.setMinimumHeight(total_height)
        self.tree.setMaximumHeight(total_height + 1)

    def update_general_info(self, general_information=None):
        if general_information is None:
            self.content_dict = {}
        else:
            self.content_dict = general_information
        #   Clear tree
        self.tree.clear()
        #   Repopulate tree
        self.populate_tree()

    def init_ui(self):
        self.collapsible_widget.collapsed_signal.connect(self.general_information_background_collapsed)
        #   Add expandable widget to layout
        self.general_layout.addWidget(self.collapsible_widget)
        #   Remove margins
        self.general_layout.setContentsMargins(0, 0, 0, 0)
        #   Set layout
        self.setLayout(self.general_layout)

    def general_information_background_collapsed(self, height):
        self.setMaximumHeight(height)


class HereditaryBackground(QWidget):
    def __init__(self, parent=None, text_labels=None, patient=None):
        super().__init__(parent)
        #   Multilingual obj.
        self.text_labels = text_labels
        #   Patient obj.
        self.patient = patient

        self.hereditary_layout = QVBoxLayout()
        self.my_test_dict_2 = {'abuela_materna': 'diabetes_mellitus_tipo_1', 'abuelo_materno':
            'carcinoma_de_células_escamosas_de_la_encía', 'papa': 'hiperesplenismo', 'mama': 'anisometropía'}

        self.hereditary_widget = WidgetTableButtons(self, self.my_test_dict_2)
        self.collapsible_widget = CollapsibleBox(self, self.text_labels.hereditary_lbl, self.hereditary_widget)
        #   UI
        self.init_ui()

    def init_ui(self):
        self.collapsible_widget.collapsed_signal.connect(self.hereditary_background_collapsed)
        #   Add expandable widget to layout
        self.hereditary_layout.addWidget(self.collapsible_widget)
        #   Remove margins
        self.hereditary_layout.setContentsMargins(0, 0, 0, 0)
        #   Set layout
        self.setLayout(self.hereditary_layout)

    def update_hereditary(self, patient=None):
        pass

    def update_height(self):
        pass

    def hereditary_background_collapsed(self, height):
        self.setMaximumHeight(height)

"""
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
        #   Remove margins
        self.immunizations_layout.setContentsMargins(0, 0, 0, 0)
        #   Set layout
        self.setLayout(self.immunizations_layout)
"""


class Allergy (QWidget):
    def __init__(self, parent=None, text_labels=None, allergies=None):
        super().__init__(parent)
        #   Layout
        self.allergies_layout = QVBoxLayout()
        self.text_labels = text_labels
        #   Contain individual tags.
        self.allergy_widgets = []
        #   Allergies
        self.allergies = allergies
        #   Widget containing all tags.
        self.widget = self.allergies_into_widget()
        self.scroll_widget = QScrollArea()
        self.scroll_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        # self.scroll_widget.setStyleSheet("border: none;")
        self.scroll_widget.setWidget(self.widget)
        self.collapsible_widget = CollapsibleBox(self, self.text_labels.allergies_lbl, self.scroll_widget)
        #   UI
        self.init_ui()

    def update_allergies(self, allergies=None):
        if allergies is None:
            self.allergies = allergies
            self.remove_allergies()
        else:
            self.allergies = allergies
            #   Remove self.widget contents
            self.remove_allergies()
            #   Remove self.widget
            #   Create new self.widget with new contents
            self.widget = self.allergies_into_widget()
            self.scroll_widget.setWidget(self.widget)
            #   Update content inside collapsible widget
            self.collapsible_widget.update_content(self.scroll_widget)

    def remove_allergies(self):
        for index, widget in enumerate(self.allergy_widgets):
            widget.deleteLater()

    def allergies_into_widget(self):
        #   Widget to be returned.
        widget = QWidget()
        #   Grid layout.
        grid_layout = QGridLayout()
        #   Columns of the Grid (Rows will be added as needed).
        grid_columns = 6
        # Variables to navigate Grid.
        column_counter = 0
        row_counter = 0
        #   Traverse grid.
        for allergy in self.allergies:
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

    def allergies_collapsed(self, height):
        self.setMaximumHeight(height)

    def init_ui(self):
        self.collapsible_widget.collapsed_signal.connect(self.allergies_collapsed)

        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.setMinimumHeight(150)
        #   Add expandable widget to layout
        self.allergies_layout.addWidget(self.collapsible_widget)
        #   Remove margins
        self.allergies_layout.setContentsMargins(0, 0, 0, 0)
        #   Set layout
        self.setLayout(self.allergies_layout)
