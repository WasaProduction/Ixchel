from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTreeWidgetItem, QTreeWidget,\
    QGridLayout, QSizePolicy
from PyQt6.QtCore import Qt, pyqtSignal
from UI.Frames.editing_area.tables.custom_table_hereditary import WidgetTableButtons
from UI.Widgets.icons.allergy_icon import AllergyIcon
from UI.Widgets.collapsible_box import CollapsibleBox


class GeneralInformation(QWidget):
    toggled_signal = pyqtSignal(int)

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
        self.collapsible_widget.toggled_signal.connect(self.height_updated)
        self.init_ui()

    def height_updated(self, height):
        self.toggled_signal.emit(height)

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
        self.collapsible_widget.toggled_signal.connect(self.general_information_background_collapsed)
        #   Add expandable widget to layout
        self.general_layout.addWidget(self.collapsible_widget)
        #   Remove margins
        self.general_layout.setContentsMargins(0, 0, 0, 0)
        #   Set layout
        self.setLayout(self.general_layout)

    def general_information_background_collapsed(self, height):
        self.setMaximumHeight(height)


class HereditaryBackground(QWidget):
    toggled_signal = pyqtSignal(int)

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
        self.collapsible_widget.toggled_signal.connect(self.height_updated)
        #   UI
        self.init_ui()

    def height_updated(self, height):
        self.toggled_signal.emit(height)

    def init_ui(self):
        self.collapsible_widget.toggled_signal.connect(self.hereditary_background_collapsed)
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
    #   Custom signal.
    toggled_signal = pyqtSignal(int)

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

        self.layout_rows = 0
        self.contents_height = 0
        self.allergies_container.setLayout(self.container_layout)
        self.collapsible_widget = CollapsibleBox(self, self.text_labels.allergies_lbl, self.allergies_container)
        self.collapsible_widget.toggled_signal.connect(self.height_updated)
        #   UI
        self.init_ui()
        self.update_allergies()

    def height_updated(self, height):
        self.toggled_signal.emit(height)

    def update_allergies(self, allergies=None):
        allergies = [] if allergies is None else allergies
        if allergies:
            #   Remove displayed allergies.
            self.remove_allergies()
            #   Update variable.
            self.allergies = allergies
            #   Place new ones.
            self.place_allergies()
            #
            self.collapsible_widget.update_height(self.contents_height)
            self.setMaximumHeight(self.contents_height + 50)

        else:
            self.allergies = []
            self.remove_allergies()
            self.place_allergies()
            self.collapsible_widget.update_content(self.allergies_container)

    def remove_allergies(self):
        if self.displayed_allergies:
            for i, widget in enumerate(self.displayed_allergies):
                widget.deleteLater()
                self.displayed_allergies.pop(i)

    def place_allergies(self):
        #   Size of empty container.
        empty_size = 100
        #   Columns of the Grid (Rows will be added as needed).
        grid_columns = 6
        # Variables to navigate Grid.
        column_counter = 0
        self.layout_rows = 0
        if not self.allergies:
            no_allergies = QLabel(self.text_labels.no_data_lbl)
            self.container_layout.addWidget(no_allergies, 0, 0)
            self.displayed_allergies.append(no_allergies)

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
            self.container_layout.addWidget(allergy_widget, self.layout_rows, column_counter)
            #   Keep track of widgets added.
            self.displayed_allergies.append(allergy_widget)
            #   Implement column/row order.
            if column_counter < grid_columns:
                column_counter += 1
            else:
                column_counter = 0
                self.layout_rows += 1
        #   Determine widget size.
        self.contents_height = self.layout_rows * 50 + empty_size

    def allergies_collapsed(self, height):
        self.setMaximumHeight(height)

    def init_ui(self):
        self.container_layout.setContentsMargins(0, 0, 0, 0)
        self.container_layout.setSpacing(1)
        self.collapsible_widget.toggled_signal.connect(self.allergies_collapsed)

        self.collapsible_widget.setStyleSheet('background: cyan')
        self.allergies_container.setStyleSheet('background: pink')

        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        self.allergies_container.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)

        #   Add expandable widget to layout
        self.allergies_layout.addWidget(self.collapsible_widget)
        #   Remove margins
        self.allergies_layout.setContentsMargins(0, 0, 0, 0)
        self.allergies_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        #   Set layout
        self.setLayout(self.allergies_layout)
