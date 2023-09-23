from PyQt6.QtWidgets import QWidget, QVBoxLayout,  QHBoxLayout, QLabel, QScrollArea, QTreeWidgetItem, QTreeWidget,\
    QSizePolicy, QFrame, QGridLayout
from PyQt6.QtCore import Qt
from UI.Widgets.icons.allergy_icon import AllergyIcon
from UI.Widgets.collapsible_box import CollapsibleBox


class GeneralInformation(QWidget):
    def __init__(self, general_information):
        super().__init__()
        general_layout = QVBoxLayout()
        section_title = QLabel("General Information")
        general_layout.addWidget(section_title)
        arr = ['Age: 28', 'Weight: 70', 'Height: 1.76']
        # My tree
        tree = QTreeWidget(self)
        general_layout.addWidget(tree)
        self.setLayout(general_layout)
        for element in arr:
            element_itm = QTreeWidgetItem(tree)
            element_itm.setText(0, element)

        height_lbl = QLabel('1.76')
        weight = QLabel('70')
        tattoos = True


class HereditaryBackground(QWidget):
    def __init__(self, hereditary_information):
        super().__init__()
        hereditary_layout = QVBoxLayout()
        section_title = QLabel('Hereditary Background')
        hereditary_layout.addWidget(section_title)
        self.setLayout(hereditary_layout)


class PathologicBackground(QWidget):
    def __init__(self, pathologic_information):
        super().__init__()
        pathologic_layout = QVBoxLayout()
        section_title = QLabel('Pathologic Background')
        pathologic_layout.addWidget(section_title)
        self.setLayout(pathologic_layout)


class Immunizations(QWidget):
    def __init__(self, immunizations_information):
        super().__init__()
        immunizations_layout = QVBoxLayout()
        section_title = QLabel('Hereditary Background')
        immunizations_layout.addWidget(section_title)
        self.setLayout(immunizations_layout)


class Allergy (QWidget):
    def __init__(self, allergies_information):
        super().__init__()
        allergies_layout = QVBoxLayout()
        section_title = QLabel("Allergies")
        allergies_layout.addWidget(section_title)
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
