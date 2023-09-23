from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QSizePolicy, QPushButton
from UI.Widgets.Calendar.agenda import Agenda
from UI.Widgets.Calendar.custom_calendar import CustomCalendar
from UI.Widgets.Calendar.AppointmentPrompt import AppointmentPrompt
from datetime import datetime, timedelta
from mongodb.read.get_holidays import GetHolidays
from UI.Widgets.Alerts.error import Error


class CalendarAgendaWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        """     Init widgets        """
        #   Retrieve holidays form db
        holidays = GetHolidays()
        #   Widget displaying the agenda
        self.agenda = Agenda(self)
        #   Widget displaying the calendar
        self.calendar = CustomCalendar(self)
        #   Pass holidays to calendar
        self.calendar.update_holidays(holidays)
        #   Update agenda to show today's week
        self.agenda.update_displayed_week(self.get_week_or_day(get_week=True))
        #   Connect calendar signal to the agenda & update agenda accordingly
        self.calendar.selectionChanged.connect(lambda: self.agenda.update_displayed_week(self.get_week_or_day()))
        #   set UI
        self.init_ui()

    def change_work_week(self):
        #   Switch between displaying work week (5 days) & week (7 days)
        self.agenda.switch_work_week()

    def get_week_or_day(self, get_week=True):
        #   Get selected week
        week = self.calendar.selectedDate().toPyDate().isocalendar()
        #   Week number
        week_num = week.week
        #   Year
        year = week.year
        #   Format for strptime
        year_week = str(year) + '-W' + str(week_num)
        if not get_week:
            return self.calendar.selectedDate().toPyDate()
        #   Dates from Mon to Sat
        #   If not ISO %Y-W%W-%w
        week = [datetime.strptime(year_week + str(x), "%G-W%V-%u") for x in reversed(range(-6, 0))]
        #   Append Sunday
        week.append((week[0] + timedelta(days=6.9)))
        #   Return selected week
        return week

    def create_appointment(self):
        #   Retrieve selected day & combine it with current time.
        my_date = datetime.combine(self.get_week_or_day(get_week=False), datetime.now().time())
        #   Check if date is in the past
        if datetime.now() - timedelta(minutes=1) > my_date:
            error_title = 'Whoops'
            error_message = 'Can\'t meet on the past mate'
            Error(self, title=error_title, message=error_message)
        else:
            #   Create appointment prompt
            prompt = AppointmentPrompt(self, my_date)
            #   Retrieve data from prompt
            if prompt.exec():
                print(prompt.retrieve_data())

    """     UI      """
    def init_ui(self):
        #   Calendar
        calendar_column_layout = QVBoxLayout()
        calendar_column_layout.addWidget(self.calendar)
        add_appointment_button = QPushButton('Add')
        add_appointment_button.clicked.connect(lambda: self.create_appointment())
        calendar_column_layout.addWidget(add_appointment_button)
        calendar_column_layout.addStretch()
        #   Prevent calendar from using excessive vertical space
        calendar_column_layout.addStretch()
        calendar_column = QWidget()
        calendar_column.setLayout(calendar_column_layout)
        #   Whole widget
        my_layout = QHBoxLayout()
        my_layout.addWidget(self.agenda)
        my_layout.addWidget(calendar_column)
        self.setLayout(my_layout)

    def hide_calendar(self):
        if self.calendar.isHidden():
            self.calendar.show()
        else:
            self.calendar.hide()

    def tune_ui(self):
        #   Month calendar
        calendar_column_layout = QVBoxLayout()
        calendar_column_layout.addWidget(self.calendar)
        #   Prevent calendar from using excessive space
        calendar_column_layout.addStretch()
        calendar_column = QWidget()
        calendar_column.setLayout(calendar_column_layout)
        """     Set size policies       """
        calendar_column.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.agenda.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        """     Add layout to this widget       """
        my_layout = QHBoxLayout()
        my_layout.addWidget(self.agenda, stretch=2)
        my_layout.addWidget(calendar_column, stretch=1)
        self.setLayout(my_layout)
