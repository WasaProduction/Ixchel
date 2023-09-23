from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel


class SectionWidget(QWidget):
    def __init__(self, parent=None, my_label_text=None, my_contents=None):
        super(SectionWidget, self).__init__(parent)
        self.my_widgets = my_contents
        interrogatory_section_layout = QVBoxLayout()
        interrogatory_section_layout.addWidget(QLabel(my_label_text))
        # Prevent error while adding widget
        if self.my_widgets is not None:
            for widget in self.my_widgets:
                interrogatory_section_layout.addWidget(widget)
        self.setLayout(interrogatory_section_layout)

    def retrieve_data(self):
        my_data = []
        for widget in self.my_widgets:
            my_data.append(widget.retrieve_data())
        return my_data if len(my_data) > 0 else None
