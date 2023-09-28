from UI.Frames.frame import Frame
from PyQt6.QtWidgets import QVBoxLayout
from UI.Widgets.Calendar.calendar_agenda_widget import CalendarAgendaWidget


class ScheduleFrame(Frame):
    def __init__(self, parent=None, button_paths=None):
        super().__init__(parent, button_path=button_paths.agenda)
        self.name = 'Agenda'
        my_layout = QVBoxLayout()
        my_layout.addWidget(CalendarAgendaWidget())
        self.setLayout(my_layout)
