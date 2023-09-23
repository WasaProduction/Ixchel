from PyQt6.QtWidgets import QWidget, QGridLayout
from data_models.model_tag import ModelTag
from mongodb.read.get_affection import GetAffection
from mongodb.read.get_color import GetColor
from UI.Widgets.tags.tag_individual_widget import TagIndividualWidget
import math


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
