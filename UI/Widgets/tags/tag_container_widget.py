from PyQt6.QtWidgets import QWidget, QGridLayout, QScrollArea, QVBoxLayout
from UI.Widgets.collapsible_box import CollapsibleBox
from PyQt6.QtCore import Qt
from data_models.model_tag import ModelTag
from mongodb.read.get_affection import GetAffection
from mongodb.read.get_color import GetColor
from UI.Widgets.tags.tag_individual_widget import TagIndividualWidget
import math


class PathologicalContainer(QScrollArea):
    def __init__(self, parent=None, patient=None):
        super().__init__(parent)
        """     Tags Section    """
        self.setFixedHeight(150)
        self.setWidgetResizable(True)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        tags_container_layout = QVBoxLayout()
        tags_container_layout.setSpacing(5)
        # Tags will be displayed in a yearly manner
        year_diagnoses_dict = {}
        for diagnosis in patient.diagnosis_entries:
            # List all years with existing records
            if diagnosis.creation_date.year not in year_diagnoses_dict:
                year_diagnoses_dict[diagnosis.creation_date.year] = [diagnosis]
            else:
                year_diagnoses_dict[diagnosis.creation_date.year].append(diagnosis)
        # Sort dict
        years_list = list(year_diagnoses_dict.keys())
        years_list.sort(reverse=True)
        year_diagnoses_dict = {key: year_diagnoses_dict[key] for key in years_list}
        # Add a CollapsibleBox per Year into scroll area
        for index, year in enumerate(year_diagnoses_dict):
            tags_container_layout.addWidget(CollapsibleBox(self, title=str(year),
                                                           content=TagContainerWidget(year_diagnoses_dict[year])))
            #   Add spacing, to avoud overlaping
            tags_container_layout.setStretch(index, 10)
        self.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.setLayout(tags_container_layout)



class TagContainerWidget(QWidget):
    def __init__(self, diagnoses):
        # For help on the grid https://realpython.com/python-pyqt-layout/
        super().__init__()
        self.tags_array = []
        self.colors_dict = GetColor().get_colors_dict()
        self.gather_tag_data(diagnoses)
        # Maximum number of columns for the tags
        max_colum_number = 6
        # Calculate rows required in order to display all the tags
        extra_row = False if len(self.tags_array) % max_colum_number == 0 else True
        max_row_number = math.trunc((len(self.tags_array) / max_colum_number) + 1 if extra_row else
                                    (len(self.tags_array) / max_colum_number))
        # Setting the layout
        my_layout = QGridLayout()
        for x in range(max_row_number):
            for y in range(max_colum_number):
                my_layout.addWidget(TagIndividualWidget(self.tags_array[-1]), x, y)
                self.tags_array.pop()
        # Applying layout to the widget
        my_layout.setHorizontalSpacing(5)
        my_layout.setVerticalSpacing(10)
        self.setLayout(my_layout)

    def gather_tag_data(self, diagnoses):
        for diagnose in diagnoses:
            for tag in diagnose.tags_contained:
                self.tags_array.append(ModelTag(diagnosis_id=diagnose.diagnosis_id, creation_date=diagnose.creation_date
                                                , name=GetAffection(tag).get_affection(),
                                                color=self.colors_dict[tag[:1]]))
