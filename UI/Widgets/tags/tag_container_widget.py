from PyQt6.QtWidgets import QWidget, QGridLayout, QSizePolicy, QVBoxLayout, QLabel
from PyQt6.QtCore import pyqtSignal
from UI.Widgets.collapsible_box import CollapsibleBox
from data_models.model_tag import ModelTag
from mongodb.read.get_affection import GetAffection
from mongodb.read.get_color import GetColor
from UI.Widgets.tags.tag_individual_widget import TagIndividualWidget


class PathologicalCollapsible(QWidget):
    toggled_signal = pyqtSignal(int)

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
        self.years_container.toggled_signal.connect(self.height_updated)
        self.collapsible_widget = CollapsibleBox(self, title=self.text_labels.pathologic_lbl,
                                                 content=self.years_container)
        self.collapsible_widget.toggled_signal.connect(self.height_updated)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.collapsible_widget)
        self.layout.setStretchFactor(self.collapsible_widget, 1)
        self.init_ui()

    def height_updated(self, height):
        self.toggled_signal.emit(height)

    def update_pathological(self, patient):
        self.years_container.update_years_collapsible(patient)
        self.collapsible_widget.update_height(self.years_container.content_height)
        self.setMaximumHeight(self.years_container.content_height + 50)

    def pathological_collapsed(self, height):
        self.setMaximumHeight(height)

    def init_ui(self):
        #   Connect signal
        self.collapsible_widget.toggled_signal.connect(self.pathological_collapsed)
        #   Configure margins
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        # self.setFrameShape(QFrame.Shape.NoFrame)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)


class YearsCollapsible(QWidget):
    toggled_signal = pyqtSignal(int)

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
        self.test_years = []
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

    def height_updated(self):
        #   Calculate height.
        self.content_height = 0
        for widget in self.test_years:
            self.content_height += widget.height()
        self.toggled_signal.emit(self.content_height)

    def tags_into_layout(self):
        #   Clear layout
        while self.year_container_lyt.count():
            item = self.year_container_lyt.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        #   No data retrieved.
        if not self.year_diagnoses_dict:
            not_lbl = QLabel(self.text_labels.no_data_lbl)
            not_lbl.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
            self.content_height = not_lbl.height()
            self.year_container_lyt.addWidget(not_lbl)
            return

        # Add a CollapsibleBox per Year into scroll area
        for index, year in enumerate(self.year_diagnoses_dict):
            #   Pass each CollapsibleBox all the contained tags
            year_widget = CollapsibleBox(self, title=str(year), content=TagsContainer(self,
                                                                                      self.year_diagnoses_dict[year],
                                                                                      text_labels=self.text_labels))
            year_widget.toggled_signal.connect(self.height_updated)

            #   Connect signal
            self.test_years.append(year_widget)
            #   Keep track of displayed years.
            self.displayed_years[year] = year_widget
            #   Keep track of height in order to update correctly when updating widget.
            self.content_height += year_widget.height()
            self.year_container_lyt.addWidget(year_widget)
            #   Allow widgets stretch to avoid overlapping text.
            self.year_container_lyt.setStretchFactor(year_widget, 1)
            #   Avoid overlapping boxes.
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
            for i, year in enumerate(years):
                #   Delete tags contained inside year.
                self.displayed_years[year].received_content.remove_tags()
                #   Delete year
                self.displayed_years[year].deleteLater()
                #   Remove year form displayed
                del self.displayed_years[year]
                #years.pop(i)

    def update_years(self, years):
        #   Update already present years
        for year in years:
            #   Remove tags contained inside year.
            self.displayed_years[year].received_content.remove_tags()
            #   Add renewed tags inside year.

    def update_years_collapsible(self, patient=None):
        self.test_years = []
        #   Remove years
        self.remove_years(list(self.year_diagnoses_dict.keys()))
        #   Extract tags into a dict (update).
        self.year_diagnoses_dict = self.extract_diagnoses_yearly(patient)
        #   Update presented tags
        self.tags_into_layout()
        #   Update currently displayed years array.
        self.displayed_years = list(self.year_diagnoses_dict.keys())

    def year_collapsed(self, height):
        self.setMaximumHeight(height)

    """     UI      """
    def init_ui(self):
        #   Remove border
        self.setStyleSheet("border: none;")
        #   Keep the preferred vertical size policy
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)


class TagsContainer(QWidget):
    #   Set of individual tags displayed in a grid layout.
    def __init__(self, parent=None, diagnoses=None, text_labels=None):
        super().__init__(parent)
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
        #   Layout
        self.my_layout = QGridLayout()
        #   Get tags inside layout
        self.place_tags()
        #   UI
        self.init_ui()

    def place_tags(self):
        #   Trackers
        column_tracker = 0
        row_tracker = 0
        #   Row length.
        row_len = 600
        current_row_len = row_len
        #   To calculate tag widths.
        font_metrics = QLabel().fontMetrics()
        #   Create every tag.
        for index in range(len(self.tags_array)):
            #   Tag object.
            tag = TagIndividualWidget(self.tags_array[-1])
            #   Calculate tag widths.
            tag_width = font_metrics.horizontalAdvance(tag.text())
            #   Tag is bigger than the entire row.
            if tag_width >= row_len:
                #   Jump to next row if there are already objects in it
                if current_row_len != row_len:
                    row_tracker += 1
                    column_tracker = 0
                #   Keep track of displayed tags
                self.tags_in_display.append(tag)
                #   Add widget
                self.my_layout.addWidget(tag, row_tracker, column_tracker)
                self.tags_array.pop()
                #   Reset row len.
                current_row_len = row_len
                #   Break line
                row_tracker += 1
                column_tracker = 0
                continue

            #   Enough space inline for tag.
            if current_row_len - tag_width > 0:
                #   Keep track of displayed tags
                self.tags_in_display.append(tag)
                #   Add widget
                self.my_layout.addWidget(tag, row_tracker, column_tracker)
                self.tags_array.pop()
                #   Update remaining space.
                current_row_len -= tag_width
                #   Update column.
                column_tracker += 1
                continue
            #   Break line and go to a new line.
            else:
                #   Break line
                row_tracker += 1
                column_tracker = 0
                #   Reset row len.
                current_row_len = row_len
                #   Keep track of displayed tags
                self.tags_in_display.append(tag)
                #   Add widget
                self.my_layout.addWidget(tag, row_tracker, column_tracker)
                self.tags_array.pop()
                #   Update remaining space.
                current_row_len -= tag_width
                #   Update column.
                column_tracker += 1

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
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        #   Configure margins
        self.setContentsMargins(0, 0, 0, 0)
        #   Configure H spacing
        self.my_layout.setHorizontalSpacing(3)
        #   Configure V spacing
        self.my_layout.setVerticalSpacing(3)
        # Applying layout to the widget
        self.setLayout(self.my_layout)
