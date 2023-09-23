from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QScrollArea, QSizePolicy, QVBoxLayout
from PyQt6.QtCore import Qt
from UI.Widgets.Calendar.day_header import DayHeader
from UI.Widgets.Calendar.line_frame import LineFrame
from UI.Widgets.Calendar.entry import FrameEntry
from mongodb.read.get_agenda_entries import GetAgendaEntries
from datetime import timedelta


class Agenda(QScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)
        #   Week in display
        self.displayed_week = []
        #   Default sizes
        self.df = DefaultSizes()
        #   Agenda object
        self.agenda_obj = GetAgendaEntries('A01260409')
        self.appointments = []
        #   Displayed appointments
        self.displayed_appointments = []
        #   False = 6 days displayed | True = 5 days displayed
        self.work_week = True
        #   Widget containing calendar, contained within QScrollArea
        self.agenda_widget = QWidget(self)
        #   Widgets being displayed at the weekend
        self.widgets_at_weekend = []
        #   Headers
        self.day_headers = []
        #   Visual lines separating the hours
        self.line_separators = []
        #   Grid Layout for the calendar
        self.my_layout = QGridLayout()
        #   Set up the basic structure
        self.init_ui()

    def place_entries(self):
        #   5-day week
        if self.work_week:
            for entry in self.appointments:
                #   Unpack data
                widget, row, column, row_span, column_span = entry
                #   Keep track of weekend widgets
                if column > (5 * self.df.header_column_span) + self.df.timestamp_column_span:
                    self.widgets_at_weekend.append((row, column, widget))
                # Add widget
                self.my_layout.addWidget(widget, row, column, row_span, column_span)
        else:
            #   TODO Prevent adding appointments on weekends
            print('a')

    def switch_work_week(self):
        """     Switch between work week & weekend      """
        #   If work week is currently being displayed
        if self.work_week:
            #   Remove weekend
            self.remove_weekend_widgets()
            self.work_week = not self.work_week
        else:
            #   Add back the weekend
            self.crate_day_columns(False)
            self.work_week = not self.work_week

    def remove_weekend_widgets(self):
        for thing in self.widgets_at_weekend:
            row, column, widget = thing
            #   Remove widget from the layout
            self.my_layout.removeWidget(widget)
            #   Delete widget
            widget.deleteLater()
            #   Remove last 2_day headers
            if row == 0:
                self.day_headers.pop(-1)
        #   Update array as widgets no longer exist
        self.widgets_at_weekend = []

    def clear_appointments(self):
        for entry in self.appointments:
            widget, row, column, row_span, column_span = entry
            self.my_layout.removeWidget(widget)
            #   Delete widgets
            widget.deleteLater()
        #   Update array as widgets no longer exist
        self.appointments = []

    def update_displayed_week(self, week_days=None):
        """     Show appointments in the week       """
        #   Retrieve agenda (Month)
        my_agenda = self.agenda_obj.get_agenda()
        #   Filter the entries of the week
        self.displayed_appointments = [appointment for appointment in my_agenda if week_days[0] <= appointment['start']
                                       <= week_days[-1]]
        #   Display entries if exist
        if self.displayed_appointments:
            #   Clear appointments
            self.clear_appointments()
            #   Place appointments
            self.schedules_into_coordinates()
        else:
            #   Clear entries
            self.clear_appointments()
        """     Update headers      """
        #   Traverse each header and update its number
        for index, header in enumerate(self.day_headers):
            #   Extract only the day
            header.update_number_text(week_days[index].strftime('%d'))

    def schedules_into_coordinates(self):
        """     Interpret appointments into coordinates     """
        for entry in self.displayed_appointments:
            #   Extraction.
            start = entry['start'].time()
            end = entry['end'].time()
            #   Hours into minutes + minutes + header + line
            row_start = ((start.hour * 60) + start.minute) + (self.df.header_row_span + self.df.line_row_span)
            # my_row_end = ((end.hour * 60) + end.minute) + (self.df.header_row_span + self.df.line_row_span)
            #   Subtract End - Start = Duration.
            t1 = timedelta(hours=start.hour, minutes=start.minute)
            t2 = timedelta(hours=end.hour, minutes=end.minute)
            duration = int((t2 - t1).total_seconds() / 60)
            #   Locate & consider hourly lines.
            for row, widget in self.line_separators:
                #   For each line contained inside the meeting add line_row_span
                if row_start <= row - self.df.header_row_span <= ((end.hour * 60) + end.minute):
                    duration += self.df.line_row_span
            """
            #   Move starting point for each hour
            for hour in range(24):
                if my_row_start > hour:
                    my_row_start += 1
                if my_row_end > hour:
                    my_duration += 1
                    my_row_end += 1
            """
            #   Sunday is 0 by default, but we need it to be 6
            my_start_date = entry['start'].date()
            #   Retrieve day/column
            column = 6 if int(my_start_date.strftime("%w")) == 0 else int(my_start_date.strftime("%w")) - 1
            column = (column * self.df.header_column_span) + self.df.timestamp_column_span
            #   Widget, Row=StartTime, Column=Day, RowSpan=Duration, ColSpan=Default_2
            self.appointments.append((FrameEntry(self, entry), row_start, column, duration, self.df.header_column_span))
        #   Place appointments into UI
        self.place_entries()

    @staticmethod
    def hour24format(hour=0):
        #   Regular numbers into 24:00 hrs format.
        if hour < 10:
            return '0{}:00'.format(hour)
        else:
            return '{}:00'.format(hour)

    """     UI      """
    def set_grid_layout(self):
        #   There are 14464 minutes in a Day + 24 for the separators + 60 for the headers
        #   Remove spacing
        self.my_layout.setSpacing(0)
        """     Customizing base layout      """
        #   7 Day view by default.
        #   Create first 5 days (work week).
        self.crate_day_columns()
        #   Create lass two days (weekend).
        self.crate_day_columns(False)
        #   Create hourly separators.
        self.create_hours_rows()

    def crate_day_columns(self, work_week=True):
        #   Determine which days are being created.
        if work_week:
            columns = 5
        else:
            columns = 2
        """     Add day headers        """
        #   Consider 5 previous days when adding a weekend
        last_used_column = 0 if work_week else (5 * self.df.header_column_span)
        last_used_column += self.df.timestamp_column_span
        for column in range(columns) if work_week else range(5, 7):
            #   Header widget
            header = DayHeader(self, 1, column)
            self.day_headers.append(header)
            if not work_week:
                self.widgets_at_weekend.append((0, column, header))
            #   Place widget
            self.my_layout.setColumnStretch(last_used_column, self.df.header_row_span)
            self.my_layout.addWidget(header, 0, last_used_column, self.df.header_row_span, self.df.header_column_span)
            #   Add space used
            last_used_column += self.df.header_column_span

    def create_hours_rows(self):
        #   24-hour format
        hours = range(25)
        """     Customizing layout      """
        #   Sizes
        last_used_row = 0
        #   Empty top left corner
        last_used_row += self.df.header_row_span
        #   Add timestamp (First column)
        for hour in hours:
            #   Move to unused row
            last_used_row += 1
            #   Place line
            line = LineFrame()
            #   TODO further testing for line delimiters
            self.my_layout.addWidget(line, last_used_row, 0, self.df.line_row_span, self.my_layout.columnCount())
            self.line_separators.append((last_used_row, line))
            #   Add space used
            last_used_row += self.df.line_row_span
            #   Add label
            self.my_layout.setRowStretch(last_used_row, self.df.timestamp_row_span)
            self.my_layout.addWidget(TimeLabelWidget(self, self.hour24format(hour)), last_used_row, 0,
                                     self.df.timestamp_row_span, self.df.timestamp_column_span)
            #   Add space used
            last_used_row += self.df.timestamp_row_span

    def init_ui(self):
        """     Customize ScrollArea UI        """
        #   Remove horizontal scroll bar
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        #   Make widget use the whole scroll Area
        self.setWidgetResizable(False)
        self.setMinimumWidth(900)
        # self.setMaximumWidth()
        # self.setMinimumHeight(500)
        # self.setMaximumHeight()
        """     Customize Widget UI        """
        #   Create the grid layout
        self.set_grid_layout()
        #   Add the layout to our widget
        self.agenda_widget.setLayout(self.my_layout)
        self.agenda_widget.setMinimumWidth(900)
        #   Place the widget inside our scroll
        self.setWidget(self.agenda_widget)
        self.agenda_widget.setContentsMargins(0, 0, 0, 0)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)


class TimeLabelWidget(QWidget):
    def __init__(self, parent=None, text=''):
        super().__init__(parent)
        my_layout = QVBoxLayout()
        label = QLabel(text)
        my_layout.addWidget(label)
        self.setLayout(my_layout)
        self.setMinimumSize(50, 10)


class DefaultSizes:
    """     Calendar proportions      """
    def __init__(self):
        #   Size of the first column
        self.timestamp_column_span = 1
        #   Day columns
        self.header_column_span = 2
        #   Size of headers containing number & day
        self.header_row_span = 5
        #   Size of each timestamp
        #   60 as one rows represents a single minute
        self.timestamp_row_span = 60
        #   Size of the lines separating representing the hours
        self.line_row_span = 1
