from PyQt6.QtWidgets import QWidget, QGridLayout, QSizePolicy, QVBoxLayout, QScrollArea, QFrame, QLabel
from UI.Widgets.collapsible_box import CollapsibleBox
from data_models.model_tag import ModelTag
from mongodb.read.get_affection import GetAffection
from mongodb.read.get_color import GetColor
from UI.Widgets.tags.tag_individual_widget import TagIndividualWidget
import math


class PathologicalCollapsible(QScrollArea):
    #   Collapsable container of a set of years containing individual tags
    def __init__(self, parent=None, text_labels=None, patient=None):
        super().__init__(parent)
        """     For testing     """
        self.testing = False
        """     Testing end     """
        #   Button tittle.
        self.text_labels = text_labels
        #   Patient obj.
        self.patient = patient
        #   TODO No tags to display.
        if self.patient.diagnosis_entries is None:
            pass
        self.years_container = YearsCollapsible(self, self.patient, self.text_labels)
        self.collapsible = CollapsibleBox(self, title=self.text_labels.pathologic_lbl, content=self.years_container)
        self.layout = QVBoxLayout()
        self.container_widget = QWidget()
        self.layout.addWidget(self.collapsible)
        self.layout.setStretchFactor(self.collapsible, 1)
        self.init_ui()

    def update_pathological(self, patient):
        self.years_container.update_years_collapsible(patient)
        self.collapsible.update_height(self.years_container.content_height)

    def init_ui(self):
        #   Configure margins
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.container_widget.setLayout(self.layout)
        #self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setWidget(self.collapsible)


class YearsCollapsible(QWidget):
    #   Set of collapsible years containing tags.
    def __init__(self, parent=None, patient=None, text_labels=None):
        super().__init__(parent)
        #   Button tittle.
        self.text_labels = text_labels
        """     For testing     """
        self.testing = False
        """     Testing end     """
        self.content_height = 0
        """     Tags Section    """
        #   One collapsible box per year.
        self.year_container_lyt = self.create_year_container_lyt()
        #   Extract tags into a dict.
        self.year_diagnoses_dict = self.extract_diagnoses_yearly(patient)
        #   Keep track of currently displayed years
        self.displayed_years = {}  # list(self.year_diagnoses_dict.keys())
        #   Get the tags into a layout.
        self.tags_into_layout()
        #   Set layout.
        self.setLayout(self.year_container_lyt)
        #   Ui.
        self.init_ui()

    def tags_into_layout(self):
        #   Clear layout
        while self.year_container_lyt.count():
            item = self.year_container_lyt.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        if not self.year_diagnoses_dict:
            not_lbl = QLabel(self.text_labels.no_data_lbl)
            not_lbl.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
            self.content_height = not_lbl.height()
            self.year_container_lyt.addWidget(not_lbl)
            return

        # Add a CollapsibleBox per Year into scroll area
        for index, year in enumerate(self.year_diagnoses_dict):
            #   Pass each CollapsibleBox all the contained tags
            year_widget = CollapsibleBox(self, title=str(year), content=TagsContainer(self.year_diagnoses_dict[year],
                                                                                      text_labels=self.text_labels))
            self.displayed_years[year] = year_widget
            self.content_height += year_widget.height()
            self.year_container_lyt.addWidget(year_widget)
            #   Allow widgets stretch to avoid overlapping.
            self.year_container_lyt.setStretchFactor(year_widget, 1)
            #   Avoid overlapping boxes
            self.year_container_lyt.setStretch(index, 3)
        self.year_container_lyt.addStretch()

    @staticmethod
    def extract_diagnoses_yearly(patient=None):
        year_diagnoses_dict = {}
        # Tags will be displayed in a yearly manner
        for diagnosis in patient.diagnosis_entries:
            # List all years with existing records
            if diagnosis.creation_date.year not in year_diagnoses_dict:
                year_diagnoses_dict[diagnosis.creation_date.year] = [diagnosis]
            else:
                year_diagnoses_dict[diagnosis.creation_date.year].append(diagnosis)
        #   Sort dict
        years_list = list(year_diagnoses_dict.keys())
        #   Show most recent years first
        years_list.sort(reverse=True)
        year_diagnoses_dict = {key: year_diagnoses_dict[key] for key in years_list}
        return year_diagnoses_dict

    @staticmethod
    def create_year_container_lyt():
        year_container_lyt = QVBoxLayout()
        #   Configure margins
        year_container_lyt.setContentsMargins(0, 0, 0, 0)
        #   Configure spacing
        year_container_lyt.setSpacing(5)
        return year_container_lyt

    def remove_years(self, years=None):
        if years is not None and years:
            #   Remove years not supposed to be displayed
            for year in years:
                #   Delete tags contained inside year.
                self.displayed_years[year].received_content.remove_tags()
                #   Delete year
                self.displayed_years[year].deleteLater()
                #   Remove year form displayed
                del self.displayed_years[year]

    def update_years(self, years):
        #   Update already present years
        for year in years:
            #   Remove tags contained inside year.
            self.displayed_years[year].received_content.remove_tags()
            #   Add renewed tags inside year.

    def update_years_collapsible(self, patient=None):
        #   Remove years
        self.remove_years(list(self.year_diagnoses_dict.keys()))
        #   Extract tags into a dict (update).
        self.year_diagnoses_dict = self.extract_diagnoses_yearly(patient)
        #   Update presented tags
        self.tags_into_layout()
        #   Update currently displayed years array.
        self.displayed_years = list(self.year_diagnoses_dict.keys())

    """     UI      """

    def init_ui(self):
        #   Remove border
        self.setStyleSheet("border: none;")
        #   Keep the preferred vertical size policy
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)


