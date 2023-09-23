from PyQt6.QtWidgets import QPlainTextEdit, QWidget, QPushButton, QStackedWidget, QFrame, QVBoxLayout,  QHBoxLayout
from PySide6.QtCore import Slot
from UI.Widgets.Calendar.calendar_agenda_widget import CalendarAgendaWidget


class ScheduleFrame(QWidget):
    def __init__(self):
        super().__init__()
        my_layout = QVBoxLayout()
        my_layout.addWidget(CalendarAgendaWidget())
        self.setLayout(my_layout)
