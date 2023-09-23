from PyQt6.QtWidgets import QCalendarWidget
from PyQt6.QtGui import QColor, QTextCharFormat


#   https://www.geeksforgeeks.org/pyqt5-qcalendarwidget-selection-changed-signal/
class CustomCalendar(QCalendarWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.tune_ui()
        self.holidays = None

    def update_holidays(self, holidays=None):
        self.holidays = holidays if not None else []
        self.highlight_holidays()

    """     UI      """
    def highlight_holidays(self):
        #   Holiday text format
        holiday_txt_frmt = QTextCharFormat()
        #   Color
        holiday_txt_frmt.setForeground(QColor('#9FF40A'))
        #   Set format for holidays
        for holiday in self.holidays:
            self.setDateTextFormat(holiday['date'], holiday_txt_frmt)

    def tune_ui(self):
        print()