class TagsContainer(QWidget):
    #   Set of individual tags.
    def __init__(self, diagnoses, text_labels=None):
        super().__init__()
        #   Button tittle.
        self.text_labels = text_labels
        #   Keep track of tracks tags (as a widget) being displayed.
        self.tags_in_display = []
        #   Save tags (as data)
        self.tags_array = []
        #   Tag colors
        self.colors_dict = GetColor().get_colors_dict()
        #   Extract data
        self.gather_tag_data(diagnoses)
        #   Maximum number of columns for the tags
        self.max_colum_number = 6
        #   Calculate & Rows required in order to display all the tags.
        self.extra_row = self.determine_extra_row()
        self.max_row_number = self.calculate_row_number()
        #   Layout
        self.my_layout = QGridLayout()
        #   Get tags inside layout
        self.place_tags()
        #   UI
        self.init_ui()

    def determine_extra_row(self):
        return False if len(self.tags_array) % self.max_colum_number == 0 else True

    def calculate_row_number(self):
        return math.trunc((len(self.tags_array) / self.max_colum_number) + 1 if self.extra_row else
                          (len(self.tags_array) / self.max_colum_number))

    def place_tags(self):
        # Setting the layout
        for x in range(self.max_row_number):
            for y in range(self.max_colum_number):
                tag = TagIndividualWidget(self.tags_array[-1])
                self.tags_in_display.append(tag)
                self.my_layout.addWidget(tag, x, y)
                self.tags_array.pop()

    def remove_tags(self):
        #   Traverse tags
        for tag in self.tags_in_display:
            #   Remove tag from layout
            self.my_layout.removeWidget(tag)
            #   Delete widget
            tag.deleteLater()
        #   Reset widget
        self.tags_in_display = []

    def update_tags(self, diagnoses):
        #   Remove currently displayed tags.
        self.remove_tags()
        #   Update data container
        self.gather_tag_data(diagnoses)
        #   Calculate & Rows required in order to display all the tags.
        self.extra_row = self.determine_extra_row()
        self.max_row_number = self.calculate_row_number()
        #   Place new tags.
        self.place_tags()

    def gather_tag_data(self, diagnoses):
        for diagnose in diagnoses:
            for tag in diagnose.tags_contained:
                self.tags_array.append(ModelTag(diagnosis_id=diagnose.diagnosis_id,
                                                creation_date=diagnose.creation_date,
                                                name=GetAffection(tag).get_affection(),
                                                color=self.colors_dict[tag[:1]]))

    """     UI      """

    def init_ui(self):
        #   Configure margins
        self.setContentsMargins(0, 0, 0, 0)
        #   Configure H spacing
        self.my_layout.setHorizontalSpacing(2)
        #   Configure V spacing
        self.my_layout.setVerticalSpacing(3)
        # Applying layout to the widget
        self.setLayout(self.my_layout)
