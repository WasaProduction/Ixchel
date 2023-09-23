from PyQt6.QtWidgets import QDialog, QLabel, QDialogButtonBox, QWidget, QDateEdit, QTimeEdit, QFormLayout, QGridLayout
from PyQt6.QtCore import QDateTime
from data_models.agenda_entry import AgendaEntry
from datetime import datetime


class AppointmentPrompt(QDialog):
    def __init__(self, parent=None, selected_day=None):
        super().__init__(parent)
        #   Ensure there's selection
        if selected_day is None:
            selected_day = datetime.now()
        #   Datetime() into QDateTime()
        q_selected_day = QDateTime.fromString(selected_day.strftime("%Y-%m-%d %H:%M:%S"), 'yyyy-MM-dd hh:mm:ss')
        #   Container widget
        self.my_widget = DatePickerWidget(self, q_selected_day)
        #   Connect container widget buttons to QDialog properties
        self.my_widget.ok_cancel.accepted.connect(self.accept)
        self.my_widget.ok_cancel.rejected.connect(self.reject)
        #   Set UI
        self.init_ui()

    def retrieve_data(self):
        #   Retrieve data from widget
        return self.my_widget.retrieve_data()

    """     UI      """
    def init_ui(self):
        layout = QFormLayout(self)
        layout.addWidget(self.my_widget)
        self.setWindowTitle('New appointment')
        self.setLayout(layout)


class DatePickerWidget(QWidget):
    def __init__(self, parent=None, selected_day=None):
        super().__init__(parent)
        #   Minutes
        self.default_appointment_time = 30 * 60
        #   Date
        self.date_lbl = QLabel('Date:')
        self.date_pick = QDateEdit()
        #   Set picker to selected date
        self.date_pick.setDate(selected_day.date())
        #   Start
        self.start_lbl = QLabel('Start:')
        self.start_time_picker = QTimeEdit()
        self.start_time_picker.timeChanged.connect(lambda: self.autoupdate_end())
        #   Set picker to selected time
        self.start_time_picker.setTime(selected_day.time())
        #   End
        self.end_lbl = QLabel('End:')
        self.end_time_picker = QTimeEdit()
        #   Set picker to selected time
        self.end_time_picker.setTime(selected_day.time().addSecs(self.default_appointment_time))
        #   Ok & Cancel buttons
        self.ok_cancel = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel,
                                          self)
        self.init_ui()

    def autoupdate_end(self):
        #   End time is updated to be default_appointment_time apart from the start
        try:
            self.end_time_picker.setTime(self.start_time_picker.time().addSecs(self.default_appointment_time))
        except AttributeError:
            #   Happens while initializing
            pass

    def retrieve_data(self):
        #   Retrieve start time and turn into Datetime()
        start_time = self.start_time_picker.time().toPyTime()
        #   Retrieve end time and turn into Datetime()
        end_time = self.end_time_picker.time().toPyTime()
        #   Retrieve date and turn into Datetime()
        date = self.date_pick.date().toPyDate()
        #   Return appointment
        return AgendaEntry(start=datetime.combine(date, start_time), end=datetime.combine(date, end_time),
                           location='Here', id_attendee='Terry Crew', id_medic='Dr. Zeus', id_organizer='Betty',
                           status=None)

    def init_ui(self):
        """     Widget layout       """
        #   Widget layout
        my_layout = QGridLayout()
        #   Date row
        my_layout.addWidget(self.date_lbl, 0, 0, 1, 1)
        my_layout.addWidget(self.date_pick, 0, 1, 1, 2)
        #   Start time row
        my_layout.addWidget(self.start_lbl, 1, 0, 1, 1)
        my_layout.addWidget(self.start_time_picker, 1, 1, 1, 2)
        #   End time row
        my_layout.addWidget(self.end_lbl, 2, 0, 1, 1)
        my_layout.addWidget(self.end_time_picker, 2, 1, 1, 2)
        #   Ok Cancel row
        my_layout.addWidget(self.ok_cancel, 3, 0, 1, 3)
        #   Set widget layout
        self.setLayout(my_layout)
