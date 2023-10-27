from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTreeWidgetItem, QTreeWidget,\
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
        #   Allergies
        self.allergies = allergies
        self.displayed_allergies = []
        #   Widget containing all tags.
        self.allergies_container = QWidget()
        self.container_layout = QGridLayout()
        self.contents_height = 0
        self.allergies_container.setLayout(self.container_layout)
        self.collapsible_widget = CollapsibleBox(self, self.text_labels.allergies_lbl, self.allergies_container)
        #   UI
        self.init_ui()
        self.update_allergies()

    def update_allergies(self, allergies=None):
        allergies = [] if allergies is None else allergies
        if allergies:
            self.allergies = allergies
            #   Remove displayed allergies.
            self.remove_allergies()
            #   Place new ones.
            self.place_allergies()
            #   Update content inside collapsible widget.
            #self.collapsible_widget.update_height(self.contents_height)
        else:
            self.allergies = []
            self.remove_allergies()
            self.place_allergies()
            #self.collapsible_widget.update_height(self.contents_height)

    def remove_allergies(self):
        if self.displayed_allergies:
            for widget in self.displayed_allergies:
                widget.deleteLater()

    def place_allergies(self):
        #   Size of empty container.
        empty_size = 100
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
            #   Container widget.
            allergy_widget = QWidget()
            allergy_widget.setLayout(allergy_layout)
            #   Place widget into Grid Layout.
            self.container_layout.addWidget(allergy_widget, row_counter, column_counter)
            #   Keep track of widgets added.
            self.displayed_allergies.append(allergy_widget)
            #   Implement column/row order.
            if column_counter < grid_columns:
                column_counter += 1
            else:
                column_counter = 0
                row_counter += 1
        #   Determine widget size.
        #   TODO look for bug, if statement should not be reversed.
        if not self.displayed_allergies:
            self.contents_height = empty_size
        else:
            self.contents_height = row_counter * self.displayed_allergies[-1].height() + empty_size
            print('row_counter:', row_counter, 'self.displayed_allergies[-1].height()', self.displayed_allergies[-1].height(), self.contents_height)

    def allergies_collapsed(self, height):
        self.setMaximumHeight(height)

    def init_ui(self):
        self.setStyleSheet('background: cyan;')
        self.allergies_container.setStyleSheet('background: pink;')
        self.container_layout.setContentsMargins(0, 0, 0, 0)
        self.container_layout.setSpacing(1)
        self.collapsible_widget.collapsed_signal.connect(self.allergies_collapsed)

        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        #self.setMinimumHeight(150)
        #   Add expandable widget to layout
        self.allergies_layout.addWidget(self.collapsible_widget)
        #   Remove margins
        self.allergies_layout.setContentsMargins(0, 0, 0, 0)
        self.allergies_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        #   Set layout
        self.setLayout(self.allergies_layout)
