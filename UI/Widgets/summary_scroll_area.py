from PyQt6.QtWidgets import QWidget, QScrollArea, QVBoxLayout, QSizePolicy, QFrame
from PyQt6.QtCore import Qt, QEvent, QSize
from UI.Widgets.background import GeneralInformation, HereditaryBackground, Allergy
from UI.Widgets.tags.tag_container_widget import PathologicalCollapsible


class SummaryScrollArea(QScrollArea):
    #   Scroll container of General information, hereditary & pathologic background, immunizations and allergies
    def __init__(self, parent=None, text_labels=None, patient=None):
        super().__init__(parent)
        #   Parameters
        self.text_labels = text_labels
        self.patient = patient
        """     Widgets     """
        self.general_information = GeneralInformation(self, self.text_labels, patient.general_info)
        self.hereditary_background = HereditaryBackground(self, self.text_labels, self.patient)
        self.allergy = Allergy(self, self.text_labels, self.patient.allergies)
        self.pathologic_background = PathologicalCollapsible(self, self.text_labels, self.patient)
        #   Heights.
        self.general_info_height = self.general_information.height()
        self.hereditary_background_height = self.hereditary_background.height()
        self.allergy_height = self.allergy.height()
        self.pathologic_background_height = self.pathologic_background.height()
        """     Height signals.     """
        self.general_information.toggled_signal.connect(self.general_info_toggled)
        self.allergy.toggled_signal.connect(self.allergy_toggled)
        self.hereditary_background.toggled_signal.connect(self.hereditary_toggled)
        self.pathologic_background.toggled_signal.connect(self.pathologic_toggled)
        #   UI
        self.init_ui()
        #   Container widget
        self.container_widget = QWidget()
        self.container_widget_height = self.container_widget.height()
        #   Layout
        self.layout = QVBoxLayout()
        self.tune_container_layout()
        self.container_widget.setLayout(self.layout)
        self.tune_container_widget()
        self.setWidget(self.container_widget)

    def update_container_widget_height(self):
        #   Calculate new height.
        self.container_widget_height = self.general_info_height + self.allergy_height + \
                                       self.hereditary_background_height + self.pathologic_background_height
        #   Apply height.
        self.container_widget.setMinimumHeight(self.container_widget_height)

    def general_info_toggled(self, height):
        #   Update section height.
        self.general_info_height = height
        #   Update containers height.
        self.update_container_widget_height()

    def allergy_toggled(self, height):
        #   Update section height.
        self.allergy_height = height
        #   Update containers height.
        self.update_container_widget_height()

    def hereditary_toggled(self, height):
        #   Update section height.
        self.hereditary_background_height = height
        #   Update containers height.
        self.update_container_widget_height()

    def pathologic_toggled(self, height):
        #   Update section height.
        self.pathologic_background_height = height
        #   Update containers height.
        self.update_container_widget_height()

    #   Force widget to adapt all available width while retaining its height.
    def eventFilter(self, obj, event):
        if obj == self.widget() and event.type() == QEvent.Type.Resize:
            self.widget().resize(self.calculate_size())
            return True
        return super(SummaryScrollArea, self).eventFilter(obj, event)

    def calculate_size(self):
        return QSize(self.width(), self.container_widget.height())

    def tune_container_widget(self):
        self.container_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.container_widget.setLayout(self.layout)

    def tune_container_layout(self):
        self.setAlignment(Qt.AlignmentFlag.AlignLeft)
        #   Customize margins
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(1)
        #   Adding widgets to layout.
        self.layout.addWidget(self.general_information)
        self.layout.addWidget(self.hereditary_background)
        self.layout.addWidget(self.allergy)
        self.layout.addWidget(self.pathologic_background)
        # Traverse and print the widgets in the QVBoxLayout.
        for i in range(self.layout.count()):
            item = self.layout.itemAt(i)
            if item is not None:
                #   Allow widget to occupy the whole layout width.
                self.layout.setStretchFactor(item.widget(), 1)
                self.layout.setStretch(i, 1)
                if i != self.layout.count() - 1:
                    #   Allow widgets stretch to avoid overlapping.
                    self.layout.setStretch(i, 1)
                else:
                    #   Last widget is to stretch further than most.
                    self.layout.setStretch(i, 5)
        #   Stack widgets atop.
        self.layout.addStretch()

    def update_summary_scroll_area(self, patient=None):
        self.patient = patient
        self.general_information.update_general_info(self.patient.general_info)
        self.hereditary_background.update_hereditary(self.patient)
        self.allergy.update_allergies(self.patient.allergies)
        self.pathologic_background.update_pathological(self.patient)

    """     UI      """
    def init_ui(self):
        # self.setWidgetResizable(True)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.setFrameShape(QFrame.Shape.NoFrame)
